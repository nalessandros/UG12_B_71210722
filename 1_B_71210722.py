a = int(input("Masukan banyak bilangan : "))
b = 0
c = ""
count = 0
while count <int(a):
    count = count+1
    n = count
    if count%7==0:
        n = 0
    elif count%3==0:
        n = count*-1
    if n>1 or n==0:
        c +=" + " + str(n)
    else:
        c += " " + str(n)
    b = b + n
print("Total =",c)
print("Hasil perhitungan diatas ialah",b)