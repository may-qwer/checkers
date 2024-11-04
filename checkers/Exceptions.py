from colorama import Style, Fore

TUPLE_IN_BOARD_QUES = (18, 28, 38, 48, 58, 68, 78, 88,
                      17, 27, 37, 47, 57, 67, 77, 87,
                      16, 26, 36, 46, 56, 66, 76, 86,
                      15, 25, 35, 45, 55, 65, 75, 85,
                      14, 24, 34, 44, 54, 64, 74, 84,
                      13, 23, 33, 43, 53, 63, 73, 83,
                      12, 22, 32, 42, 52, 62, 72, 82,
                      11, 21, 31, 41, 51, 61, 71, 81)


class NotCorrectInput(Exception):
    def __call__(self, inp):
        print(Fore.RED + "Your input is not correct. Your input is " + inp + " You input should be like a3 or A3. Try again." + Style.RESET_ALL)



class NotCorrectCell(Exception):
    def __call__(self, inp, err = 'You chose empty cell.'): # err == EMPTY, OTHER_COLOR
        if not inp in TUPLE_IN_BOARD_QUES:
            err = 'You chose cell, that is outside the board.'
        print(Fore.RED + "You enter not correct cell. " + err + " Try again." + Style.RESET_ALL)


class NotCorrectInputIsWin(Exception):
    def __call__(self, inp):
        print(Fore.LIGHTRED_EX + 'Your input is not correct. Your input is ' + inp + 'Enter "Y" or "y", if you want to start over, or enter "N" or "n", if you want to finish playing.' + Style.RESET_ALL)

class NotCorrectInputChecker(Exception):
    def __call__(self):
        print(Fore.LIGHTRED_EX + 'Your input is not correct. There are checkers which can eat. Chose one.' + Style.RESET_ALL)
