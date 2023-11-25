#1 bilangan_terbesar_2bilangan
a = int(input("Masukkan angka pertama   : "))
b = int(input("Masukkan angka kedua     : "))
if a>b:
    print ("angka pertama (",a,")lebih besar dari angka kedua (",b,")")
elif b>a:
    print ("angka kedua (",b,") lebih besar dari angka pertama (",a,")")
else:
    print ("nilainya sama")



#2 bilangan_terbesar_3bilangan
a = int(input("Masukkan angka pertama   : "))
b = int(input("Masukkan angka kedua     : "))
c = int(input("Masukkan angka ketiga    : "))
if a>=b and a>=c:
    print ("angka terbesar adalah",a)
elif b>=a and b>=c:
    print ("angka terbesar adalah",b)
else:
    print ("angka terbesar adalah",c)



#3 fibonacci
length = 10
x = 0
y = 1
iteration = 0
if length <= 0:
    print("masukkan angka yang lebih besar dari nol")
elif length == 1:
    print("Deret fibonacci ini memiliki {} elemen".format(length),":")
    print(x)
else:
    print("Deret fibonacci ini memiliki {} elemen".format(length),":")
while(iteration < length):
    print(x, end=',')
    z = x+y
    x=y
    y=z
    iteration +=1



#4 mencari bilangan ganjil
n = int(input("Masukkan angka   : "))
for i in range (1,n,2):
    print(i)


#5 DESAIN ABC 3 kebawah
a = int(input("Ulang 3 kali aja yaaa : "))
for i in range(a):
    print("A B C")