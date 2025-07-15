import os
import sqlite3

def home():
    while True:
        os.system("cls")
        print("Selamat Datang")
        print("-" * 15)
        print("1. Kelas")
        print("2. Keluar")
        print("-" * 15)
        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            halaman_kelas()
        elif pilihan == "2":
            print("\nKeluar dari program. Sampai jumpa!")
            exit()
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk kembali ke menu utama...")

def halaman_kelas():
    while True:
        os.system("cls")
        print("\n== Halaman Kelas ==")
        print("1. Tambah Kelas")
        print("2. Lihat Kelas")
        print("3. Edit Kelas")
        print("4. Hapus Kelas")
        print("5. Kembali ke Menu Utama")
        pilihan = input("Masukkan pilihan: ").strip()

        if pilihan == "1":
            tambah_kelas()
        elif pilihan == "2":
            lihat_kelas()
        elif pilihan == "3":
            edit_kelas()
        elif pilihan == "4":
            hapus_kelas()
        elif pilihan == "5":
            break
        else:
            print("\nPilihan tidak valid. Silakan coba lagi.")
            input("Tekan Enter untuk melanjutkan...")

def tambah_kelas():
    conn = sqlite3.connect('akademik.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS kelas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            kode TEXT,
            jumlah_mahasiswa INTEGER
        )
    ''')

    nama_kelas = input("\nMasukkan nama kelas: ").strip()
    kode_kelas = input("Masukkan kode kelas: ").strip()
    jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: ").strip())

    cursor.execute('''
        INSERT INTO kelas (nama, kode, jumlah_mahasiswa)
        VALUES (?, ?, ?)
    ''', (nama_kelas, kode_kelas, jumlah_mahasiswa))

    conn.commit()
    conn.close()
    print("\nData kelas berhasil ditambahkan.")
    input("Tekan Enter untuk kembali ke menu Kelas...")

def lihat_kelas():
    conn = sqlite3.connect('akademik.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM kelas")
    rows = cursor.fetchall()

    if rows:
        print("\n== Data Kelas ==")
        for row in rows:
            print(f"ID: {row[0]}, Nama Kelas: {row[1]}, Kode Kelas: {row[2]}, Jumlah Mahasiswa: {row[3]}")
    else:
        print("\nTidak ada data kelas.")

    conn.close()
    input("\nTekan Enter untuk kembali ke menu Kelas...")


def edit_kelas():
    conn = sqlite3.connect('akademik.db')
    cursor = conn.cursor()

    print("\nData Sebelum Pembaruan:")
    cursor.execute("SELECT * FROM kelas")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Nama Kelas: {row[1]}, Kode Kelas: {row[2]}, Jumlah Mahasiswa: {row[3]}")

    id_kelas = int(input("\nMasukkan ID Kelas yang ingin diubah: ").strip())
    nama_baru = input("Masukkan Nama Kelas Baru: ").strip()
    kode_baru = input("Masukkan Kode Kelas Baru: ").strip()
    jumlah_mahasiswa_baru = int(input("Masukkan Jumlah Mahasiswa Baru: ").strip())

    cursor.execute('''
        UPDATE kelas
        SET nama = ?, kode = ?, jumlah_mahasiswa = ?
        WHERE id = ?
    ''', (nama_baru, kode_baru, jumlah_mahasiswa_baru, id_kelas))

    conn.commit()
    print("\nData kelas berhasil diperbarui.")
    conn.close()
    input("\nTekan Enter untuk kembali ke menu Kelas...")

def hapus_kelas():
    conn = sqlite3.connect('akademik.db')
    cursor = conn.cursor()

    print("\nData Sebelum Penghapusan:")
    cursor.execute("SELECT * FROM kelas")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Nama Kelas: {row[1]}, Kode Kelas: {row[2]}, Jumlah Mahasiswa: {row[3]}")

    id_kelas = int(input("\nMasukkan ID Kelas yang ingin dihapus: ").strip())
    cursor.execute("DELETE FROM kelas WHERE id = ?", (id_kelas,))

    conn.commit()
    print("\nData kelas berhasil dihapus.")
    conn.close()
    input("\nTekan Enter untuk kembali ke menu Kelas...")

if __name__ == "__main__":
    home()

