class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.siz = [1] * n

    def root(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.root(self.par[x])
        return self.par[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return
        if self.siz[x] > self.siz[y]:
            self.par[y] = x
            self.siz[x] += self.siz[y]
        else:
            self.par[x] = y
            self.siz[y] += self.siz[x]

    def is_same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return self.siz[self.root(x)]
