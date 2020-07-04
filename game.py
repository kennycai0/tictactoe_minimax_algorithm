import copy
from random import randint


class TicTacToe:

    def __init__(self):
        self.cells = []
        self.board = None
        self.player_one = None
        self.player_two = None
        self.computer_mode = None

    def coordinate_board(self, cells="_" * 9):
        self.board = []
        keys = [(1, 3), (2, 3), (3, 3), (1, 2), (2, 2), (3, 2), (1, 1), (2, 1), (3, 1)]
        for i in range(9):
            cell_w_coordinate = {keys[i]: cells[i]}
            self.board.append(copy.deepcopy(cell_w_coordinate))

    def show_board(self):
        print("---------")
        for i in range(0, 9, 3):
            val0 = next(iter(self.board[i].values()))
            val1 = next(iter(self.board[i + 1].values()))
            val2 = next(iter(self.board[i + 2].values()))
            print(f"| {val0 if val0 != '_' else ' '} {val1 if val1 != '_' else ' '} {val2 if val2 != '_' else ' '} |")
        print("---------")

    def user_enter_coordinate(self, symbol):
        try:
            x, y = input("Enter the coordinates: ").split()
            x = int(x)
            y = int(y)
        except ValueError:
            print("You should enter numbers!")
            return False

        coordinate = (x, y)
        for i in range(9):
            for k, v in self.board[i].items():
                if k == coordinate:
                    if v == "_":
                        self.board[i][k] = symbol
                        return True
                    else:
                        print("This cell is occupied! Choose another one!")
                        return False
        print("Coordinates should be from 1 to 3!")
        return False

    def outcome(self):
        winner = self.winner()
        if winner:
            return winner
        elif self.finished():
            return True
        else:
            return False

    def winner(self):
        self.cells = []
        for i in range(9):
            self.cells.append(next(iter(self.board[i].values())))
        # rows
        for i in range(0, 9, 3):
            if self.cells[i] == "X" and self.cells[i + 1] == "X" and self.cells[i + 2] == "X":
                return "X"
            elif self.cells[i] == "O" and self.cells[i + 1] == "O" and self.cells[i + 2] == "O":
                return "O"

        # columns
        for i in range(3):
            if self.cells[i] == "X" and self.cells[i + 3] == "X" and self.cells[i + 6] == "X":
                return "X"
            elif self.cells[i] == "O" and self.cells[i + 3] == "O" and self.cells[i + 6] == "O":
                return "O"

        # diagonals
        if self.cells[0] == "X" and self.cells[4] == "X" and self.cells[8] == "X":
            return "X"
        elif self.cells[0] == "O" and self.cells[4] == "O" and self.cells[8] == "O":
            return "O"
        if self.cells[2] == "X" and self.cells[4] == "X" and self.cells[6] == "X":
            return "X"
        elif self.cells[2] == "O" and self.cells[4] == "O" and self.cells[6] == "O":
            return "O"

        return False

    def finished(self):
        for i in range(9):
            for k, v in self.board[i].items():
                if v == "_":
                    return False
        return True

    def select_players(self):
        commands = input("Input command: ").split()
        try:
            if commands[0] == "start":
                self.player_one, self.player_two = commands[1], commands[2]
                return True
            elif commands[0] == "exit":
                return commands[0]
        except IndexError:
            print("Bad parameters")

    def who_playing(self, player, symbol):
        if player == "user":
            return self.user_enter_coordinate(symbol)
        elif player == "easy":
            self.computer_mode = "easy"
            print('Making move level "easy"')
            return self.easy_robot(symbol)
        elif player == "medium":
            self.computer_mode = "medium"
            print('Making move level "medium"')
            return self.medium_robot(symbol)
        elif player == "hard":
            self.computer_mode = "hard"
            print('Making move level "hard"')
            return self.hard_robot(symbol)

    def easy_robot(self, symbol):
        while True:
            robot_chose_number = randint(0, 8)
            for k, v in self.board[robot_chose_number].items():
                if v == "_":
                    self.board[robot_chose_number][k] = symbol
                    return True

    def medium_robot(self, symbol):

        move_to_make = self.check_move(symbol)

        if not move_to_make:
            move_to_make = self.check_move("O" if symbol == "X" else "X")

        if move_to_make:
            for k, v in self.board[move_to_make].items():
                self.board[move_to_make][k] = symbol
        else:
            self.easy_robot(symbol)

        return True

    def check_move(self, symbol):
        self.cells = []
        for i in range(9):
            self.cells.append(next(iter(self.board[i].values())))
        # rows
        for i in range(0, 9, 3):
            if self.cells[i] == symbol and self.cells[i + 1] == symbol and self.cells[i + 2] == "_":
                return i + 2
            elif self.cells[i] == symbol and self.cells[i + 1] == "_" and self.cells[i + 2] == symbol:
                return i + 1
            elif self.cells[i] == "_" and self.cells[i + 1] == symbol and self.cells[i + 2] == symbol:
                return i
        # columns
        for i in range(3):
            if self.cells[i] == symbol and self.cells[i + 3] == symbol and self.cells[i + 6] == "_":
                return i + 6
            elif self.cells[i] == symbol and self.cells[i + 3] == "_" and self.cells[i + 6] == symbol:
                return i + 3
            elif self.cells[i] == "_" and self.cells[i + 3] == symbol and self.cells[i + 6] == symbol:
                return i

        # diagonals
        if self.cells[0] == symbol and self.cells[4] == symbol and self.cells[8] == "_":
            return 8
        elif self.cells[0] == symbol and self.cells[4] == "_" and self.cells[8] == symbol:
            return 4
        elif self.cells[0] == "_" and self.cells[4] == symbol and self.cells[8] == symbol:
            return 0

        # other diagonal
        if self.cells[2] == symbol and self.cells[4] == symbol and self.cells[6] == "_":
            return 6
        elif self.cells[2] == symbol and self.cells[4] == "_" and self.cells[6] == symbol:
            return 4
        elif self.cells[2] == "_" and self.cells[4] == symbol and self.cells[6] == symbol:
            return 2

        return False

    def hard_robot(self, symbol):
        if symbol == "X":
            m, index = self.min()
            for k in self.board[index]:
                self.board[index][k] = symbol
        else:
            m, index = self.max()
            for k in self.board[index]:
                self.board[index][k] = symbol
        return True

    def max(self):
        maxv = -2
        index = None
        result = self.outcome()

        if result == "X":
            return -1, 0
        elif result == "O":
            return 1, 0
        elif result is True:
            return 0, 0

        for i in range(9):
            for k, v in self.board[i].items():
                if v == "_":
                    self.board[i][k] = "O"
                    m, min_index = self.min()
                    if m > maxv:
                        maxv = m
                        index = i
                    self.board[i][k] = "_"
        return maxv, index

    def min(self):
        minv = 2
        index = None
        result = self.outcome()

        if result == "X":
            return -1, 0
        elif result == "O":
            return 1, 0
        elif result is True:
            return 0, 0

        for i in range(9):
            for k, v in self.board[i].items():
                if v == "_":
                    self.board[i][k] = "X"
                    m, max_index = self.max()
                    if m < minv:
                        minv = m
                        index = i
                    self.board[i][k] = "_"
        return minv, index


game = TicTacToe()

while True:

    actions = game.select_players()
    if actions == "exit":
        break
    if actions is None:
        continue
    game.coordinate_board()
    game.show_board()

    while True:

        while True:
            if game.who_playing(game.player_one, "X"):
                break

        outcome = game.outcome()
        game.show_board()
        if outcome == "X" or outcome == "O":
            print(f"{outcome} wins")
            break
        elif outcome is True:
            print("Draw")
            break

        while True:
            if game.who_playing(game.player_two, "O"):
                break

        outcome = game.outcome()
        game.show_board()
        if outcome == "X" or outcome == "O":
            print(f"{outcome} wins")
            break
        elif outcome is True:
            print("Draw")
            break

# COORDINATE TABLE
# (1, 3) (2, 3) (3, 3)
# (1, 2) (2, 2) (3, 2)
# (1, 1) (2, 1) (3, 1)
