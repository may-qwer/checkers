import copy
from colorama import Back, Style, Fore, init
from exceptions import NotCorrectCell, NotCorrectInput

EMPTY_CELL = " "
BLACK_CHECKER_CELL = Fore.BLACK + "o"
BLACK_QUEEN_CHECKER_CELL = Fore.BLACK + "0"
WHITE_CHECKER_CELL = Fore.LIGHTWHITE_EX + "o"
WHITE_QUEEN_CHECKER_CELL = Fore.LIGHTWHITE_EX + "0"
POSSIBLE_CELL = Fore.LIGHTGREEN_EX + "o"


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

# BOARD_DICT = {
#               18: EMPTY_CELL, 28: BLACK_CHECKER_CELL, 38: EMPTY_CELL, 48: BLACK_CHECKER_CELL, 58: EMPTY_CELL, 68: BLACK_CHECKER_CELL, 78: EMPTY_CELL, 88: BLACK_CHECKER_CELL,
#               17: BLACK_CHECKER_CELL, 27: EMPTY_CELL, 37: BLACK_CHECKER_CELL, 47: EMPTY_CELL, 57: BLACK_CHECKER_CELL, 67: EMPTY_CELL, 77: BLACK_CHECKER_CELL, 87: EMPTY_CELL,
#               16: EMPTY_CELL, 26: BLACK_CHECKER_CELL, 36: EMPTY_CELL, 46: BLACK_CHECKER_CELL, 56: EMPTY_CELL, 66: BLACK_CHECKER_CELL, 76: EMPTY_CELL, 86: BLACK_CHECKER_CELL,
#               15: EMPTY_CELL, 25: BLACK_CHECKER_CELL, 35: EMPTY_CELL, 45: EMPTY_CELL, 55: EMPTY_CELL, 65: EMPTY_CELL, 75: EMPTY_CELL, 85: EMPTY_CELL,
#               14: WHITE_CHECKER_CELL, 24: EMPTY_CELL, 34: EMPTY_CELL, 44: EMPTY_CELL, 54: EMPTY_CELL, 64: EMPTY_CELL, 74: EMPTY_CELL, 84: EMPTY_CELL,
#               13: WHITE_CHECKER_CELL, 23: EMPTY_CELL, 33: WHITE_CHECKER_CELL, 43: EMPTY_CELL, 53: WHITE_CHECKER_CELL, 63: EMPTY_CELL, 73: WHITE_CHECKER_CELL, 83: EMPTY_CELL,
#               12: EMPTY_CELL, 22: WHITE_CHECKER_CELL, 32: EMPTY_CELL, 42: WHITE_CHECKER_CELL, 52: EMPTY_CELL, 62: WHITE_CHECKER_CELL, 72: EMPTY_CELL, 82: WHITE_CHECKER_CELL,
#               11: WHITE_CHECKER_CELL, 21: EMPTY_CELL, 31: WHITE_CHECKER_CELL, 41: EMPTY_CELL, 51: WHITE_CHECKER_CELL, 61: EMPTY_CELL, 71: WHITE_CHECKER_CELL, 81:  EMPTY_CELL
# }


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
        print("   A  B  C  D  E  F  G  H ")
        print("   1  2  3  4  5  6  7  8 ")

    def make_possible_staps(self, staps):
        for stap in staps:
            self.board[stap] = POSSIBLE_CELL


class Checker:
    def __init__(self, board):
        self.board = board
        self.out_checker = ''
        self.out_stap = ''

    def enter_checker(self):
        self.get_checker(input("Enter the checker, which will go (like A3 or a3):"))

    def get_checker(self, str_checker):
        try:
            if not str_checker[0].isdigit() and str_checker[1].isdigit() and len(str_checker) == 2:
                num_checker = str(ord(str_checker[0].lower()) - ord("a") + 1) + str_checker[1]
                if int(num_checker[0]) >= 1 and int(num_checker[0]) <= 8 and int(num_checker[1]) >= 1 and int(num_checker[1]) <= 8 and self.board[int(num_checker)] != EMPTY_CELL:
                    self.out_checker = num_checker
                else:
                    raise NotCorrectCell
            else:
                raise NotCorrectInput
        except NotCorrectCell as ex:
            del str_checker, num_checker
            ex('You chose empty cell.')
            self.out_checker = ''
            self.enter_checker()
        except NotCorrectInput as ex:
            ex(str_checker)
            del str_checker
            self.out_checker = ''
            self.enter_checker()

    def enter_stap(self, staps):
        self.get_stap(input("Enter one of stap (like b4 or b4):"), staps)

    def get_stap(self, str_stap, staps):
        try:
            if not str_stap[0].isdigit() and str_stap[1].isdigit() and len(str_stap) == 2:
                num_stap = str(ord(str_stap[0].lower()) - ord("a") + 1) + str_stap[1]
                if int(num_stap[0]) >= 1 and int(num_stap[0]) <= 8 and int(num_stap[1]) >= 1 and int(num_stap[1]) <= 8 and int(num_stap) in staps:
                    self.out_stap = num_stap
                else:
                    raise NotCorrectCell
            else:
                raise NotCorrectInput
        except NotCorrectCell as ex:
            del str_stap, num_stap
            ex('You chose cell, you can not go into.')
            self.out_checker = ''
            self.enter_stap(staps)
        except NotCorrectInput as ex:
            ex(str_stap)
            del str_stap, num_stap
            self.out_checker = ''
            self.enter_stap(staps)



