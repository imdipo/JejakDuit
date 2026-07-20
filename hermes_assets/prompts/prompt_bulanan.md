Tugasmu adalah menganalisis kondisi keuangan bulan ini.

Instruksi:
1. Panggil tool `get_laporan_mingguan_terakhir(limit=4)` untuk membaca ringkasan 4 minggu terakhir.
2. Panggil tool `get_laporan_bulanan_terakhir(limit=2)` untuk membandingkan dengan bulan lalu (apakah ada peningkatan/penurunan).
3. Evaluasi apakah target tabungan bulan ini tercapai tanpa mengorbankan kualitas hidup sebagai anak kuliahan.
4. skor_boros. semakin tinggi, tandanya sangat boros 

Output WAJIB berupa JSON murni dengan struktur:
{
  "periode": "Bulanan",
  "total_pengeluaran_bulan_ini": 0,
  "perbandingan_bulan_lalu": "Teks analisis komparasi...",
  "evaluasi_gaya_hidup": "Teks evaluasi...",
  "rekomendasi_alokasi_bulan_depan": "Teks rekomendasi...",
  "skor_boros": "1-10"
}