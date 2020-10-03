from myqueue import Queue
# not a circular queue, memory limitations apply
class IRdequeue(Queue):
    def Lpop(self):
        return Queue.pop(self)
        
    def __makeValid(self):
        if self.front > self.rear:
            self.front = self.rear = -1
        elif self.front == -1 and self.rear != -1:
            self.front = 0

    def Rpop(self):
        if self.rear == -1:
            print('underflow')
            return None
        X = self.que[self.rear]
        self.rear -= 1
        self.__makeValid()
        return X

Q = IRdequeue(LEN = int(input('Enter length of dequeue:'))) 
print("""Type:- *Turn on Caps-Lock for ease of input
        X:\t\t to exit
        PSH <pin> <name>:to push to queue
        POP L:\t\t to pop the to the Left of the queue
        POP R:\t\t to pop the to the Right of the queue
        DIS:\t\t to display the queue""")

while True:
    x = input('>').lstrip().rstrip()
    l = x.split()
    if x == 'X':
        break
    elif "PSH" in x:
        try:
            Q.push(l[1])
        except:
            print('~>Err: parameter expected')
    elif "POP" in x:
        if l[1] == 'R':
            print(Q.Rpop())
        if l[1] == 'L':
            print(Q.Lpop())
    elif "DIS" in x:
        print(Q)
    else:
        print('~>Err: Unknown Command')


        
        
        
