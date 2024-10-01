from colorama import Back, Style, Fore, init

ERR_NOT_EMPTY = 'You chose empty cell.'


class NotCorrectInput(Exception):
    def __call__(self, inp):
        print(Fore.RED + "Your input is not correct. Your input is " + inp + " You input should be like a3 or A3. Try again." + Style.RESET_ALL)



class NotCorrectCell(Exception):
    def __call__(self, err):
        print(Fore.RED + "You enter not correct cell. " + err + " Try again." + Style.RESET_ALL)

