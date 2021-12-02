a = input("Masukan nama : ")
b = input("Masukan nomor kursi "+a+" : ")
aa = []
bb = []
while a != "STOP":
    if b not in aa:
        aa.append(b)
        bb.append(a)
    else:
        print("Mohon maaf kursi tersebut telah terisi!")
    a = input("Masukan nama : ")
print("List kursi yang telah terisi : ")
for i in range (len(aa)):
    print("Kursi nomor %s telah diisi oleh %s" % (aa[i],bb[i]))