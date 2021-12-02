a = (input("Input : "))
b = 2 * len(a)-2
c =''
print("Output: ")
for aa in range (0, len(a)-1):
    for bb in range (0, b):
        print('', end ='')
    b -= 2
    for bb in range (0, aa + 1):
        print(f'{a[bb]}', end= '')
    print ('')
b = -1
for aa in range (len(a)-1, -1,-1):
    for bb in range (b, -1, -1):
        print('', end = '')
    b += 2
    for bb in range (0, aa + 1):
        print(f'{a[bb]}', end='')

    print ('')