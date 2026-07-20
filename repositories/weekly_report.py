from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.log_duit import LogDuit

def laporan_mingguan(db:Session):
    minggu_lalu = datetime.now() - timedelta(days=7)
    return db.query(LogDuit).filter(LogDuit.waktu_transaksi >= minggu_lalu).all()