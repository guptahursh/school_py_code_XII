# 1 2 3 4 5 6 7
# R           F
class Queue:

    def __init__(self,*args,**kwargs):
        self.que = []
        self.front = -1
        self.rear = -1
        for i in args:
            self.que.append(i)
            self.rear += 1
        if self.rear != -1:
            self.front = 0
        if 'LEN' in kwargs:
            d = kwargs['LEN'] - len(self.que)
            self.que += [None for _ in range(d)]
        self.length = len(self.que)
    
    def __repr__(self):
        Q = str(self.que[self.front:self.rear +1])
        L = str(self.length)
        return "{"+L+"}"+":"+Q

    def __iter__(self):
        self.index = self.front
        return self
    def hello(self):
        print('hello')

    def __next__(self):
        self.index += 1
        if self.index <= self.rear:
            return self.stk[self.index]
        raise StopIteration

    def __makeValid(self):
        if self.front > self.rear:
            self.front = self.rear = -1
        elif self.front == -1 and self.rear != -1:
            self.front = 0

    def pop(self):
        if self.front == -1:
            print('underflow')
            return None
        X = self.que[self.front]
        self.front += 1
        self.__makeValid()
        return X

    def push(self,e):
        if self.rear >= self.length -1:
            print('overflow')
            return None
        self.rear += 1
        self.que[self.rear] = e
        self.__makeValid()

class Uqueue(Queue):
    def __init__(self,*args,**kwargs):
        self.rear = -1
        self.que = []
        self.front = -1
        self.length = -1

    def makeValid(self):
        if self.front > self.rear:
            self.front = self.rear = -1
        elif self.front == -1 and self.rear != -1:
            self.front = 0

    def push(self,e):
        if self.rear >= self.length:
            if self.que == []:
                self.que = [0]
            self.que.append(None)
            self.length += 1
        self.rear += 1
        self.que[self.rear] = e
        self.makeValid()


    
