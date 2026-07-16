import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.database import SessionLocal
from models.log_duit import LogDuit, jenisTransaksi
# fungsi-fungsi bersih-bersih dari file sebelah
from scrapers.parser_email import read_gmail, parse_email, reformatting 

def save_to_postgres(data_siap_db):
    db = SessionLocal()
    try:
        print(f"Memulai proses insert {len(data_siap_db)} data ke Postgres...")
        for data in data_siap_db:
            duplikat = db.query(LogDuit).filter(LogDuit.no_referensi == data["nomorReferensi"]).first()
            if duplikat:
                print(f"Data {data['nomorReferensi']} sudah ada, skip!")
                continue
                
            transaksi_baru = LogDuit(
                no_referensi = data["nomorReferensi"],
                penerima = data["penerima"],
                nominal = data["nominal"],
                jenis = jenisTransaksi.pengeluaran.value,
                waktu_transaksi = data["waktuTransaksi"],
                deskripsi = None,
            )
            db.add(transaksi_baru)
            
        db.commit()
        print("Semua data baru berhasil disimpan ke PostgreSQL dengan selamat!")
    except Exception as e:
        db.rollback()
        print(f"error pas save ke DB: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Pipeline Ingestion Gmail (pig xixi)")
    
    html_mentah = read_gmail()
    data_bersih = parse_email(html_mentah)
    data_siap = reformatting(data_bersih)
    
    if data_siap:
        save_to_postgres(data_siap)
    else:
        print("tidak ada transaksi data yang perlu diproses.")
        
    print("--- Pipeline Selesai ---")