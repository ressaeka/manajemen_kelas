# 🏫 Manajemen Kelas

**Manajemen Kelas** adalah aplikasi Python sederhana berbasis CLI (Command Line Interface) yang digunakan untuk mengelola data kelas. Aplikasi ini mendukung operasi CRUD (Create, Read, Update, Delete) serta menggunakan SQLite sebagai basis datanya.

---

## 📌 Fitur Utama

- ➕ Tambah data kelas
- 📋 Lihat daftar kelas
- ✏️ Edit data kelas
- 🗑️ Hapus data kelas
- 🔁 Navigasi menu berbasis terminal
- 🗂️ Terintegrasi dengan database SQLite

---

## 📁 Struktur File

| File              | Fungsi                                                        |
|-------------------|---------------------------------------------------------------|
| `main.py`         | Titik masuk program, menampilkan menu utama                  |
| `kelas.py`        | Logika utama fitur kelas (tambah, lihat, edit, hapus)         |
| `database.py`     | Koneksi dan operasi terhadap database SQLite (`akademik.db`)  |
| `akademik.db`     | File database SQLite untuk menyimpan data kelas               |

---

## ▶️ Cara Menjalankan

1. Pastikan Python 3 sudah terinstal di perangkat kamu.
2. Jalankan program menggunakan perintah:
   ```bash
   python main.py
