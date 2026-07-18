from sqlalchemy.orm import Session
from datetime import datetime
from decimal import Decimal
from sqlalchemy import func
from models.log_duit import LogDuit, jenisTransaksi

def total_duit(db:Session):
    total_pemasukan = db.query(func.sum(LogDuit.nominal)).filter(LogDuit.jenis == "pemasukan").scalar() or 0
    total_pengeluaran = db.query(func.sum(LogDuit.nominal)).filter(LogDuit.jenis == "pengeluaran").scalar() or 0
    
    total_duit_gw = total_pemasukan - total_pengeluaran

    return total_duit_gw

# update, buat update deskripsi. biar nanti si AI-nya paham ini pengeluaran buat apa
def update_deskripsi(db:Session, nomor_referensi:str, deskripsi_baru:str):
    # ambil data berdasarkan nomor referensinya
    db_log = db.query(LogDuit).filter(LogDuit.no_referensi == nomor_referensi).first()

    if db_log:
        db_log.deskripsi = deskripsi_baru
        db.commit()
        db.refresh(db_log)

        return db_log
    return None

# create, uang masuk ga ada notifnya. jadi yaudah manual juga (sekalian buat uang keluar kalo ga kecatet)
def create_uang_masuk(db:Session, nominal: Decimal, deskripsi: str, jenis: str, penerima: str):
    no_ref_manual = f"MNL-{int(datetime.now().timestamp())}" # generate otomatis pake timestamp aja, ga ada referensinya kan 

    transaksi_baru = LogDuit(
    no_referensi = no_ref_manual,
    penerima = penerima,
    nominal = nominal,
    jenis = jenis,
    deskripsi = deskripsi,
    waktu_transaksi = datetime.now()  
    )

    db.add(transaksi_baru)
    db.commit()
    db.refresh(transaksi_baru)
    return transaksi_baru


def delete_transaksi(db: Session, nomor_referensi: str):
    db_log = db.query(LogDuit).filter(LogDuit.no_referensi == nomor_referensi).first()
    if db_log:
        db.delete(db_log)
        db.commit()
        return True
    return False



         