from datetime import datetime
from sqlalchemy.orm import Session
from models.log_duit import LogDuit
from datetime import datetime
import calendar


def laporan_bulanan(db: Session):
    hari_ini = datetime.now()

    if hari_ini.month == 1:
        bulan_lalu = 12
        tahun_berlaku = hari_ini.year - 1
    
    else:
        bulan_lalu == hari_ini.month - 1
        tahun_berlaku = hari_ini.year

    
    _, angka_hari_terakhir = calendar.monthrange(tahun_berlaku, bulan_lalu) # calendar biar kita dapet tanggal terakhirnya 28, 29, 30 atau, 31
    # monthrange balikin tuple (hari_pertama_sebagai_angka, jumlah_hari_dalam_bulan). ambil yang kedua

    awal_bulan = datetime(tahun_berlaku, bulan_lalu, 1, 0, 0, 0)
    akhir_bulan = datetime(tahun_berlaku, bulan_lalu, angka_hari_terakhir, 23, 59, 59)

    return db.query(LogDuit).filter(LogDuit.waktu_transaksi.between(awal_bulan, akhir_bulan)).all()