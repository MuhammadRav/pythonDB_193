#no 1#
def mengubah_suhu(suhu, pilih):
    if pilih == 'C'or'c':
        fahrenheit = (suhu * 9/5) + 32
        return fahrenheit
    elif pilih == 'F'or'f':
        celsius = (suhu - 32) * 5/9
        return celsius
    else:
        return "gagal wes."

pilih = input("Masukkan pilihanmu (C/F) : ")
suhu = float(input("Masukkan suhu : "))
hasil = mengubah_suhu(suhu, pilih)
print("Hasilnya adalah : ", hasil)


#no 2#
LuasPersegi = lambda sisi: sisi**2
sisi = float(input("Masukkan sisi: "))
luas = LuasPersegi(sisi)
print("Luasnya adalah : ",luas)