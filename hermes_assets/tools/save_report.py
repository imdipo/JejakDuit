from datetime import datetime
import json
from models.database import SessionLocal
from models.insights import laporan_bulanan, laporan_mingguan, laporan_tahunan


MAP_LAPORAN = {
    "weekly": laporan_mingguan,
    "monthly": laporan_bulanan,
    "annual": laporan_tahunan
}

def simpan_laporan_ke_db(tipe_laporan: str, json_data_str: str, periode: str = None) -> str:
    """Menyimpan hasil laporan yang dibuat ke database PostgreSQL.

    Args:
        tipe_laporan (str): 'weekly', 'monthly', atau 'annual'.
        json_data_str (str): String format JSON hasil analisis.
        periode (str): String penanda periode laporan yang dianalisis (BUNKAN tanggal dibuat).
            Format yang WAJIB digunakan:
            - Jika weekly: 'YYYY-Wxx' (contoh: '2026-W03' untuk minggu ke-3 tahun 2026)
            - Jika monthly: 'YYYY-MM' (contoh: '2026-01' untuk Januari 2026)
            - Jika annual: 'YYYY' (contoh: '2026' untuk tahun 2026)
    """

    tipe_clean = tipe_laporan.lower().strip()
    if tipe_clean not in MAP_LAPORAN:
        return f"Gagal: Tipe laporan '{tipe_laporan}' tidak valid. Gunakan 'weekly', 'monthly', atau 'annual'."

    try:
        data_json = json.loads(json_data_str) if isinstance(json_data_str, str) else json_data_str
    except json.JSONDecodeError as err:
        return f"Gagal: Format JSON tidak valid. detail: {str(err)}"
    
    with SessionLocal() as db: # db session context manager katanya
        try:
            ModelClass = MAP_LAPORAN[tipe_clean]
            laporan = ModelClass(
                tanggal_dibuat = datetime.now(),
                periode = periode,
                insight_data = data_json
            )
            db.add(laporan)
            db.commit()
            return f"sudah berhasil menyimpan laporan {tipe_clean} ke database"
        except Exception as e:
            db.rollback()
            return f"Gagal proses penyimpanan: {str(e)}"