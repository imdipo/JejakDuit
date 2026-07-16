from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.dialects.postgresql import JSONB
from models.database import Base

class laporanMingguan(Base):
    __tablename__ = "laporan_mingguan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tanggal_dibuat = Column(DateTime)
    insight_data = Column(JSONB, nullable=False)
