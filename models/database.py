import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base() 
# ini buat ngambil semua nama table, kolom, tipe data, relasi foreign key ke Base.metadata
# Base.metadata, properti dari fungsi declrataive base yang kita taro di log_duit itu loh


def get_database():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_database():
    Base.metadata.create_all(bind=engine)





# def get_connection():
#     try: 
#         conn = psycopg2.connect(
#             dbname = os.getenv("DB_NAME"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             host=os.getenv("DB_HOST"),
#             port=os.getenv("DB_PORT")
#         )
#         print("connected")
#         return conn
    
#     except Exception as e:
#         print(f"gagal: {e}")
#         return None

