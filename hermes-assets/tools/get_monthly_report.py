from sqlalchemy.orm import Session
from models.database import SessionLocal
from models.insights import laporaBulanan

def ambil_laporan_bulanan(limit: int = 2):
    db = SessionLocal()
    try:
        laporan = (
            db.query(laporaBulanan).order_by(laporaBulanan.tanggal_dibuat.desc())
            .limit(limit).all()
        )
        isi_laporan_bulanan = []

        for insight in laporan:
            item = {
                "tanggal_laporan_dibuat": insight.tanggal_dibuat.strftime("%Y-%m-%d"),
                "detail_insight": insight.insight_data
            }
        isi_laporan_bulanan.append(item)

        return isi_laporan_bulanan
    finally:
        db.close()