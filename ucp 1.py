def panjang_():
    p = int(input("masukkan panjang : "))
    t = int(input("masukkan tinggi : "))
    L = 0.5 * p * t
    if p < 1:
        print("Salah")

    else:
        print("yap : ", L)
panjang_()


def Lsegitiga(panjang=1, tinggi =1):
    p = int(input("masukkan panjang : "))
    t = int(input("masukkan tinggi : "))
    L = 0.5 * p * t
    if panjang <= 0 or tinggi <= 0:
        print("Nda bisaaa sayang")
        return
    else:
        print("Luas adalah : ", L)
Lsegitiga()