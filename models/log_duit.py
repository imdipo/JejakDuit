from sqlalchemy import Column, String, Numeric, Text, DateTime, Enum
from models.database import Base
import enum

class jenisTransaksi(str, enum.Enum):
    pemasukan = "pemasukan"
    pengeluaran = "pengeluaran"

class LogDuit(Base):
    __tablename__ = "log_duit"

    no_referensi = Column(String(50), primary_key=True)
    penerima = Column(String(50))
    nominal = Column(Numeric(15, 2))
    jenis = Column(Enum(jenisTransaksi), nullable=False)
    deskripsi = Column(Text, nullable=True) 
    waktu_transaksi = Column(DateTime)      

















# sebelumnya belum pake orm, disimpen gapapa 
# from database import get_connection


# def create_table():
#     connect = get_connection()

#     if not connect:
#         raise Exception("gagal connect")

#     with connect:
#         with connect.cursor() as cursor: # dipakein with, jadi ga perlu nulis close sama commit lagi
#             cursor.execute(
#                 """
#             CREATE TABLE IF NOT EXISTS log_duit (
#                 no_referensi VARCHAR(50) PRIMARY KEY,
#                 tanggal_transaksi DATE,
#                 penerima VARCHAR(50),
#                 nominal NUMERIC(15, 2),
#                 deskripsi TEXT,
#                 jam_transaksi TIMESTAMP,
#                 jenis TEXT
#             );
#             """
#             )

#     print("table keuangan udah terbuat")

