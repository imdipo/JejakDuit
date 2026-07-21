from models.log_duit import LogDuit
from models.database import SessionLocal

db = SessionLocal()


data_baru = LogDuit(
nominal=45000.00,
tanggal_transaksi="2026-05-31",
no_referensi="MDR99998"
)

db.add(data_baru)

db.commit()
print("Semua data berhasil disimpan ke Postgres tanpa query SQL!", flush=True)

db.close() 

