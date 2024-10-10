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

# BOARD_DICT = {
#               18: EMPTY_CELL, 28: EMPTY_CELL, 38: EMPTY_CELL, 48: EMPTY_CELL, 58: EMPTY_CELL, 68: EMPTY_CELL, 78: EMPTY_CELL, 88: EMPTY_CELL,
#               17: EMPTY_CELL, 27: EMPTY_CELL, 37: EMPTY_CELL, 47: EMPTY_CELL, 57: EMPTY_CELL, 67: EMPTY_CELL, 77: EMPTY_CELL, 87: EMPTY_CELL,
#               16: EMPTY_CELL, 26: EMPTY_CELL, 36: EMPTY_CELL, 46: EMPTY_CELL, 56: EMPTY_CELL, 66: EMPTY_CELL, 76: EMPTY_CELL, 86: EMPTY_CELL,
#               15: EMPTY_CELL, 25: EMPTY_CELL, 35: EMPTY_CELL, 45: EMPTY_CELL, 55: EMPTY_CELL, 65: EMPTY_CELL, 75: EMPTY_CELL, 85: EMPTY_CELL,
#               14: EMPTY_CELL, 24: EMPTY_CELL, 34: EMPTY_CELL, 44: BLACK_CHECKER_CELL, 54: EMPTY_CELL, 64: EMPTY_CELL, 74: EMPTY_CELL, 84: EMPTY_CELL,
#               13: EMPTY_CELL, 23: EMPTY_CELL, 33: EMPTY_CELL, 43: EMPTY_CELL, 53: EMPTY_CELL, 63: EMPTY_CELL, 73: EMPTY_CELL, 83: EMPTY_CELL,
#               12: EMPTY_CELL, 22: BLACK_CHECKER_CELL, 32: EMPTY_CELL, 42: EMPTY_CELL, 52: EMPTY_CELL, 62: EMPTY_CELL, 72: EMPTY_CELL, 82: EMPTY_CELL,
#               11: WHITE_CHECKER_CELL, 21: EMPTY_CELL, 31: EMPTY_CELL, 41: EMPTY_CELL, 51: EMPTY_CELL, 61: EMPTY_CELL, 71: EMPTY_CELL, 81:  EMPTY_CELL
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

class Checker:
    def __init__(self, board):
        self.board = board
        self.out_checker = ''
        self.out_stap = ''
        self.eating_checkers = []
        self.staps = []

    def enter_checker(self, in_str = "Enter the checker, which will go (like A3 or a3):"):
        self.get_checker(input(in_str))

    def get_checker(self, str_checker):
        try:
            if len(str_checker) == 2 and not str_checker[0].isdigit() and str_checker[1].isdigit():
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

    def eat(self):
        # staps.append(self.eat_checker)
        # eating_checker_and_stap += [self.eat_checker,  (self.eat_checker + (self.eat_checker - int(self.out_checker)))]
        # if self.can_eat_ques(int(self.eat_checker)):
        #     self.eat(staps, eating_checker_and_stap)
        # return staps, eating_checker_and_stap
        pass


class BlackChecker(Checker):
    def get_possible_staps(self):
        self.can_eat(int(self.out_checker))
        if len(self.eating_checkers) != 0:
            return self.staps, self.eating_checkers
        staps = [int(self.out_checker) - 11, int(self.out_checker) + 9]
        for stap_index, stap in enumerate(staps):
            if not stap in self.board:
                staps[stap_index] = 0
            elif self.board[stap] == BLACK_CHECKER_CELL:
                staps[stap_index] = 0
        staps = [stap for stap in staps if stap != 0]
        self.staps += staps
        return self.staps, self.eating_checkers

    def make_stap(self, stap):
        if len(self.eating_checkers) != 0:
            for eating_checker in self.eating_checkers:
                self.board[eating_checker] = EMPTY_CELL
        self.board[int(self.out_checker)] = EMPTY_CELL
        self.board[int(self.out_stap)] = BLACK_CHECKER_CELL

    def can_eat(self, checker):
        staps = [(checker - 11), (checker + 11), (checker - 9), (checker + 9)]
        print(Fore.BLACK + 'def' + Style.RESET_ALL)
        for stap in staps:
            if stap in self.board and self.board[stap] == WHITE_CHECKER_CELL and not stap in self.eating_checkers:
                if self.board[stap] == WHITE_CHECKER_CELL and self.board[2*stap - checker]:
                    self.eating_checkers += [stap]
                    self.staps = [2*self.eating_checkers[-1] - checker]
                    self.can_eat(self.staps[-1])


