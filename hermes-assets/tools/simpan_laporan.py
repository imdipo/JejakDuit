from datetime import datetime
import json
from models.database import SessionLocal
from models.insights import LaporanBulanan, LaporanMingguan, LaporanTahunan


def simpan_laporan_ke_db(tipe_laporan: str, json_data_str: str) -> str:
    """Menyimpan hasil laporan yang dibuat oleh Hermes ke database PostgreSQL.

    tipe_laporan: 'weekly', 'monthly', atau 'annual' json_data_str: string
    format JSON hasil analisis
    """
    db = SessionLocal()
    try:
        # Load string JSON dari Hermes ke Dictionary Python
        data_json = json.loads(json_data_str)
        sekarang = datetime.now()

        if tipe_laporan == "weekly":
            laporan = LaporanMingguan(
                tanggal_dibuat=sekarang, insight_data=data_json
            )
        elif tipe_laporan == "monthly":
            laporan = LaporanBulanan(
                tanggal_dibuat=sekarang, insight_data=data_json
            )
        elif tipe_laporan == "annual":
            laporan = LaporanTahunan(
                tanggal_dibuat=sekarang, insight_data=data_json
            )
        else:
            return "Tipe laporan tidak valid."

        db.add(laporan)
        db.commit()
        return f"Berhasil menyimpan {tipe_laporan} ke database!"
    except Exception as e:
        db.rollback()
        return f"Gagal menyimpan ke database: {str(e)}"
    finally:
        db.close()