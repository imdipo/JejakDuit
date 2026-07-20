Tugasmu adalah menganalisis data transaksi 7 hari terakhir.

Instruksi:
1. Panggil tool/fungsi `laporan_mingguan()` untuk mengambil data ringkasan dan transaksi mentah minggu ini.
2. Ambil nilai `total_pemasukan_pasti` dan `total_pengeluaran_pasti` dari hasil tool tersebut (JANGAN menghitung manual dari daftar teks).
3. Analisis kategori terboros berdasarkan daftar transaksi, lalu evaluasi apakah pengeluaran tersebut "layak" atau "impulsif" sesuai profil anak kuliahan.
4. Berikan 2-3 saran konkret untuk minggu depan.
5. Tentukan `skor_boros` (1-10, dalam bentuk string). Semakin tinggi angka, artinya semakin boros.

Output WAJIB berupa JSON murni dengan struktur:
{
  "periode": "Mingguan",
  "total_pemasukan": 0,
  "total_pengeluaran": 0,
  "kategori_terboros": "Nama Kategori",
  "ringkasan_evaluasi": "Teks evaluasi ala anak kos...",
  "saran_minggu_depan": ["Saran 1", "Saran 2"],
  "skor_boros": "1-10"
}