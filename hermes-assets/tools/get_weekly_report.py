from sqlalchemy.orm import Session
from models.database import SessionLocal
from models.insights import laporanMingguan

def ambil_laporan_mingguan(limit: int=4):
    """
    Digunakan untuk mengambil beberapa laporan mingguan terakhir.

    Gunakan fungsi ini saat membuat laporan bulanan atau tahunan. atau bisa untuk keperluan menganalisis tren minggu ke minggu.
    """
    db = SessionLocal()
    try: 
        laporan = (
            db.query(laporanMingguan).order_by(laporanMingguan.tanggal_dibuat.desc())
            .limit(limit).all()
        )
    
        isi_laporan_mingguan = []
        for log in laporan:
            item = {
                "tanggal_laporan_dibuat": log.tanggal_dibuat.strftime("%Y-%m-%d"),
                "detall_insight": log.insight_data,
            }
            isi_laporan_mingguan.append(item)
        
        return isi_laporan_mingguan

    finally: db.close()

