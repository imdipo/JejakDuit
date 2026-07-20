from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.log_duit import LogDuit

def laporan_mingguan(db:Session):
    minggu_lalu = datetime.now() - timedelta(days=7)
    
    list_transaksi = (
        db.query(LogDuit).filter(LogDuit.waktu_transaksi >= minggu_lalu).order_by(LogDuit.waktu_transaksi.desc())
        .all()
    )

    log_transaksi_rapih = []
    for data in list_transaksi:
        log_transaksi_rapih.append({
            "tanggal transaksi": data.waktu_transaksi.strftime("%Y-%m-%d %H:%M"),
            "kategori": data.jenis,
            "penerima": data.penerima,
            "nominal": f"Rp {data.nominal}",
            "deskripsi": data.deskripsi
        })
    
    return log_transaksi_rapih