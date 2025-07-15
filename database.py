import sqlite3 as database

conn = database.connect('db_futsal')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS pengguna
(
    id_pengguna INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) UNIQUE,
    kata_sandi VARCHAR(255),
    email VARCHAR(100),
    peran TEXT,
    tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS lapangan
(
    id_lapangan INTEGER PRIMARY KEY AUTOINCREMENT,
    nama VARCHAR(100),
    nama_jenis_lapangan VARCHAR(100),
    harga_per_jam DECIMAL(10, 2),
    status_ketersediaan BOOLEAN DEFAULT 1,
    deskripsi TEXT
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS jenis_lapangan
(
    id_jenis_lapangan INTEGER PRIMARY KEY AUTOINCREMENT,
    nama_jenis_lapangan VARCHAR(100),
    harga_per_jam DECIMAL(10, 2)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS pemesanan
(
    id_pemesanan INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pengguna INTEGER,
    id_lapangan INTEGER,
    tanggal_pemesanan DATE,
    waktu_mulai TIME,
    waktu_selesai TIME,
    total_harga DECIMAL(10, 2),
    status TEXT,
    tanggal_dibuat TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(id_pengguna) REFERENCES pengguna(id_pengguna),
    FOREIGN KEY(id_lapangan) REFERENCES lapangan(id_lapangan)
)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS pembayaran
(
    id_pembayaran INTEGER PRIMARY KEY AUTOINCREMENT,
    id_pemesanan INTEGER,
    id_pengguna INTEGER,
    jumlah DECIMAL(10,2),
    tanggal_pembayaran TIMESTAMP,
    metode_pembayaran TEXT,
    status TEXT,
    FOREIGN KEY(id_pemesanan) REFERENCES pemesanan(id_pemesanan),
    FOREIGN KEY(id_pengguna) REFERENCES pengguna(id_pengguna)
)''')

cursor.execute("INSERT INTO pengguna (username, kata_sandi, email, peran) VALUES ('admin', 'admin', 'admin@gmail.com', 'admin')")
cursor.execute("INSERT INTO pengguna (username, kata_sandi, email, peran) VALUES ('user', 'user', 'user@gmail.com', 'pengguna')")

cursor.execute("INSERT INTO jenis_lapangan (nama_jenis_lapangan, harga_per_jam) VALUES ('Sintetis', 100000)")
cursor.execute("INSERT INTO jenis_lapangan (nama_jenis_lapangan, harga_per_jam) VALUES ('Vinyl', 150000)")

cursor.execute("INSERT INTO lapangan (nama, nama_jenis_lapangan, harga_per_jam, status_ketersediaan, deskripsi) VALUES ('Lapangan A', 'Sintetis', 100000, 1, 'Lapangan A dengan jenis Lapangan sintetis')")
cursor.execute("INSERT INTO lapangan (nama, nama_jenis_lapangan, harga_per_jam, status_ketersediaan, deskripsi) VALUES ('Lapangan B', 'Vinyl', 150000, 1, 'Lapangan B dengan jenis Lapangan vinyl')")

cursor.execute("INSERT INTO pemesanan (id_pengguna, id_lapangan, tanggal_pemesanan, waktu_mulai, waktu_selesai, total_harga, status) VALUES (1, 1, '2021-12-01', '08:00:00', '10:00:00', 200000, 'menunggu')")

cursor.execute("INSERT INTO pembayaran (id_pemesanan, id_pengguna, jumlah, tanggal_pembayaran, metode_pembayaran, status) VALUES (1, 1, 200000, '2021-12-01 10:00:00', 'tunai', 'lunas')")

conn.commit()
conn.close()

