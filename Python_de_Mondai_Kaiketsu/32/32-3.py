class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]

    def root(self, x):
        if self.par[x] == x:
            return x
        return self.root(self.par[x])

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        self.par[y] = x

    def is_same(self, x, y):
        return self.root(x) == self.root(y)
