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


my_set = Myset()
my_set.add(1)
my_set.add(3)
if my_set.exist(1):
    print("1 exists (A)")
if my_set.exist(2):
    print("2 exists (B)")
my_set.add(2)
if my_set.exist(1):
    print("1 exists (C)")
if my_set.exist(2):
    print("2 exists (D)")
