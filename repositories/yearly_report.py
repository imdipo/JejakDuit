from datetime import datetime
from sqlalchemy.orm import Session
from models.log_duit import LogDuit
from datetime import datetime


def laporan_tahunan(db: Session):
    hari_ini = datetime.now()
    tahun_lalu = hari_ini.year - 1

    awal_tahun = datetime(tahun_lalu, 1,1,0,0,0)
    akhir_tahun = datetime(tahun_lalu, 12, 31, 23, 59, 59)

    return db.query(LogDuit).filter(LogDuit.waktu_transaksi.between(awal_tahun, akhir_tahun)).all()