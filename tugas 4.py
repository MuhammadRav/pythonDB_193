class PersegiPanjang:
    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def Keliling(self):
        return 2 * (self.panjang + self.lebar)
    
    def Luas(self):
        return self.panjang * self.lebar
    
    def __str__(self):
        return f"Persegi Panjang, panjang  {self.panjang} cm, dan lebar {self.lebar} cm"
    
panjang = float(input("Masukkan panjang : "))
lebar = float(input("Masukkan lebar : "))
Persegi_Panjang = PersegiPanjang(panjang, lebar)

print(Persegi_Panjang)
print(f"Kelilingnya adalah : {Persegi_Panjang.Keliling()} cm")
print(f"Luasnya adalah : {Persegi_Panjang.Luas()} cm^2")
