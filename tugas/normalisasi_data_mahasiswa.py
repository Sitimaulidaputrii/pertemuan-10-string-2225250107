# Fungsi untuk membersihkan dan menormalkan nama mahasiswa.
def normalisasi_nama(nama):
    nama = nama.strip()
    nama = " ".join(nama.split())
    return nama.title()

# Fungsi untuk membuat inisial dari setiap kata pada nama.
def buat_inisial(nama):
    kata = nama.split()
    inisial = ""

    for k in kata:
        inisial += k[0].upper()

    return inisial

# Fungsi untuk menormalkan kode kelas.
def normalisasi_kode(kode):
    kode = kode.strip().upper()
    kode = "-".join(kode.split())
    return kode

# Input: Meminta nama mahasiswa dan kode kelas.
nama = input("Nama: ")
kode = input("Kode kelas: ")

# Proses: menormalkan data nama dan kode kelas.
nama_normal = normalisasi_nama(nama)
kode_normal = normalisasi_kode(kode)
inisial = buat_inisial(nama_normal)
jumlah_kata = len(nama_normal.split())

# Output: Menampilkan hasil normalisasi.
print("\n--- Hasil Normalisasi Nama Mahasiswa ---")
print(f"Nama          : {nama_normal} ")
print(f"Kode kelas    : {kode_normal}")
print(f"Jumlah kata   : {jumlah_kata}")
print(f"Inisial       : {inisial}")