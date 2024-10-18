import copy
from colorama import Back, Style, Fore, init
from exceptions import NotCorrectCell, NotCorrectInput

EMPTY_CELL = " "
BLACK_CHECKER_CELL = Fore.BLACK + "o"
BLACK_QUEEN_CHECKER_CELL = Fore.BLACK + "0"
WHITE_CHECKER_CELL = Fore.LIGHTWHITE_EX + "o"
WHITE_QUEEN_CHECKER_CELL = Fore.LIGHTWHITE_EX + "0"
POSSIBLE_CELL = Fore.LIGHTGREEN_EX + "o"
POSSIBLE_QUEEN_CELL = Fore.LIGHTGREEN_EX + "0"
EATING_CHECKER_CELL = Fore.RED + "o"
EATING_QUEEN_CHECKER_CELL = Fore.RED + "0"

BLACK_WIN = Fore.CYAN + 'Black WIN!!! Congratulations!!!' + Style.RESET_ALL
WHITE_WIN = Fore.CYAN + 'White WIN!!! Congratulations!!!' + Style.RESET_ALL

BOARD_DICT = {
              18: EMPTY_CELL, 28: BLACK_CHECKER_CELL, 38: EMPTY_CELL, 48: BLACK_CHECKER_CELL, 58: EMPTY_CELL, 68: BLACK_CHECKER_CELL, 78: EMPTY_CELL, 88: BLACK_CHECKER_CELL,
              17: BLACK_CHECKER_CELL, 27: EMPTY_CELL, 37: BLACK_CHECKER_CELL, 47: EMPTY_CELL, 57: BLACK_CHECKER_CELL, 67: EMPTY_CELL, 77: BLACK_CHECKER_CELL, 87: EMPTY_CELL,
              16: EMPTY_CELL, 26: BLACK_CHECKER_CELL, 36: EMPTY_CELL, 46: BLACK_CHECKER_CELL, 56: EMPTY_CELL, 66: BLACK_CHECKER_CELL, 76: EMPTY_CELL, 86: BLACK_CHECKER_CELL,
              15: EMPTY_CELL, 25: EMPTY_CELL, 35: EMPTY_CELL, 45: EMPTY_CELL, 55: EMPTY_CELL, 65: EMPTY_CELL, 75: EMPTY_CELL, 85: EMPTY_CELL,
              14: EMPTY_CELL, 24: EMPTY_CELL, 34: EMPTY_CELL, 44: EMPTY_CELL, 54: EMPTY_CELL, 64: EMPTY_CELL, 74: EMPTY_CELL, 84: EMPTY_CELL,
              13: WHITE_CHECKER_CELL, 23: EMPTY_CELL, 33: WHITE_CHECKER_CELL, 43: EMPTY_CELL, 53: WHITE_CHECKER_CELL, 63: EMPTY_CELL, 73: WHITE_CHECKER_CELL, 83: EMPTY_CELL,
              12: EMPTY_CELL, 22: WHITE_CHECKER_CELL, 32: EMPTY_CELL, 42: WHITE_CHECKER_CELL, 52: EMPTY_CELL, 62: WHITE_CHECKER_CELL, 72: EMPTY_CELL, 82: WHITE_CHECKER_CELL,
              11: WHITE_CHECKER_CELL, 21: EMPTY_CELL, 31: WHITE_CHECKER_CELL, 41: EMPTY_CELL, 51: WHITE_CHECKER_CELL, 61: EMPTY_CELL, 71: WHITE_CHECKER_CELL, 81:  EMPTY_CELL
}

BOARD_COLOR_LIST = [
    [Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX],
    [Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE],
    [Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX],
    [Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE],
    [Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX],
    [Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE],
    [Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX],
    [Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE, Back.LIGHTBLACK_EX, Back.WHITE],
]

#----------------------------------------------------------------------------------------------------------------------

