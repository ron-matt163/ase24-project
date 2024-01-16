class Sym:
    def __init__(self, s, n):
        self.txt = s or " "
        self.at = n or 0
        self.n = 0
        self.has = {}
        self.mode = None
        self.most = 0

    def add(self, x):
        if (x != "?"):
            self.n = self.n + 1
            self.has[x] = 1 + (self.has[x] or 0)
            if (self.has[x] > self.most):
                self.most, self.mode = self.has[x], x

    def mid(self):
        return self.mode
