Tugasmu adalah menyusun evaluasi keuangan tahunan.

Instruksi:
1. Panggil tool `get_laporan_bulanan_terakhir(limit=12)` untuk membaca seluruh rangkuman 12 bulan terakhir.
2. Identifikasi bulan mana yang paling boros dan bulan mana yang paling efisien.
3. Buat strategi besar untuk tahun depan agar tabungan semakin tebal.

Output WAJIB berupa JSON murni dengan struktur:
{
  "periode": "Tahunan",
  "bulan_terboros": "Nama Bulan",
  "bulan_terhemat": "Nama Bulan",
  "analisis_tren_tahunan": "Teks tren...",
  "pencapaian_gaya_hidup_kos": "Teks refleksi...",
  "strategi_tahun_depan": ["Strategi 1", "Strategi 2"]
}