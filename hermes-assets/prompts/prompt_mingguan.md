Tugasmu adalah menganalisis data transaksi 7 hari terakhir.

Instruksi:
1. Panggil tool/fungsi `laporan_mingguan()` untuk mengambil data transaksi mentah minggu ini.
2. Hitung total pengeluaran dan total pemasukan.
3. Analisis kategori terboros dan evaluasi apakah pengeluaran tersebut "layak" atau "impulsif" sesuai profil anak kos.
4. Berikan 2-3 saran konkret untuk minggu depan.
5. skor_boros. semakin tinggi, tandanya sangat boros 

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