from colorama import Back, Style, Fore, init

class NotCorrectInput(Exception):
    def __init__(self, checker):
        self.checker = checker

    def __call__(self, enter_def, *args, **kwargs):
        print(Fore.RED + "Your input is not correct. Try again." + Style.RESET_ALL)
        self.checker.out_stap = ''
        self.checker.enter_def()


class NotCorrectCell(Exception):
    def __init__(self, checker):
        self.checker = checker

    def __call__(self, enter_def, *args, **kwargs):
        print(Fore.RED + "You enter not correct cell. Try again." + Style.RESET_ALL)
        self.checker.out_stap = ''
        self.checker.enter_def()
