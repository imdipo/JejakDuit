from models.database import engine, Base, get_database
from models.log_duit import LogDuit
from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends, HTTPException
from decimal import Decimal
import repositories.log_repository as log_repo
import repositories.all_log as all_log


Base.metadata.create_all(bind=engine)
print("sudah terbuat tablenya")

app = FastAPI(title="Dashboard Duit")

@app.get("/logs")
def lihat_semua_transakasi(db:Session = Depends(get_database)):
    return  all_log.get_all_logs(db)

@app.patch("/logs/editDeskripsi/{nomor_referensi}")
def isi_deskripsi(nomor_referensi: str, deskripsi_baru: str, db: Session = Depends(get_database)):
    update_deskripsi = log_repo.update_deskripsi(db, nomor_referensi=nomor_referensi, deskripsi_baru=deskripsi_baru)
    if not update_deskripsi:
        raise HTTPException(status_code=404, detail="nomor referensi tidak ditemukan")
    return {"status": "sukses", "data": update_deskripsi}


@app.get("/logs/saldo")
def lihat_total_saldo(db: Session = Depends(get_database)):
    return log_repo.total_duit(db)

@app.post("/logs/tambah-manual")
def tambah_transaksi_manual(nominal: Decimal, deskripsi: str, jenis: str, penerima: str, db: Session = Depends(get_database)):
    nominal_desimal = Decimal(str(nominal))
    transaksi_baru = log_repo.create_uang_masuk(
        db = db,
        penerima=penerima, 
        nominal=nominal_desimal, 
        deskripsi=deskripsi, 
        jenis=jenis
        )
    
    return {"status":"sukses", "data":transaksi_baru}
