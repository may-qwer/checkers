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


# BOARD_DICT = {
#               18: EMPTY_CELL, 28: BLACK_CHECKER_CELL, 38: EMPTY_CELL, 48: BLACK_CHECKER_CELL, 58: EMPTY_CELL, 68: BLACK_CHECKER_CELL, 78: EMPTY_CELL, 88: BLACK_CHECKER_CELL,
#               17: BLACK_CHECKER_CELL, 27: EMPTY_CELL, 37: BLACK_CHECKER_CELL, 47: EMPTY_CELL, 57: BLACK_CHECKER_CELL, 67: EMPTY_CELL, 77: BLACK_CHECKER_CELL, 87: EMPTY_CELL,
#               16: EMPTY_CELL, 26: BLACK_CHECKER_CELL, 36: EMPTY_CELL, 46: BLACK_CHECKER_CELL, 56: EMPTY_CELL, 66: BLACK_CHECKER_CELL, 76: EMPTY_CELL, 86: BLACK_CHECKER_CELL,
#               15: EMPTY_CELL, 25: EMPTY_CELL, 35: EMPTY_CELL, 45: EMPTY_CELL, 55: EMPTY_CELL, 65: EMPTY_CELL, 75: EMPTY_CELL, 85: EMPTY_CELL,
#               14: EMPTY_CELL, 24: EMPTY_CELL, 34: EMPTY_CELL, 44: EMPTY_CELL, 54: EMPTY_CELL, 64: EMPTY_CELL, 74: EMPTY_CELL, 84: EMPTY_CELL,
#               13: WHITE_CHECKER_CELL, 23: EMPTY_CELL, 33: WHITE_CHECKER_CELL, 43: EMPTY_CELL, 53: WHITE_CHECKER_CELL, 63: EMPTY_CELL, 73: WHITE_CHECKER_CELL, 83: EMPTY_CELL,
#               12: EMPTY_CELL, 22: WHITE_CHECKER_CELL, 32: EMPTY_CELL, 42: WHITE_CHECKER_CELL, 52: EMPTY_CELL, 62: WHITE_CHECKER_CELL, 72: EMPTY_CELL, 82: WHITE_CHECKER_CELL,
#               11: WHITE_CHECKER_CELL, 21: EMPTY_CELL, 31: WHITE_CHECKER_CELL, 41: EMPTY_CELL, 51: WHITE_CHECKER_CELL, 61: EMPTY_CELL, 71: WHITE_CHECKER_CELL, 81:  EMPTY_CELL
# }

