from sqlalchemy.orm import Session
from models.database import SessionLocal
from models.insights import laporan_mingguan

def ambil_laporan_mingguan(limit: int=4):
    """
    Digunakan untuk mengambil beberapa laporan mingguan terakhir.

    Gunakan fungsi ini saat membuat laporan bulanan atau tahunan. atau bisa untuk keperluan menganalisis tren minggu ke minggu.
    """
    db = SessionLocal()
    try: 
        laporan = (
            db.query(laporan_mingguan).order_by(laporan_mingguan.tanggal_dibuat.desc())
            .limit(limit).all()
        )
    
        isi_laporan_mingguan = []
        for insight in laporan:
            item = {
                "tanggal_laporan_dibuat": insight.tanggal_dibuat.strftime("%Y-%m-%d"),
                "periode": insight.periode,
                "detall_insight": insight.insight_data,
            }
            isi_laporan_mingguan.append(item)
        
        return isi_laporan_mingguan

    finally: db.close()

