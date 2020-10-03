from mystack import Stack

S = Stack(LEN = int(input('Enter length of Stack:'))) 
print("""Type:- *Turn on Caps-Lock for ease of input
        X:\t\t to exit
        PSH <pin> <name>:to push the node to the stack
        POP:\t\t to pop
        DIS:\t\t to display the stack""")

while True:
    x = input('>').lstrip().rstrip()
    if x == 'X':
        break
    elif "PSH" in x:
        try:
            l = x.split()
            S.push((int(l[1]),l[2]))
        except Exception as e:
            print('~>Err: <node> required')
    elif "POP" in x:
        print(S.pop())
    elif "DIS" in x:
        print(S)
    else:
        print('~>Err: Unknown Command')