BOARD_DICT = {
              18: EMPTY_CELL, 28: EMPTY_CELL, 38: EMPTY_CELL, 48: EMPTY_CELL, 58: EMPTY_CELL, 68: EMPTY_CELL, 78: EMPTY_CELL, 88: EMPTY_CELL,
              17: EMPTY_CELL, 27: EMPTY_CELL, 37: EMPTY_CELL, 47: EMPTY_CELL, 57: WHITE_CHECKER_CELL, 67: EMPTY_CELL, 77: EMPTY_CELL, 87: EMPTY_CELL,
              16: EMPTY_CELL, 26: EMPTY_CELL, 36: EMPTY_CELL, 46: EMPTY_CELL, 56: EMPTY_CELL, 66: EMPTY_CELL, 76: EMPTY_CELL, 86: EMPTY_CELL,
              15: EMPTY_CELL, 25: EMPTY_CELL, 35: EMPTY_CELL, 45: EMPTY_CELL, 55: EMPTY_CELL, 65: EMPTY_CELL, 75: EMPTY_CELL, 85: EMPTY_CELL,
              14: EMPTY_CELL, 24: BLACK_CHECKER_CELL, 34: EMPTY_CELL, 44: EMPTY_CELL, 54: EMPTY_CELL, 64: EMPTY_CELL, 74: EMPTY_CELL, 84: EMPTY_CELL,
              13: WHITE_CHECKER_CELL, 23: EMPTY_CELL, 33: EMPTY_CELL, 43: EMPTY_CELL, 53: EMPTY_CELL, 63: EMPTY_CELL, 73: EMPTY_CELL, 83: EMPTY_CELL,
              12: EMPTY_CELL, 22: EMPTY_CELL, 32: EMPTY_CELL, 42: EMPTY_CELL, 52: EMPTY_CELL, 62: EMPTY_CELL, 72: EMPTY_CELL, 82: EMPTY_CELL,
              11: EMPTY_CELL, 21: EMPTY_CELL, 31: EMPTY_CELL, 41: EMPTY_CELL, 51: EMPTY_CELL, 61: EMPTY_CELL, 71: EMPTY_CELL, 81:  EMPTY_CELL
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
    def __init__(self, board, inp_checker):
        self.board = board
        self.inp_checker = inp_checker
        self.out_stap = ''
        self.eating_checkers = []
        self.staps = []

    def enter_stap(self, staps):
        self.get_stap(input("Enter one of stap (like b4 or b4):"), staps)

    def get_stap(self, str_stap, staps):
        try:
            if len(str_stap) == 2 and not str_stap[0].isdigit() and str_stap[1].isdigit():
                num_stap = str(ord(str_stap[0].lower()) - ord("a") + 1) + str_stap[1]
                if int(num_stap[0]) >= 1 and int(num_stap[0]) <= 8 and int(num_stap[1]) >= 1 and int(num_stap[1]) <= 8 and int(num_stap) in staps:
                    self.out_stap = num_stap
                else:
                    raise NotCorrectCell
            else:
                raise NotCorrectInput
        except NotCorrectCell as ex:
            ex('You chose cell, you can not go into.')
        except NotCorrectInput as ex:
            ex(str_stap)


class BlackChecker(Checker):
    color = 'black'
    def get_checker(self, str_checker):
        super().get_checker(str_checker)
        try:
            if len(str_checker) == 2 and not str_checker[0].isdigit() and str_checker[1].isdigit():
                num_checker = str(ord(str_checker[0].lower()) - ord("a") + 1) + str_checker[1]
                if int(num_checker) in self.board and self.board[int(num_checker)] == BLACK_CHECKER_CELL:
                    self.out_checker = num_checker
                else:
                    raise NotCorrectCell
            else:
                raise NotCorrectInput
        except NotCorrectCell as ex:
            ex('You chose empty cell.')
        except NotCorrectInput as ex:
            ex(str_checker)

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
        for stap in staps:
            if stap in self.board and self.board[stap] == WHITE_CHECKER_CELL and (2*stap - checker) in self.board and self.board[2*stap - checker] == EMPTY_CELL and not stap in self.eating_checkers:
                self.eating_checkers += [stap]
                self.staps += [2*self.eating_checkers[-1] - checker]
                self.can_eat(self.staps[-1])


class WhiteChecker(Checker):
    color = 'white'
    def get_possible_staps(self):
        self.can_eat(int(self.inp_checker))
        if len(self.eating_checkers) != 0:
            return self.staps, self.eating_checkers
        staps = [int(self.inp_checker) + 11, int(self.inp_checker) - 9]
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
        self.board[int(self.inp_checker)] = EMPTY_CELL
        self.board[int(self.out_stap)] = WHITE_CHECKER_CELL

    def can_eat(self, checker):
        staps = [(checker - 11), (checker + 11), (checker - 9), (checker + 9)]
        for stap in staps:
            if stap in self.board and self.board[stap] == BLACK_CHECKER_CELL and (2*stap - checker) in self.board and self.board[2*stap - checker] == EMPTY_CELL and not stap in self.eating_checkers:
                self.eating_checkers += [stap]
                self.staps += [2*self.eating_checkers[-1] - checker]
                self.can_eat(self.staps[-1])


class BlackQueenChecker(BlackChecker):
    pass


class WhiteQueenChecker(WhiteChecker):
    pass

#----------------------------------------------------------------------------------------------------------------------

def enter_checker(iteration, now_board, inp = "Enter the checker, which will go (like A3 or a3):"):
    if iteration % 2 == 0:
        print(Fore.GREEN, 'White go:', Style.RESET_ALL)
    else:
        print(Fore.GREEN, 'Black go:', Style.RESET_ALL)
    checker_cell = input(inp)

    try:
        if len(checker_cell) == 2 and not checker_cell[0].isdigit() and checker_cell[1].isdigit():
            checker_cell = int(str(ord(checker_cell[0].lower()) - ord("a") + 1) + checker_cell[1])
            if checker_cell in now_board:
                return checker_cell
            else:
                raise NotCorrectCell
        else:
            raise NotCorrectInput
    except NotCorrectCell as ex:
        ex('You chose empty cell.')
        return ''
    except NotCorrectInput as ex:
        ex(str(checker_cell))
        return ''

# def get_checker_cycle(checker, inp_checker):
#     check_checker = True
#     while check_checker:
#         enter_checker("Enter the checker, which will go (like A3 or a3):")
#         checker.get_checker(inp_checker)
#         chosen_checker = checker.out_checker
#         if chosen_checker != '':
#             check_checker = False

def create_checker(iteration, now_board, checker_cell):
    if iteration % 2 == 0 and now_board[checker_cell] == WHITE_CHECKER_CELL:
        checker = WhiteChecker(now_board, checker_cell)
    elif iteration % 2 != 0 and now_board[checker_cell] == BLACK_CHECKER_CELL:
        checker = BlackChecker(now_board, checker_cell)
    elif iteration % 2 == 0 and now_board[checker_cell] == WHITE_QUEEN_CHECKER_CELL:
        checker = WhiteQueenChecker(now_board, checker_cell)
    elif iteration % 2 != 0 and now_board[checker_cell] == BLACK_QUEEN_CHECKER_CELL:
        checker = BlackQueenChecker(now_board, checker_cell)
    else:
        ex = NotCorrectCell()
        ex('You chose empty cell.')
        checker = ''
        enter_checker(iteration=iteration, now_board=now_board)
    return checker

# def check_can_eat(iteration, now_board, checker):
#     for cell in now_board:
#         if iteration % 2 == 0 and now_board[cell] == WHITE_CHECKER_CELL:
#             checker.can_eat(cell)
#             if checker.eating_checkers != 0: checker.out_checker = str(cell)
#         elif iteration % 2 != 0 and now_board[cell] == BLACK_CHECKER_CELL:
#             checker.can_eat(cell)
#     return checker.get_possible_staps()

def make_possible_staps_cycle(iteration, checker, board):
    check_possible_staps = True
    while check_possible_staps:
        possible_staps, eating_checkers = checker.get_possible_staps()
        if len(possible_staps) == 0:
            board.show()
            if iteration % 2 == 0:
                print(Fore.GREEN, 'White go:', Style.RESET_ALL)
            else:
                print(Fore.GREEN, 'Black go:', Style.RESET_ALL)
            checker_cell = enter_checker(iteration=iteration, now_board=board, inp = 'You chose checker, which can not go. Try again:')
            check_checker = True
            while check_checker:
                checker = create_checker(iteration, board, checker_cell)
                if checker != '':
                    check_checker = False
            possible_staps, eating_checkers = checker.get_possible_staps()
        else:
            check_possible_staps = False
    return possible_staps, eating_checkers

def possible_board_show(now_board, possible_staps, eating_checkers):
    possible_board = Board(copy.deepcopy(now_board))
    possible_board.make_possible_staps(possible_staps, eating_checkers)
    possible_board.show()
    del possible_board

def enter_stap_cycle(checker, possible_staps):
    check_enter_stap = True
    while check_enter_stap:
        checker.enter_stap(possible_staps)
        chosen_stap = checker.out_stap
        if chosen_stap != '':
            check_enter_stap = False
    checker.make_stap(chosen_stap)

#----------------------------------------------------------------------------------------------------------------------

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
            checker_cell = enter_checker(iteration = iteration, now_board=now_board)
            check_checker = True
            while check_checker:
                checker = create_checker(iteration, now_board, checker_cell)
                if checker != '':
                    check_checker = False

            print()
            print(21 * '-')
            print()
            possible_staps, eating_checkers = make_possible_staps_cycle(iteration, checker, board)

            possible_board_show(now_board, possible_staps, eating_checkers)

            enter_stap_cycle(checker, possible_staps)

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

                else:
                    running = False
                    one_more = False
                    print(Fore.LIGHTCYAN_EX + 'Thanks for game!!! Good luck!!!' + Style.RESET_ALL)

            iteration += 1
            del checker

if __name__ == "__main__":
    main()
    #queen checker, eat if can eat,