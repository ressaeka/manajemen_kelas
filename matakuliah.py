import os
import sqlite3

def home():
    while True:
        os.system("cls")
        print("Selamat Datang")
        print("-" * 15)
        print("1. Matakuliah")
        print("2. Keluar")
        print("-" * 15)
        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            halaman_matakuliah() 
        elif pilihan == "2":
            print("\nKeluar dari program. Sampai jumpa!")
            exit()
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk kembali ke menu utama...")

def halaman_matakuliah():
    while True:
        os.system("cls")
        print("\n==Halaman Matakuliah==")
        print("1. Tambah Matakuliah")
        print("2. Lihat Matakuliah")
        print("3. Edit Matakuliah")
        print("4. Hapus Matakuliah")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            tambah_matakuliah()
        elif pilihan == "2":
            lihat_matakuliah()
        elif pilihan == "3":
            edit_matakuliah()
        elif pilihan == "4":
            hapus_matakuliah()
        elif pilihan == "5":
            break 
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

def tambah_matakuliah():
    conn = sqlite3.connect('matakuliah.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS matakuliah (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            kode TEXT,
            sks INTEGER,
            semester INTEGER
        )
    ''')

    nama_matakuliah = input("\nMasukkan nama matakuliah: ").strip()
    kode = input("Masukkan kode matakuliah: ").strip()
    sks = int(input("Masukkan jumlah SKS: ").strip())
    semester = int(input("Masukkan semester: ").strip())

    cursor.execute('''
        INSERT INTO matakuliah (nama, kode, sks, semester)
        VALUES (?, ?, ?, ?)
    ''', (nama_matakuliah, kode, sks, semester))

    conn.commit()
    conn.close()
    print("\nData matakuliah berhasil ditambahkan.")
    input("Tekan Enter untuk kembali ke menu Matakuliah...")

def lihat_matakuliah():
    conn = sqlite3.connect('matakuliah.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM matakuliah")
    rows = cursor.fetchall()

    if rows:
        print("\n== Data Matakuliah ==")
        for row in rows:
            print(f"ID: {row[0]}, Nama: {row[1]}, Kode: {row[2]}, SKS: {row[3]}, Semester: {row[4]}")
    else:
        print("\nTidak ada data matakuliah.")

    conn.close()
    input("\nTekan Enter untuk kembali ke menu Matakuliah...")

def edit_matakuliah():
    conn = sqlite3.connect('matakuliah.db')
    cursor = conn.cursor()

    print("\nData Sebelum Pembaruan:")
    cursor.execute("SELECT * FROM matakuliah")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Nama: {row[1]}, Kode: {row[2]}, SKS: {row[3]}, Semester: {row[4]}")

    id_matakuliah = int(input("\nMasukkan ID Matakuliah yang ingin diubah: ").strip())
    nama_baru = input("Masukkan Nama Baru: ").strip()
    kode_baru = input("Masukkan Kode Baru: ").strip()
    sks_baru = int(input("Masukkan SKS Baru: ").strip())
    semester_baru = int(input("Masukkan Semester Baru: ").strip())

    cursor.execute('''
        UPDATE matakuliah
        SET nama = ?, kode = ?, sks = ?, semester = ?
        WHERE id = ?
    ''', (nama_baru, kode_baru, sks_baru, semester_baru, id_matakuliah))

    conn.commit()
    print("\nData berhasil diperbarui.")
    conn.close()
    input("\nTekan Enter untuk kembali ke menu Matakuliah...")

def hapus_matakuliah():
    conn = sqlite3.connect('matakuliah.db')
    cursor = conn.cursor()

    print("\nData Sebelum Penghapusan:")
    cursor.execute("SELECT * FROM matakuliah")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Nama: {row[1]}, Kode: {row[2]}, SKS: {row[3]}, Semester: {row[4]}")

    id_matakuliah = int(input("\nMasukkan ID Matakuliah yang ingin dihapus: ").strip())
    cursor.execute("DELETE FROM matakuliah WHERE id = ?", (id_matakuliah,))

    conn.commit()
    print("\nData berhasil dihapus.")
    conn.close()
    input("\nTekan Enter untuk kembali ke menu Matakuliah...")

if __name__ == "__main__":
    home()