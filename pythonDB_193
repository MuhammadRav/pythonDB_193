import sqlite3
from tkinter import *

def prediksi_fakultas(biologi, fisika, inggris, matematika, kimia, sejarah, geografi, seni, ekonomi, agama):
    mata_pelajaran = {
        'Biologi': biologi,
        'Fisika': fisika,
        'Inggris': inggris,
        'Matematika': matematika,
        'Kimia': kimia,
        'Sejarah': sejarah,
        'Geografi': geografi,
        'Seni': seni,
        'Ekonomi': ekonomi,
        'Agama': agama
    }

    mata_pelajaran_tertinggi = max(mata_pelajaran, key=mata_pelajaran.get)

    if mata_pelajaran_tertinggi == 'Biologi':
        return "Kedokteran"
    elif mata_pelajaran_tertinggi == 'Fisika':
        return "Teknik"
    elif mata_pelajaran_tertinggi == 'Inggris':
        return "Bahasa"
    elif mata_pelajaran_tertinggi == 'Matematika':
        return "Guru MTK"
    elif mata_pelajaran_tertinggi == 'Kimia':
        return "Penelitian"
    elif mata_pelajaran_tertinggi == 'Sejarah':
        return "Ahli Sejarah"
    elif mata_pelajaran_tertinggi == 'Geografi':
        return "BMKG"
    elif mata_pelajaran_tertinggi == 'Seni':
        return "Seni"
    elif mata_pelajaran_tertinggi == 'Ekonomi':
        return "Akuntan"
    elif mata_pelajaran_tertinggi == "Agama":
        return "Ustadddz"
    else:
        return "Pilih sesuai keinginan dari nilai tertinggi yang sama"

def simpan_data(nama, biologi, fisika, inggris, matematika, kimia, sejarah, geografi, seni, ekonomi, agama):
    conn = sqlite3.connect('nilaisiswa.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            matematika INTEGER,
            kimia INTEGER,
            sejarah INTEGER,
            geografi INTEGER,
            seni INTEGER,
            ekonomi INTEGER,
            agama INTEGER,
            prediksi_fakultas TEXT  
        )
    ''')

    prediksi = prediksi_fakultas(biologi, fisika, inggris, matematika, kimia, sejarah, geografi, seni, ekonomi, agama)

    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, matematika, kimia, sejarah, geografi, seni, ekonomi, agama, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (nama, biologi, fisika, inggris, matematika, kimia, sejarah, geografi, seni, ekonomi, agama, prediksi))

    conn.commit()
    conn.close()

def submit_nilai():
    nama = entry_nama.get()
    nilai_biologi_val = nilai_biologi.get()
    nilai_fisika_val = nilai_fisika.get()
    nilai_inggris_val = nilai_inggris.get()
    nilai_matematika_val = nilai_matematika.get()
    nilai_kimia_val = nilai_kimia.get()
    nilai_sejarah_val = nilai_sejarah.get()
    nilai_geografi_val = nilai_geografi.get()
    nilai_seni_val = nilai_seni.get()
    nilai_ekonomi_val = nilai_ekonomi.get()
    nilai_agama_val = nilai_agama.get()

    simpan_data(nama, nilai_biologi_val, nilai_fisika_val, nilai_inggris_val, nilai_matematika_val, nilai_kimia_val, nilai_sejarah_val, nilai_geografi_val, nilai_seni_val, nilai_ekonomi_val, nilai_agama_val)

    label_hasil.config(text=f"Hasil prediksi: {prediksi_fakultas(nilai_biologi_val, nilai_fisika_val, nilai_inggris_val, nilai_matematika_val, nilai_kimia_val, nilai_sejarah_val, nilai_geografi_val, nilai_seni_val, nilai_ekonomi_val, nilai_agama_val)}")

root = Tk()
root.title("Input Nilai Siswa")

Label(root, text="Nama Siswa:").grid(row=0, column=0, padx=10, pady=5)
entry_nama = Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="Nilai Biologi:").grid(row=1, column=0, padx=10, pady=5)
nilai_biologi = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_biologi.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Nilai Fisika:").grid(row=2, column=0, padx=10, pady=5)
nilai_fisika = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_fisika.grid(row=2, column=1, padx=10, pady=5)

Label(root, text="Nilai Inggris:").grid(row=3, column=0, padx=10, pady=5)
nilai_inggris = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_inggris.grid(row=3, column=1, padx=10, pady=5)

Label(root, text="Nilai Matematika:").grid(row=4, column=0, padx=10, pady=5)
nilai_matematika = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_matematika.grid(row=4, column=1, padx=10, pady=5)

Label(root, text="Nilai Kimia:").grid(row=5, column=0, padx=10, pady=5)
nilai_kimia = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_kimia.grid(row=5, column=1, padx=10, pady=5)

Label(root, text="Nilai Sejarah:").grid(row=6, column=0, padx=10, pady=5)
nilai_sejarah = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_sejarah.grid(row=6, column=1, padx=10, pady=5)

Label(root, text="Nilai Geografi:").grid(row=7, column=0, padx=10, pady=5)
nilai_geografi = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_geografi.grid(row=7, column=1, padx=10, pady=5)

Label(root, text="Nilai Seni:").grid(row=8, column=0, padx=10, pady=5)
nilai_seni = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_seni.grid(row=8, column=1, padx=10, pady=5)

Label(root, text="Nilai Ekonomi:").grid(row=9, column=0, padx=10, pady=5)
nilai_ekonomi = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_ekonomi.grid(row=9, column=1, padx=10, pady=5)

Label(root, text="Nilai Agama:").grid(row=10, column=0, padx=10, pady=5)
nilai_agama = Scale(root, from_=0, to=100, orient=HORIZONTAL)
nilai_agama.grid(row=10, column=1, padx=10, pady=5)

Button(root, text="Submit Nilai", command=submit_nilai).grid(row=11, column=0, columnspan=2, pady=10)

label_hasil = Label(root, text=" ")
label_hasil.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()