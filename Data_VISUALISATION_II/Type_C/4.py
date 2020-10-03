from myqueue import Queue
# unlimited Queue

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


print("""Type:- *Turn on Caps-Lock for ease of input
        X:\t\t to exit
        PSH <element>:\t to push <element>
        POP:\t\t to pop
        DIS:\t\t to display the queue""")

Q = Uqueue()
while True:
    x = input('>').lstrip().rstrip()
    if x == 'X':
        break
    elif "PSH" in x:
        try:
            print("len:",Q.length)
            Q.push(x.split()[1])
        except Exception as e:
            print(e)
            print('~>Err: <element> required')
    elif "POP" in x:
        print(Q.pop())
    elif "DIS" in x:
        print(Q)
    else:
        print('~>Err: Unknown Command')