class WhiteChecker(Checker):
    def get_possible_staps(self):
        self.can_eat(int(self.out_checker))
        if len(self.eating_checkers) != 0:
            return self.staps, self.eating_checkers
        staps = [int(self.out_checker) + 11, int(self.out_checker) - 9]
        for stap_index, stap in enumerate(staps):
            if not stap in self.board:
                staps[stap_index] = 0
            elif self.board[stap] == WHITE_CHECKER_CELL:
                staps[stap_index] = 0
        staps = [stap for stap in staps if stap != 0]
        self.staps += staps
        return self.staps, self.eating_checkers

    def make_stap(self, stap):
        if len(self.eating_checkers) != 0:
            for eating_checker in self.eating_checkers:
                self.board[eating_checker] = EMPTY_CELL
        self.board[int(self.out_checker)] = EMPTY_CELL
        self.board[int(self.out_stap)] = WHITE_CHECKER_CELL

    def can_eat(self, checker):
        staps = [(checker - 11), (checker + 11), (checker - 9), (checker + 9)]
        for stap in staps:
            if stap in self.board and self.board[stap] == BLACK_CHECKER_CELL and not stap in self.eating_checkers:
                if self.board[stap] == BLACK_CHECKER_CELL and self.board[2*stap - checker]:
                    self.eating_checkers += [stap]
                    self.staps = [2*self.eating_checkers[-1] - checker]
                    self.can_eat(self.staps[-1])


class BlackQueenChecker(BlackChecker):
    pass


class WhiteQueenChecker(WhiteChecker):
    pass


def main():
    init()
    one_more = True
    while one_more:
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
            check_checker = True
            while check_checker:
                checker.enter_checker()
                chosen_checker = checker.out_checker
                if chosen_checker != '':
                    check_checker = False
            chosen_checker = int(chosen_checker)
            print()
            print(21*'-')
            print()
            check_possible_staps = True
            while check_possible_staps:
                possible_staps, eating_checkers = checker.get_possible_staps()
                if len(possible_staps) == 0:
                    board.show()
                    if iteration % 2 == 0:
                        print(Fore.GREEN, 'White go:', Style.RESET_ALL)
                    else:
                        print(Fore.GREEN, 'Black go:', Style.RESET_ALL)
                    checker.enter_checker('You chose checker, which can not go. Try again:')
                    chosen_checker = int(checker.out_checker)
                    possible_staps, eating_checkers = checker.get_possible_staps()
                else:
                    check_possible_staps = False
            possible_board = Board(copy.deepcopy(now_board))
            possible_board.make_possible_staps(possible_staps, eating_checkers)
            possible_board.show()
            del possible_board
            check_enter_stap = True
            while check_enter_stap:
                checker.enter_stap(possible_staps)
                chosen_stap = checker.out_stap
                if chosen_checker != '':
                    check_enter_stap = False
            checker.make_stap(chosen_stap)
            print(21*'-')
            iw = board.is_win()
            if iw != 0:
                board.show()
                print(iw)
                check_input_cg = True
                while check_input_cg:
                    continue_game = input('Would you like to play one more game?!(Y/n):')
                    if continue_game.lower() == 'y' or continue_game.lower() == 'n':
                        check_input_cg = False
                if continue_game.lower() == 'y':
                    running = False
                    one_more = True
                    continue
                else:
                    one_more = False
                    break
            iteration += 1
            del checker

if __name__ == "__main__":
    main()