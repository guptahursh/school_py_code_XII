from myqueue import Queue

print('Input Format: a b c d e f g ... (elements seperated with spaces)')
E = list(map(int,input('Enter Queue:')))

print("""Type:- *Turn on Caps-Lock for ease of input
        X:\t\t to exit
        PSH <element>:\t to push <element>
        POP:\t\t to pop
        DIS:\t\t to display the queue""")
Q = Queue(*E)
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

