class Queue():
    def __init__(self):
        self.que = list()

    def __repr__(self):
        return str(self.que)

    def push(self,e):
        self.que.append(e)

    def pop(self):
        return self.que.pop()

    def popItem(self,e):
        return self.que.pop(self.que.index(e))



print("""Type:- *Turn on Caps-Lock for ease of input
        X:\t\t to exit
        1: Insert Element
        2: Search for Element
        3: Change Priority""")


HighestPr = Queue()
NormalPr = Queue()
LowestPr = Queue()


dis = {"H":"Highest_Priority","N":"Normal_Priority","L":"Lowest_Priority"}
disR = { k:v for k,v in zip(dis.values(),dis.keys())}
indx = ["H","N","L"]
Queues = {"H":HighestPr,"N":NormalPr,"L":LowestPr}
while True:
    def insertElement():
        E = input("Enter element : ")
        P = input("Priority [Highest/Normal/Lowest] (H/N/L) : ")
        Queues[P].push(E)
        return 'element added'
        
    def searchForElement(E = None):
        if E is None:
            E = input("Enter element you want to search for : ")

        for name,que in Queues.items():
            if E in que.que:
                return('element has '+dis[name])
        else:
            return('element not found')

    def changePriority():
        E = input("Enter element : ")
        x = searchForElement(E).split()[2] #returns where element present

        if x == 'found':
            return "element not "+x # if not present

        x = disR[x]
        opt = input("Want to Increase/Decrease its priority (I/D) ?: ")
        if opt == 'I':
            if x == 'H':
                return "already at max priority"
            k = indx[indx.index(x)+1]
            Queues[k].push(E)
            return 'priority changed to '+dis[k]
        if opt == 'D':
            if x == 'L':
                return "already at min priority"
            E = Queues[x].popItem(E)
            k = indx[indx.index(x)+1]
            Queues[k].push(E)
            return 'priority changed to '+dis[k]

    x = input("> ")
    L = x.split()
    Options = [insertElement,searchForElement,changePriority]
    try:
        print(Options[int(L[0])-1]())
    except:
        print("~>Err: invalid input")



