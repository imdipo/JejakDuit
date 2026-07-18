from sqlalchemy.orm import Session
from models.log_duit import LogDuit

def get_all_logs(db: Session):
    return db.query(LogDuit).order_by(LogDuit.waktu_transaksi.desc()).all()


