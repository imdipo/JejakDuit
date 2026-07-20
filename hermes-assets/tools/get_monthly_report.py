from sqlalchemy.orm import Session
from models.database import SessionLocal
from models.insights import laporan_bulanan

def ambil_laporan_bulanan(limit: int = 12):
    """
    fungsi ini digunakan setiap membuat laporan tahunan. atau bisa dipakai untuk melihat rekam jejak insight bulan lalu
    """
    db = SessionLocal()
    try:
        laporan = (
            db.query(laporan_bulanan).order_by(laporan_bulanan.tanggal_dibuat.desc())
            .limit(limit).all()
        )
        isi_laporan_bulanan = []

        for insight in laporan:
            item = {
                "tanggal_laporan_dibuat": insight.tanggal_dibuat.strftime("%Y-%m-%d"),
                "periode": insight.periode,
                "detail_insight": insight.insight_data
            }
            isi_laporan_bulanan.append(item)

        return isi_laporan_bulanan
    finally:
        db.close()