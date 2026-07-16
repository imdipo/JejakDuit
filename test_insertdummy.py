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

# def insert_data_bersih(list_data_email):
#     # 1. Buka koneksi/session ke database
  
    
#     try:
#         # 2. Looping data email kamu yang berbentuk list of dict
#         for data in list_data_email:
            
#             # 3. Ubah DICTIONARY menjadi OBJECT CLASS (Kuncinya di sini!)

            
#             # 4. Daftarkan object ini ke antrean database
            
        
#         # 5. Ketuk palu! Kirim dan simpan semua data sekaligus ke Postgres

        
#     except Exception as e:
#         db.rollback() # Batalkan semua jika ada 1 saja yang error (misal no. referensi kembar)
#         print(f"Gagal insert data karena: {e}")
#     finally:
#         db.close() # Putuskan koneksi setelah selesai