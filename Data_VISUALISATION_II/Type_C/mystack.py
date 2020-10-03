class Stack:
    def __init__(self,*args,**kwargs):
        self.stk = []
        self.top = -1
        for i in args:
            self.stk.append(i)
            self.top += 1
        if 'LEN' in kwargs:
            d = kwargs['LEN'] - len(self.stk)
            self.stk += [None for _ in range(d)]
        self.length = len(self.stk)

    def __iter__(self):
        self.index = -1
        return self

    def __next__(self):
        self.index += 1
        if self.index <= self.top:
            return self.stk[self.index]
        raise StopIteration

    def __repr__(self):
        S = str(self.stk[:self.top + 1])
        L = str(self.length)
        return "{"+L+"}"+":"+S

    def pop(self):
        if self.top == -1:
            print('underflow')
            return None
        X = self.stk[self.top]
        self.top -= 1
        return X

    def push(self,e):
        try:
            self.top += 1
            self.stk[self.top] = e
        except:
            print('overflow')

