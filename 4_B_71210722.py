a = int(input("Input : "))
print("Output : ")
for i in range(1,a+1):
    for j in range(1,a+1):
        if i==a or i+j==a+1 or j-i==a-i:
            print("*",end=" ")
        else:
            print(end="  ")
    print()