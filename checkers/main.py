import copy
from colorama import Back, Style, Fore, init
from Exceptions import NotCorrectCell, NotCorrectInput, NotCorrectInputIsWin, NotCorrectInputChecker

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

# BOARD_DICT = {
#               18: EMPTY_CELL, 28: EMPTY_CELL, 38: EMPTY_CELL, 48: EMPTY_CELL, 58: EMPTY_CELL, 68: EMPTY_CELL, 78: EMPTY_CELL, 88: EMPTY_CELL,
#               17: EMPTY_CELL, 27: EMPTY_CELL, 37: EMPTY_CELL, 47: EMPTY_CELL, 57: EMPTY_CELL, 67: EMPTY_CELL, 77: EMPTY_CELL, 87: EMPTY_CELL,
#               16: EMPTY_CELL, 26: EMPTY_CELL, 36: EMPTY_CELL, 46: EMPTY_CELL, 56: EMPTY_CELL, 66: EMPTY_CELL, 76: EMPTY_CELL, 86: EMPTY_CELL,
#               15: EMPTY_CELL, 25: EMPTY_CELL, 35: EMPTY_CELL, 45: EMPTY_CELL, 55: EMPTY_CELL, 65: EMPTY_CELL, 75: EMPTY_CELL, 85: EMPTY_CELL,
#               14: EMPTY_CELL, 24: EMPTY_CELL, 34: EMPTY_CELL, 44: EMPTY_CELL, 54: EMPTY_CELL, 64: EMPTY_CELL, 74: EMPTY_CELL, 84: EMPTY_CELL,
#               13: EMPTY_CELL, 23: EMPTY_CELL, 33: EMPTY_CELL, 43: EMPTY_CELL, 53: EMPTY_CELL, 63: EMPTY_CELL, 73: EMPTY_CELL, 83: EMPTY_CELL,
#               12: EMPTY_CELL, 22: EMPTY_CELL, 32: EMPTY_CELL, 42: EMPTY_CELL, 52: EMPTY_CELL, 62: EMPTY_CELL, 72: EMPTY_CELL, 82: EMPTY_CELL,
#               11: EMPTY_CELL, 21: EMPTY_CELL, 31: EMPTY_CELL, 41: EMPTY_CELL, 51: EMPTY_CELL, 61: EMPTY_CELL, 71: EMPTY_CELL, 81:  EMPTY_CELL
# }

