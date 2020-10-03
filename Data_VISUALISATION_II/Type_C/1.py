from mystack import Stack

x = int(input('enter size of stack:'))
S = Stack(LEN=x)

print("""Type:- *Turn on Caps-Lock for ease of input
        X:\t\t to exit
        PSH <element>:\t to push <element>
        POP:\t\t to pop
        DIS:\t\t to display the stack""")

while True:
    x = input('>').lstrip().rstrip()
    if x == 'X':
        break
    elif "PSH" in x:
        try:
            S.push(x.split()[1])
        except:
            print('~>Err: <element> required')
    elif "POP" in x:
        print(S.pop())
    elif "DIS" in x:
        print(S)
    else:
        print('~>Err: Unknown Command')

