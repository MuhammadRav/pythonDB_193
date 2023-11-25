import tkinter as tk

def hasil_prediksi():
    luaran.config(text="Hasil Prediksi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")

# Membuat label judul
judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Helvetica", 16))
judul.grid(row=0, column=0, columnspan=2, pady=2)

judul = tk.Label(root, text="  Masukkan Nilai Mata Pelajaran:", font=("Helvetica",10))
judul.grid(row=1, column=0,pady=2)

# Membuat 10 input nilai mata pelajaran
mata_pelajaran = []
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    label.grid(row=1+i+1, column=0,pady=5)
    entry = tk.Entry(root)
    entry.grid(row=1+i+1, column=1,pady=5)
    mata_pelajaran.append(entry)

# Membuat button Hasil Prediksi
button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
button.grid(row=12, column=0, columnspan=2,pady=5)

# Membuat label luaran hasil prediksi
luaran = tk.Label(root, text="", font=("Helvetica", 12))
luaran.grid(row=13, column=0, columnspan=2,pady=5)

# Menampilkan GUI
root.mainloop()