BOARD_DICT = {
              18: EMPTY_CELL, 28: BLACK_CHECKER_CELL, 38: EMPTY_CELL, 48: BLACK_CHECKER_CELL, 58: EMPTY_CELL, 68: BLACK_CHECKER_CELL, 78: EMPTY_CELL, 88: BLACK_CHECKER_CELL,
              17: BLACK_CHECKER_CELL, 27: EMPTY_CELL, 37: BLACK_CHECKER_CELL, 47: EMPTY_CELL, 57: BLACK_CHECKER_CELL, 67: EMPTY_CELL, 77: BLACK_CHECKER_CELL, 87: EMPTY_CELL,
              16: EMPTY_CELL, 26: EMPTY_CELL, 36: EMPTY_CELL, 46: EMPTY_CELL, 56: EMPTY_CELL, 66: BLACK_CHECKER_CELL, 76: EMPTY_CELL, 86: BLACK_CHECKER_CELL,
              15: EMPTY_CELL, 25: EMPTY_CELL, 35: BLACK_CHECKER_CELL, 45: EMPTY_CELL, 55: EMPTY_CELL, 65: EMPTY_CELL, 75: EMPTY_CELL, 85: EMPTY_CELL,
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

BORDERS = [
           18, 28, 38, 48, 58, 68, 78, 88,
           17, 27, 37, 47, 57, 67, 77, 87,
           16, 26, 36, 46, 56, 66, 76, 86,
           15, 25, 35, 45, 55, 65, 75, 85,
           14, 24, 34, 44, 54, 64, 74, 84,
           13, 23, 33, 43, 53, 63, 73, 83,
           12, 22, 32, 42, 52, 62, 72, 82,
           11, 21, 31, 41, 51, 61, 71, 81,
           ]

TERMS = [11, -11, 9, -9]

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

    def make_possible_staps(self, stap_and_eating_checker_dict):
        for stap, eating_checker in stap_and_eating_checker_dict.items():
            self.board[stap] = POSSIBLE_CELL
            if eating_checker != 0:
                self.board[eating_checker] = EATING_CHECKER_CELL

    def is_win(self):
        count = [0, 0] # count[0] - white, count[1] - black
        for checker in self.board:
            if self.board[checker] == WHITE_CHECKER_CELL or self.board[checker] == WHITE_QUEEN_CHECKER_CELL:
                count[0] += 1
            elif self.board[checker] == BLACK_CHECKER_CELL or self.board[checker] == BLACK_QUEEN_CHECKER_CELL:
                count[1] += 1
        if count[0] == 0:
            return BLACK_WIN
        elif count[1] == 0:
            return WHITE_WIN
        else:
            return 0

#----------------------------------------------------------------------------------------------------------------------

class Checker:
    def __init__(self, int_checker, board):
        self.int_checker = int_checker
        self.board = board
        self.return_staps_and_checkers_dict = {}
        self.POSSIBLE_EATING_CHECKERS_LIST = []
        self.QUEEN_CONDITION = []

    def check_can_eat(self, checker):
        staps = [(checker + TERMS[0]), (checker + TERMS[1]), (checker + TERMS[2]), (checker + TERMS[3])]
        for stap in staps:
            if stap in self.board and self.board[stap] in self.POSSIBLE_EATING_CHECKERS_LIST and (2 * stap - checker) in self.board and self.board[2 * stap - checker] == EMPTY_CELL:
                self.return_staps_and_checkers_dict[2*stap - checker] = stap # {stap: eating_checker}

    def get_possible_staps(self):
        self.check_can_eat(self.int_checker)

    def make_stap(self, stap):
        if len(self.return_staps_and_checkers_dict) != 0:
            self.board[self.return_staps_and_checkers_dict[stap]] = EMPTY_CELL
        self.board[self.int_checker] = EMPTY_CELL
        self.return_staps_and_checkers_dict = {}

    def check_can_be_queen(self, stap):
        if stap in self.QUEEN_CONDITION:
            return stap
        return 0


class WhiteChecker(Checker):
    def __init__(self, int_checker, board):
            super().__init__(int_checker, board)
            self.POSSIBLE_EATING_CHECKERS_LIST = [BLACK_CHECKER_CELL, BLACK_QUEEN_CHECKER_CELL]
            self.OUR_CHECKERS_LIST = [WHITE_CHECKER_CELL, WHITE_QUEEN_CHECKER_CELL]
            self.QUEEN_CONDITION = BORDERS[:8]

    def get_possible_staps(self):
        super().get_possible_staps()
        if len(self.return_staps_and_checkers_dict) != 0:
            return self.return_staps_and_checkers_dict
        staps = [self.int_checker + TERMS[0], self.int_checker + TERMS[3]]
        for stap_index, stap in enumerate(staps):
            if not stap in self.board or not self.board[stap] == EMPTY_CELL:
                staps[stap_index] = 0
        staps = [stap for stap in staps if stap != 0]
        self.return_staps_and_checkers_dict = {k:0 for k in staps}
        return self.return_staps_and_checkers_dict

    def make_stap(self, stap):
        super().make_stap(stap)
        ques_queen = self.check_can_be_queen(stap)
        if ques_queen != 0:
            self.board[stap] = WHITE_QUEEN_CHECKER_CELL
        else:
            self.board[stap] = WHITE_CHECKER_CELL


class BlackChecker(Checker):
    def __init__(self, int_checker, board):
        super().__init__(int_checker, board)
        self.POSSIBLE_EATING_CHECKERS_LIST = [WHITE_CHECKER_CELL, WHITE_QUEEN_CHECKER_CELL]
        self.OUR_CHECKERS_LIST = [BLACK_CHECKER_CELL, BLACK_QUEEN_CHECKER_CELL]
        self.QUEEN_CONDITION = BORDERS[-8:]

    def get_possible_staps(self):
        super().get_possible_staps()
        if len(self.return_staps_and_checkers_dict) != 0:
            return self.return_staps_and_checkers_dict
        staps = [self.int_checker + TERMS[1], self.int_checker + TERMS[2]]
        for stap_index, stap in enumerate(staps):
            if not stap in self.board or not self.board[stap] == EMPTY_CELL:
                staps[stap_index] = 0
        staps = [stap for stap in staps if stap != 0]
        self.return_staps_and_checkers_dict = {k: 0 for k in staps}
        return self.return_staps_and_checkers_dict

    def make_stap(self, stap):
        super().make_stap(stap)
        ques_queen = self.check_can_be_queen(stap)
        if ques_queen != 0:
            self.board[stap] = BLACK_QUEEN_CHECKER_CELL
        else:
            self.board[stap] = BLACK_CHECKER_CELL


# ----------------------------------------------------------------------------------------------------------------------

class QueenChecker(Checker):
    def __init__(self, int_checker, board):
        super().__init__(int_checker, board)
        self.all_staps_list = []

    def make_stap_list(self, checker):
        for term in TERMS:
            stap = checker + term
            one_way_staps = []
            while stap in BORDERS:
                one_way_staps.append(stap)
                stap += term
            self.all_staps_list.append(one_way_staps)

    def check_can_eat(self, checker):
        self.make_stap_list(checker)
        for one_way_staps in self.all_staps_list:
            for stap in one_way_staps:
                if self.board[stap] in self.POSSIBLE_EATING_CHECKERS_LIST and (2 * stap - checker) in self.board and self.board[2 * stap - checker] == EMPTY_CELL:
                    self.return_staps_and_checkers_dict.update({i: stap for i in one_way_staps[one_way_staps.index(stap)+1:]})# [2*stap - checker] = stap # {stap: eating_checker}


    def get_possible_staps(self):
        super().get_possible_staps()
        if len(self.return_staps_and_checkers_dict) != 0:
            return self.return_staps_and_checkers_dict
        temp_staps = []
        for one_way_staps in self.all_staps_list:
            for stap in one_way_staps:
                if self.board[stap] == EMPTY_CELL:
                    temp_staps.append(stap)
                else:
                    break
        self.return_staps_and_checkers_dict = {k: 0 for k in temp_staps}
        return self.return_staps_and_checkers_dict
        

class WhiteQueenChecker(QueenChecker):
    def __init__(self, int_checker, board):
        super().__init__(int_checker, board)
        self.POSSIBLE_EATING_CHECKERS_LIST = [BLACK_CHECKER_CELL, BLACK_QUEEN_CHECKER_CELL]

    def make_stap(self, stap):
        super().make_stap(stap)
        self.board[stap] = WHITE_QUEEN_CHECKER_CELL
        self.return_staps_and_checkers_dict = {}


class BlackQueenChecker(QueenChecker):
    def __init__(self, int_checker, board):
        super().__init__(int_checker, board)
        self.POSSIBLE_EATING_CHECKERS_LIST = [BLACK_CHECKER_CELL, BLACK_QUEEN_CHECKER_CELL]

    def make_stap(self, stap):
        super().make_stap(stap)
        self.board[stap] = WHITE_QUEEN_CHECKER_CELL
        self.return_staps_and_checkers_dict = {}

# ----------------------------------------------------------------------------------------------------------------------

class Game:
    def __init__(self):
        self.one_more = True
        self.running = True
        self.iteration = 2
        self.possible_staps_and_eating_checkers_for_all_checkers_dict = {}

    def check_inp_checker(self, board):
        inp_str_checker = input("Enter the checker, which will go (like A3 or a3): ")
        out_int_checker = 0
        try:
            if len(inp_str_checker) == 2 and not inp_str_checker[0].isdigit() and inp_str_checker[1].isdigit():
                out_int_checker = int(str(ord(inp_str_checker[0].lower()) - ord("a") + 1) + inp_str_checker[1])
                if not out_int_checker in board or board[out_int_checker] == EMPTY_CELL:
                    raise NotCorrectCell
                if len(self.possible_staps_and_eating_checkers_for_all_checkers_dict) != 0 and not out_int_checker in self.possible_staps_and_eating_checkers_for_all_checkers_dict:
                    raise NotCorrectInputChecker
            else:
                raise NotCorrectInput
        except NotCorrectCell as ex:
            ex(inp=out_int_checker, err='You chose empty cell.')
            out_int_checker = self.check_inp_checker(board)
        except NotCorrectInput as ex:
            ex(inp_str_checker)
            out_int_checker = self.check_inp_checker(board)
        except NotCorrectInputChecker as ex:
            ex()
            out_int_checker = self.check_inp_checker(board)
        finally:
            return out_int_checker

    def create_checker(self, out_checker, board):
        checker = 0
        try:
            if self.iteration % 2 == 0:
                if board[out_checker] == WHITE_CHECKER_CELL:
                    checker = WhiteChecker(out_checker, board)
                elif board[out_checker] == WHITE_QUEEN_CHECKER_CELL:
                    checker = WhiteQueenChecker(out_checker, board)
                else:
                    raise NotCorrectCell
            elif self.iteration % 2 != 0:
                if board[out_checker] == BLACK_CHECKER_CELL:
                    checker = BlackChecker(out_checker, board)
                elif board[out_checker] == BLACK_QUEEN_CHECKER_CELL:
                    checker = BlackQueenChecker(out_checker, board)
                else:
                    raise NotCorrectCell
        except NotCorrectCell as ex:
            ex(inp=out_checker, err='You chose checker other color.')
            new_out_int_checker = self.check_inp_checker(board )
            checker = self.create_checker(new_out_int_checker, board)
        finally:
            return checker

    def check_possible_staps(self, checker, board):
        possible_staps_and_eating_checkers_dict = {}
        try:
            possible_staps_and_eating_checkers_dict = checker.get_possible_staps()
            if len(possible_staps_and_eating_checkers_dict) == 0:
                raise NotCorrectCell
        except NotCorrectCell as ex:
            ex(checker.int_checker, 'You chose checker, which can not go.')
            new_out_int_checker = self.check_inp_checker(board)
            new_checker = self.create_checker(new_out_int_checker, board)
            possible_staps_and_eating_checkers_dict= self.check_possible_staps(new_checker, board)
        finally:
            return possible_staps_and_eating_checkers_dict

    def check_inp_stap(self, staps):
        inp_str_stap = input('Enter the stap (like B4 or b4): ')
        out_int_stap = 0
        try:
            if len(inp_str_stap) == 2 and not inp_str_stap[0].isdigit() and inp_str_stap[1].isdigit():
                out_int_stap = int(str(ord(inp_str_stap[0].lower()) - ord("a") + 1) + inp_str_stap[1])
                if not out_int_stap in staps:
                    raise NotCorrectCell
            else:
                raise NotCorrectInput
        except NotCorrectCell as ex:
            ex(inp=out_int_stap, err='You do not chose one of stap.')
            out_int_stap = self.check_inp_stap(staps)
        except NotCorrectInput as ex:
            ex(inp_str_stap)
            out_int_stap = self.check_inp_stap(staps)
        finally:
            return out_int_stap

    def check_enter_chose_win_game(self):
        running = True
        one_more = True
        continue_game = input('Would you like to play one more game?!(Y/n):')
        try:
            if continue_game.lower() == 'y':
                running = False
                one_more = True
            elif continue_game.lower() == 'n':
                running = False
                one_more = False
                print(Fore.LIGHTCYAN_EX + 'Thanks for game!!! Good luck!!!' + Style.RESET_ALL)
            else:
                raise NotCorrectInputIsWin
        except NotCorrectInputIsWin as ex:
            ex(continue_game)
            self.check_enter_chose_win_game()
        finally:
            return running, one_more

    def who_go(self):
        if self.iteration % 2 == 0:
            print(Fore.GREEN, 'White go:', Style.RESET_ALL)
        else:
            print(Fore.GREEN, 'Black go:', Style.RESET_ALL)

    def check_possible_board_and_make_stap(self, checker, now_board):
        possible_staps_and_eating_checkers_dict = self.check_possible_staps(checker, now_board.return_board())
        possible_board = Board(copy.deepcopy(now_board.return_board()))
        possible_board.make_possible_staps(possible_staps_and_eating_checkers_dict)
        possible_board.show()
        del possible_board
        temp_checker = 0
        stap = self.check_inp_stap(possible_staps_and_eating_checkers_dict)
        checker.make_stap(stap)
        print(checker.return_staps_and_checkers_dict, checker)
        if len(checker.return_staps_and_checkers_dict) != 0:
            checker.check_can_eat(stap)
            if len(checker.return_staps_and_checkers_dict) != 0:
                if type(checker) == WhiteChecker:
                    temp_checker = WhiteChecker(stap, now_board.return_board())
                elif type(checker) == BlackChecker:
                    temp_checker = BlackChecker(stap, now_board.return_board())
                elif type(checker) == WhiteQueenChecker or (stap in BORDERS[:8] and type(checker) == WhiteChecker):
                    temp_checker = WhiteQueenChecker(stap, now_board.return_board())
                elif type(checker) == BlackQueenChecker or (stap in BORDERS[-8:] and type(checker) == BlackChecker):
                    temp_checker = BlackQueenChecker(stap, now_board.return_board())
                del checker
                self.check_possible_board_and_make_stap(temp_checker, now_board)

    def check_can_eat_for_all_checkers(self, now_board):
        possible_staps_and_eating_checkers_for_all_checkers_dict = {} # {checker: {return_staps_and_checkers_dict}}
        for cell in now_board:
            if self.iteration % 2 == 0:
                if now_board[cell] == WHITE_CHECKER_CELL:
                    temp_checker = WhiteChecker(cell, now_board)
                    temp_checker.check_can_eat(cell)
                    if len(temp_checker.return_staps_and_checkers_dict) != 0:
                        possible_staps_and_eating_checkers_for_all_checkers_dict[cell] = temp_checker.return_staps_and_checkers_dict
                    del temp_checker
                elif now_board[cell] == WHITE_QUEEN_CHECKER_CELL:
                    temp_checker = WhiteQueenChecker(cell, now_board)
                    temp_checker.check_can_eat(cell)
                    if len(temp_checker.return_staps_and_checkers_dict) != 0:
                        possible_staps_and_eating_checkers_for_all_checkers_dict[cell] = temp_checker.return_staps_and_checkers_dict
                    del temp_checker
            elif self.iteration % 2 != 0:
                if now_board[cell] == BLACK_CHECKER_CELL:
                    temp_checker = BlackChecker(cell, now_board)
                    temp_checker.check_can_eat(cell)
                    if len(temp_checker.return_staps_and_checkers_dict) != 0:
                        possible_staps_and_eating_checkers_for_all_checkers_dict[cell] = temp_checker.return_staps_and_checkers_dict
                    del temp_checker
                elif now_board[cell] == BLACK_QUEEN_CHECKER_CELL:
                    temp_checker = BlackQueenChecker(cell, now_board)
                    temp_checker.check_can_eat(cell)
                    if len(temp_checker.return_staps_and_checkers_dict) != 0:
                        possible_staps_and_eating_checkers_for_all_checkers_dict[cell] = temp_checker.return_staps_and_checkers_dict
                    del temp_checker
        return possible_staps_and_eating_checkers_for_all_checkers_dict

    def show_possible_staps_for_all_checkers(self, now_board):
        temp_now_board = copy.deepcopy(now_board)
        self.possible_staps_and_eating_checkers_for_all_checkers_dict = self.check_can_eat_for_all_checkers(temp_now_board.return_board())
        if len(self.possible_staps_and_eating_checkers_for_all_checkers_dict) == 0:
            return now_board
        else:
            for ch in self.possible_staps_and_eating_checkers_for_all_checkers_dict:
                temp_now_board.make_possible_staps(self.possible_staps_and_eating_checkers_for_all_checkers_dict[ch])
            return temp_now_board

    def run(self):
        while self.one_more:
            board = copy.deepcopy(BOARD_DICT)
            self.iteration = 2  # iteration%2 == 0 go white, iteration%2 != 0 - go black
            while self.running:
                now_board = Board(board)
                self.show_possible_staps_for_all_checkers(now_board).show()
                self.who_go()
                out_int_checker = self.check_inp_checker(now_board.return_board())
                checker = self.create_checker(out_int_checker, now_board.return_board())
                self.check_possible_board_and_make_stap(checker, now_board)
                iw = now_board.is_win()
                if iw != 0:
                    now_board.show()
                    print(iw)
                    self.running, self.one_more = self.check_enter_chose_win_game()
                self.iteration += 1
                del checker

# ----------------------------------------------------------------------------------------------------------------------

def main():
    init()
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
