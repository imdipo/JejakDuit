from bs4 import BeautifulSoup
from get_email import read_gmail
from decimal import Decimal
from datetime import datetime
import re

mapping_info = {
    "No. Referensi": "nomorReferensi",
    "Nomor Referensi": "nomorReferensi",
    "Tanggal": "tanggal",
    "Jam": "jam",

    "Nominal Transaksi": "nominal",
    "Total Transaksi": "nominal",
    "Proteksi Jiwa": "nominal",  
}

def parse_email(html_mentah):
    html_bersih = []
    for html in html_mentah:
        data_bersih = {}
        soup = BeautifulSoup(html, "html.parser")
        penerima = soup.find("td", style=lambda s: s and "background-color:#fafafa" in re.sub(r"\s+", "", s))

        nama_penerima = None
        if penerima:
            nama_penerima = penerima.find("h4").get_text(strip=True)
        
        print(f"nama penerima: {nama_penerima}")

        data_bersih["penerima"] = nama_penerima

        tabel = soup.find_all("tr")
        for baris in tabel:
            data = baris.find_all("td")
            if len(data) == 2:
                label = data[0].get_text(strip=True)
                value = data[1].get_text(strip=True)

                if label in mapping_info:
                    data_bersih[mapping_info[label]] = value
        
        print(f"ini data bersih dari parse_email: {data_bersih}")

        html_bersih.append(data_bersih)

    return html_bersih

BULAN_INDO_TO_ENG = {
    'Jan': 'Jan', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Apr',
    'Mei': 'May', 'Jun': 'Jun', 'Jul': 'Jul', 'Agu': 'Aug',
    'Sep': 'Sep', 'Okt': 'Oct', 'Nov': 'Nov', 'Des': 'Dec'
}

def bersihkan_dan_gabungkan_waktu(tanggal_str, jam_str):
    jam_bersih = jam_str.replace(" WIB", "") 

    for bulan_indo, bulan_inggris in BULAN_INDO_TO_ENG.items():
        if bulan_indo in tanggal_str:
            tanggal_str = tanggal_str.replace(bulan_indo, bulan_inggris)

    waktu_gabungan = f"{tanggal_str} {jam_bersih}" # jadi '7 Jul 2026 13:29:14'
    pola_waktu = "%d %b %Y %H:%M:%S"
    objek_datetime = datetime.strptime(waktu_gabungan, pola_waktu)
    
    return objek_datetime

def reformatting(list_email_bersih):
    for data in list_email_bersih:
        angka_nominal = re.sub(r'[^\d,]', '', data["nominal"])
        angka_nominal = angka_nominal.replace(",", ".")
        data["nominal"] = Decimal(angka_nominal)

        data["waktuTransaksi"] = bersihkan_dan_gabungkan_waktu(data["tanggal"], data["jam"])

        data.pop("tanggal","")
        data.pop("jam","")
    return list_email_bersih 

# hasil_akhir = reformatting()
# print("Hasil Akhir:", hasil_akhir)

