from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models.database import SessionLocal
from models.log_duit import LogDuit
from sqlalchemy import func

def laporan_mingguan():
    """
    fungsi yang digunakan setiap minggunya, berisi query untuk mengambil semua transaksi yang terjadi 7 hari terakhir 
    sekalian mengambil total pemasukan dan pengeluaran pasti 7 hari terakhir.
    """
    minggu_lalu = datetime.now() - timedelta(days=7)

    with SessionLocal() as db:

        total_pemasukan = db.query(func.sum(LogDuit.nominal)).filter(LogDuit.waktu_transaksi >= minggu_lalu, LogDuit.jenis == "pemasukan").scalar() or 0
        total_pengeluaran = db.query(func.sum(LogDuit.nominal)).filter(LogDuit.waktu_transaksi >= minggu_lalu, LogDuit.jenis == "pengeluaran").scalar() or 0
    
        list_transaksi = (
            db.query(LogDuit).filter(LogDuit.waktu_transaksi >= minggu_lalu).order_by(LogDuit.waktu_transaksi.desc()).all()
        )

        if not list_transaksi:
            return "Tidak ada transaksi dalam 7 hari terakhir."
        
        teks_transaksi = "DAFTAR TRANSAKSI 7 HARI TERAKHIR:\n"

        for data in list_transaksi:
            teks_transaksi += f"- [{data.waktu_transaksi.strftime('%Y-%m-%d')}] {data.jenis.upper()}: Rp{data.nominal:,.0f} | Penerima: {data.penerima} | Ket: {data.deskripsi}\n"

        return {
            "total_pemasukan": total_pemasukan,
            "total_pengeluaran": total_pengeluaran,
            "daftar_transaksi": teks_transaksi
        }