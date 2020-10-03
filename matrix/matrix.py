class Matrix:
    def __init__(self):
        self.enter_values()
    
    def __repr__(self):
        S = "matrix(\n"
        for r in self.value:
           S += str(r)+'\n'
        S += ")"
        return S
    
    def __mul__(self):
        pass

    def enter_values(self):
        self.value = []
        while True:
            x = list(map(int,input().rstrip().split()))
            if not self.value:
                self.c = len(x)
            if not x:
                self.r = len(self.value)
                break
            else:
                self.value.append(x[:self.c])

assert hasattr(Matrix,'enter_values') # this is a cool piece of code
