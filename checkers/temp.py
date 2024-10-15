class T:
    def __init__(self, q):
        self.q = q

    def t(self):
        print('T', type(self))


class TT(T):
    def t(self):
        print('TT', type(self))


if __name__ == '__main__':
    t = T(4)
    t = TT(5)
    print(t.q)

