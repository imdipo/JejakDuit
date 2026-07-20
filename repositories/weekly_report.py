from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.log_duit import LogDuit

def laporan_mingguan(db:Session):
    minggu_lalu = datetime.now() - timedelta(days=7)
    
    list_transaksi = (
        db.query(LogDuit).filter(LogDuit.waktu_transaksi >= minggu_lalu).order_by(LogDuit.waktu_transaksi.desc())
        .all()
    )

    if not list_transaksi:
        return "Tidak ada transaksi dalam 7 hari terakhir."
    
    teks = "DAFTAR TRANSAKSI 7 HARI TERAKHIR:\n"

    log_transaksi_rapih = []
    for data in list_transaksi:
        teks += f"- [{data.waktu_transaksi.strftime('%Y-%m-%d')}] {data.jenis.upper()}: Rp{data.nominal:,.0f} | Penerima: {data.penerima} | Ket: {data.keterangan}\n"
    
    return log_transaksi_rapih