class BlackChecker(Checker):
    def get_possible_staps(self, checker):
        eating_checker_and_stap = []
        staps = [checker - 11, checker + 9]
        for stap in staps:
            if stap > 88:
                staps.remove(stap)
            elif stap < 11:
                staps.remove(stap)
            elif self.board[stap] == BLACK_CHECKER_CELL:
                staps.remove(stap)
            elif self.board[stap] == WHITE_CHECKER_CELL and self.board[stap+(stap-checker)] == EMPTY_CELL:
                staps.append(stap+(stap-checker))
                eating_checker_and_stap = [stap, (stap+(stap-checker))]
                staps.remove(stap)
        return staps, eating_checker_and_stap

    def make_stap(self, eating_checker_and_stap):
        if len(eating_checker_and_stap) != 0 and int(self.out_stap) == int(eating_checker_and_stap[1]):
            self.board[int(eating_checker_and_stap[0])] = EMPTY_CELL
        self.board[int(self.out_checker)] = EMPTY_CELL
        self.board[int(self.out_stap)] = BLACK_CHECKER_CELL


class WhiteChecker(Checker):
    def get_possible_staps(self, checker):
        eating_checker_and_stap = []
        staps = [checker + 11, checker - 9]
        print(staps)
        for stap in staps:
            print(stap)
            if stap > 88:
                staps.remove(stap)
            elif stap < 11:
                staps.remove(stap)
            elif self.board[stap] == WHITE_CHECKER_CELL:
                staps.remove(stap)
            elif self.board[stap] == BLACK_CHECKER_CELL and self.board[stap+(stap-checker)] == EMPTY_CELL:
                staps.append((stap+(stap-checker)))
                eating_checker_and_stap = [stap, (stap+(stap-checker))]
                staps.remove(stap)
        return staps, eating_checker_and_stap

    def make_stap(self, eating_checker_and_stap):
        if len(eating_checker_and_stap) != 0 and int(self.out_stap) == int(eating_checker_and_stap[1]):
            self.board[int(eating_checker_and_stap[0])] = EMPTY_CELL
        self.board[int(self.out_checker)] = EMPTY_CELL
        self.board[int(self.out_stap)] = WHITE_CHECKER_CELL




class BlackQueenChecker(BlackChecker):
    pass


class WhiteQueenChecker(WhiteChecker):
    pass


def main():
    init()
    running = True
    now_board = copy.deepcopy(BOARD_DICT)
    iteration = 2 #itaration%2 == 0 go white, iteration%2 != 0 - go black
    #iteration = 3
    while running:
        board = Board(now_board)
        board.show()
        if iteration % 2 == 0:
            checker = WhiteChecker(now_board)
            print(Fore.GREEN, 'White go:', Style.RESET_ALL)
        else:
            checker = BlackChecker(now_board)
            print(Fore.GREEN, 'Black go:', Style.RESET_ALL)
        checker.enter_checker()
        chosen_checker = checker.out_checker
        if chosen_checker == '':
            checker.enter_checker()
        chosen_checker = int(chosen_checker)
        print()
        print(21*'-')
        print()
        possible_staps, eating_checker_and_stap = checker.get_possible_staps(chosen_checker)
        possible_board = Board(copy.deepcopy(now_board))
        possible_board.make_possible_staps(possible_staps)
        possible_board.show()
        del possible_board
        checker.enter_stap(possible_staps)
        if checker.out_stap == '':
            checker.enter_stap(possible_staps)
        checker.make_stap(eating_checker_and_stap)
        print(21*'-')


        iteration += 1
        del checker




if __name__ == "__main__":
    main()