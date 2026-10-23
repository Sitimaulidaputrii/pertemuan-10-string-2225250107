# Pertemuan 10 - String dan Pengolahan Teks 

Nama: Siti Maulida Putri Irawan
NIM: 2225250107
Kelas: 3A

## Tujuan

Memahami penggunaan string dan Python untuk membersihkan dan menormalkan data teks, seperti nama mahasiswa dan kode kelas. Program ini juga menggunakan fungsi untuk menghitung jumlah kata dan membuat inisial mmahasiswa.

## Cara Menjalankan

Program tugas dapat dijalankan melalui Terminal VS Code dengan perintah:
```bash
python tugas/normalisasi_data_mahasiswa.py
```

untuk menjalankan program latihan:
```bash
python latihan/01_dasar_string.py
```

untuk menjalankan yang lainnya, gunakan perintah sesuai dengan nama berkasnya.

## Algoritma

1. Meminta input nama mahasiswa dan kode kelas.
2. Menghapus spasi berlebih pada nama menggunakan strip().
3. Mengubah nama menjadi format title case menggunakan title().
4. Memisahkan nama menjadi beberapa kata dan mengambil huruf awal setiap kata sebagai inisial.
5. Mengubah kode kelas menjadi huruf besar menggunakan upper() dan mengganti spasi dengan tanda hubung menggunakan split() dan join().
6. Menampilkan nama, kode kelas, jumlah kata, dan inisial yang sudah dinormalisasi.

## Test Case

| No | Input | Hasil yang diharapkan | Hasil aktual | Status |
| --- | --- | --- | --- | --- |
| 1 | nama: aan hendrayana; kode kelas: pmat a 2026 | Aan Hendrayana, PMAT-A-2026, AH | Aan Hendrayana, PMAT-A-2026, 2 kata, AH | Berhasil |
| 2 | nama: fATHIYYAH mUTHMAINNAH; kode kelas: kelas b | Fathiyyah Muthmainnah, KELAS-B, FM | Fathiyyah Muthmainnah, KELAS-B, 2 kata, FM | Berhasil |
| 3 | nama: BUDI, kode kelas: pmtk 01 | BUDI, PMTK-01, B | BUDI, PMTK-01, 1 kata, B | Berhasil |
| 4 | nama: siti  nur aisyah, kode kelas: kelas c | Siti Nur Aisyah, KELAS-C, SNA | Siti Nur Aisyah, KELAS-C, 3 kata, SNA |

## Refleksi

Melalui tugas ini, saya belajar menggunakan beberapa metode string, seperti strip(), title(), upper(), split(), dan join(). Salah satu kesalahan yang saya temukan adalah lupa menggunakan tanda kurung pada pemanggilan metode string. Akibatnya, program mengalami error saat memproses teks. Saya memperbaikinya dengan menambahkan tanda kurung agar metode dapat dijalankan dan menghasilkan nilai yang sesuai.

## Referensi

Python Software Foundation. The Python Tutorial
Materi pertemuan 07 Algoritma dan Pemrograman: String dan Pengolahan Teks dalam Python.