dapetin credentials
```
https://console.cloud.google.com/
```

install 
```

pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

penjelasannya masih dibuat, nanti akan diupdate readme nya hehe. sementara pake penjelasan gambar dibawah ini dulu:

![simple work flow](asset/mermaid.png)

Penjelasan Sederhana Alur Sistem:

1. Ingestion Layer (Data Pipeline):

    - Script Python secara berkala mengekstrak email transaksi mentah dari Gmail API, membersihkan datanya (cleaning & parsing), lalu menyimpannya ke PostgreSQL.

2. Storage & DB Layer:

    - PostgreSQL menyimpan raw transactions serta tabel-tabel terstruktur untuk penampung laporan analisis (laporan_mingguan, bulanan, tahunan).

3. Agentic AI Layer (Hermes Agent):

    - Hermes Cron Daemon otomatis memicu Hermes AI Agent sesuai jadwal (Senin jam 08:00, Tanggal 1, dsb.).

    - Agent membaca DB via Native Tool Calling, melakukan financial reasoning, lalu menyimpan hasil analisis JSON kembali ke database secara aman (anti-crash fallback).

4. Alerts & Notification:

    - Hasil ringkasan analisis finansial langsung dikirim secara real-time ke Discord Webhook sebagai laporan akhir.

lebih lengkapnya, masih dibikin penjelasannya hehe ditunggu ya 👉👈