x = input('enter the expression:') # the expression with
                                   # or without spaces
def convert(x):
    S = ''
    for i in range(len(x)-1):
        # if i is num and i + 1 is num: S += i
        if x[i].isalnum() and x[i + 1].isalnum():
                S += x[i]
        else:
        # if i is not num S += i + ' '
        # if i is num but i + 1 not num : S += i + ' '
                S += x[i] + ' '
    S += x[len(x)-1]
    return S.split()

print(convert(x))


