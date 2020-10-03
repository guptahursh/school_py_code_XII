from mystack import Stack

class Rstack(Stack):
    def __init__(self,*args,**kwargs):
        super().__init__(self,*args,**kwargs)
        if self.stk:
            self.top = 0

    def __repr__(self):
        S = str(self.stk[self.top:])
        L = str(self.length)
        return "{"+L+"}"+":"+S

    def pop(self):
        try:
            X = self.stk[self.top]
            self.top += 1
            return X
        except:
            print('underflow')
            return None
    
    def push(self,e):
        if self.top == 0:
            print('overflow')
            return None
        self.top -= 1
        self.stk[self.top] = e
        
            






