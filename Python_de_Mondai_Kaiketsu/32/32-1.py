class Myset:
    def __init__(self):
        self.set = []

    def add(self, x):
        if self.exist(x):
            return
        self.set.append(x)

    def exist(self, x):
        for s in self.set:
            if s == x:
                return True
        return False
