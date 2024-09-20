import copy
from colorama import Back, Style, Fore, init


BOARD_DICT = {
              1: "", 2: "b", 3: "", 4: "b", 5: "", 6: "b", 7: "", 8: "b",
              9: "b", 10: "", 11: "b", 12: "", 13: "b", 14: "", 15: "b", 16: "",
              17: "", 18: "b", 19: "", 20: "b", 21: "", 22: "b", 23: "", 24: "b",
              25: "", 26: "", 27: "", 28: "", 29: "", 30: "", 31: "", 32: "",
              33: "", 34: "", 35: "", 36: "", 37: "", 38: "", 39: "", 40: "",
              41: "w", 42: "", 43: "w", 44: "", 45: "w", 46: "", 47: "w", 48: "",
              49: "", 50: "w", 51: "", 52: "w", 53: "", 54: "w", 55: "", 56: "w",
              57: "w", 58: "", 59: "w", 60: "", 61: "w", 62: "", 63: "w", 64: ""
}


class Board:

    def __init__(self):
        pass

    def show(self, board):
        for i in range(4):
            print(Back.WHITE + Back.LIGHTBLACK_EX + Back.WHITE + Back.LIGHTBLACK_EX + Back.WHITE + Back.LIGHTBLACK_EX + Back.WHITE + Back.LIGHTBLACK_EX)
            print(Back.LIGHTBLACK_EX + Back.WHITE + Back.LIGHTBLACK_EX + Back.WHITE + Back.LIGHTBLACK_EX + Back.WHITE + Back.LIGHTBLACK_EX + Back.WHITE)




class Checker:
    pass


class QueenChecker(Checker):
    pass


if __name__ == "__main__":
    init()
    board = Board()
    board.show(BOARD_DICT)