class Board:
    def __init__(self, board):
        self.board = board

    def show(self):
        checker_pos = 18
        number = 8
        for i in BOARD_COLOR_LIST:
            print(str(number) + " ", end='')
            for j in i:
                print(j +' ' + self.board[checker_pos] + ' ', end='')
                checker_pos += 10
            print(Style.RESET_ALL)
            checker_pos -= 81
            number -= 1
        print("   A  B  C  D  E  F  G  H")
        print("   1  2  3  4  5  6  7  8")

    def return_board(self):
        return self.board

    def make_possible_staps(self, staps, eating_checkers):
        for stap in staps:
            self.board[stap] = POSSIBLE_CELL
        for checker in eating_checkers:
            self.board[checker] = EATING_CHECKER_CELL

    def is_win(self):
        count = [0, 0] # count[0] - white, count[1] - black
        for checker in self.board:
            if self.board[checker] == WHITE_CHECKER_CELL:
                count[0] += 1
            elif self.board[checker] == BLACK_CHECKER_CELL:
                count[1] += 1
        if count[0] == 0:
            return BLACK_WIN
        elif count[1] == 0:
            return WHITE_WIN
        else:
            return 0

    def make_stap(self):
        pass

class Checker:
    def __init(self, int_checker, board):
        self.int_checker = int_checker
        self.board = board


class WhiteChecker(Checker):
    pass


class BlackChecker(Checker):
    pass


class WhiteQueenChecker(WhiteChecker):
    pass


class BlackQueenChecker(BlackChecker):
    pass

# ----------------------------------------------------------------------------------------------------------------------

def check_inp_checker(inp_str_checker, board):
    type_of_now_checker = [[WHITE_CHECKER_CELL, WHITE_QUEEN_CHECKER_CELL], [BLACK_CHECKER_CELL, BLACK_QUEEN_CHECKER_CELL]]
    try:
        if len(inp_str_checker) == 2 and not inp_str_checker[0].isdigit() and inp_str_checker[1].isdigit():
            out_int_checker = int(str(ord(inp_str_checker[0].lower()) - ord("a") + 1) + inp_str_checker[1])
            if out_int_checker in board and board[out_int_checker] != EMPTY_CELL:
                return out_int_checker
            else:
                raise NotCorrectCell
        else:
            raise NotCorrectInput
    except NotCorrectCell as ex:
        ex(inp=out_int_checker, err='You chose empty cell.')
        new_inp_str_checker = input("Enter the checker, which will go (like A3 or a3):")
        check_inp_checker(new_inp_str_checker, board)
    except NotCorrectInput as ex:
        ex(inp_str_checker)
        new_inp_str_checker = input("Enter the checker, which will go (like A3 or a3):")
        check_inp_checker(new_inp_str_checker, board)

def create_checker(out_checker, board, iteration):
    try:
        if iteration % 2 == 0:
            if board.return_board()[out_checker] == WHITE_CHECKER_CELL:
                checker = WhiteChecker()
            elif board.return_board()[out_checker] == WHITE_QUEEN_CHECKER_CELL:
                checker = WhiteQueenChecker()
            else:
                raise NotCorrectCell
        elif iteration % 2 != 0:
            if board.return_board()[out_checker] == BLACK_CHECKER_CELL:
                checker = BlackChecker()
            elif board.return_board()[out_checker] == BLACK_QUEEN_CHECKER_CELL:
                checker = BlackQueenChecker()
            else:
                raise NotCorrectCell
    except NotCorrectCell as ex:
        ex(inp=out_checker, err='You chose checker other color.')
        new_inp_str_checker = input("Enter the checker, which will go (like A3 or a3):")
        check_inp_checker(new_inp_str_checker, board)

# ----------------------------------------------------------------------------------------------------------------------

def main():
    init()
    one_more = True
    while one_more:
        running = True
        board = copy.deepcopy(BOARD_DICT)
        iteration = 2  #itaration%2 == 0 go white, iteration%2 != 0 - go black
        while running:
            now_board = Board(board)
            now_board.show()
            inp_checker = input("Enter the checker, which will go (like A3 or a3):")
            out_checker = check_inp_checker(inp_checker, now_board.return_board())


        #defs: eat_staps_if_can_eat(try do it), enter_and_check_checker, create_checker, get_possible_staps, enter_and_check_stap, check_win,

if __name__ == '__main__':
    main()
