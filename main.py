from models.database import init_database, get_database
from models.log_duit import LogDuit
from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends, HTTPException, Cookie, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
import os
import uuid
from decimal import Decimal
import repositories.log_repository as log_repo
import repositories.all_log as all_log


init_database()
print("sudah terbuat tablenya")

app = FastAPI(title="Dashboard Duit")

# In-memory session database
active_sessions = set()

def verify_session(session_id: str = Cookie(None)):
    if not session_id or session_id not in active_sessions:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    return session_id

@app.get("/", response_class=HTMLResponse)
def read_index(session_id: str = Cookie(None)):
    if not session_id or session_id not in active_sessions:
        return RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates", "index.html")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>Frontend index.html not found</h1><p>Please make sure templates/index.html is created.</p>", status_code=404)

@app.get("/login", response_class=HTMLResponse)
def read_login(session_id: str = Cookie(None)):
    if session_id and session_id in active_sessions:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates", "login.html")
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    return HTMLResponse(content="<h1>Login page login.html not found</h1>", status_code=404)

@app.post("/login")
def login_post(username: str = Form(...), password: str = Form(...)):
    expected_username = os.getenv("DASHBOARD_USERNAME")
    expected_password = os.getenv("DASHBOARD_PASSWORD")
    
    if username == expected_username and password == expected_password:
        new_session = str(uuid.uuid4())
        active_sessions.add(new_session)
        
        response = JSONResponse(content={"status": "sukses", "message": "Login berhasil"})
        response.set_cookie(
            key="session_id",
            value=new_session,
            httponly=True,
            samesite="lax",
            max_age=3600 * 24 * 7 # 1 week
        )
        return response
        
    raise HTTPException(status_code=400, detail="Username atau Password salah")

@app.post("/logout")
@app.get("/logout")
def logout_post(session_id: str = Cookie(None)):
    if session_id in active_sessions:
        active_sessions.remove(session_id)
    response = RedirectResponse(url="/login", status_code=status.HTTP_303_SEE_OTHER)
    response.delete_cookie("session_id")
    return response

@app.get("/logs")
def lihat_semua_transakasi(db:Session = Depends(get_database), session_id: str = Depends(verify_session)):
    return  all_log.get_all_logs(db)

@app.patch("/logs/editDeskripsi/{nomor_referensi}")
def isi_deskripsi(nomor_referensi: str, deskripsi_baru: str, db: Session = Depends(get_database), session_id: str = Depends(verify_session)):
    update_deskripsi = log_repo.update_deskripsi(db, nomor_referensi=nomor_referensi, deskripsi_baru=deskripsi_baru)
    if not update_deskripsi:
        raise HTTPException(status_code=404, detail="nomor referensi tidak ditemukan")
    return {"status": "sukses", "data": update_deskripsi}


@app.get("/logs/saldo")
def lihat_total_saldo(db: Session = Depends(get_database), session_id: str = Depends(verify_session)):
    return log_repo.total_duit(db)

@app.post("/logs/tambah-manual")
def tambah_transaksi_manual(nominal: Decimal, deskripsi: str, jenis: str, penerima: str, db: Session = Depends(get_database), session_id: str = Depends(verify_session)):
    nominal_desimal = Decimal(str(nominal))
    transaksi_baru = log_repo.create_uang_masuk(
        db = db,
        penerima=penerima, 
        nominal=nominal_desimal, 
        deskripsi=deskripsi, 
        jenis=jenis
        )
    
    return {"status":"sukses", "data":transaksi_baru}

@app.delete("/logs/{nomor_referensi}")
def hapus_transaksi(nomor_referensi: str, db: Session = Depends(get_database), session_id: str = Depends(verify_session)):
    deleted = log_repo.delete_transaksi(db, nomor_referensi=nomor_referensi)
    if not deleted:
        raise HTTPException(status_code=404, detail="nomor referensi tidak ditemukan")
    return {"status": "sukses", "message": "Transaksi berhasil dihapus"}


