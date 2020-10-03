from mystack import Stack
x = input('enter the string:').split()

S = Stack(LEN = len(x))
for i in x:
    S.push(i*2)

out = ''
# print(S)
while S.top != -1:
    out += S.pop() + ' '
print(out)
    


