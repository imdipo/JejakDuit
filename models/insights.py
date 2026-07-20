from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.dialects.postgresql import JSONB
from models.database import Base

class laporan_mingguan(Base):
    __tablename__ = "laporan_mingguan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tanggal_dibuat = Column(DateTime)
    periode = Column(String(20), nullable=True)
    insight_data = Column(JSONB, nullable=False)

class laporan_bulanan(Base):
    __tablename__ = "laporan_bulanan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tanggal_dibuat = Column(DateTime)
    periode = Column(String(20), nullable=True)
    insight_data = Column(JSONB, nullable=False)

class laporan_tahunan(Base):
    __tablename__ = "laporan_tahunan"

    id = Column(Integer, primary_key=True, autoincrement=True)
    tanggal_dibuat = Column(DateTime)
    periode = Column(String(20), nullable=True)
    insight_data = Column(JSONB, nullable=False)
