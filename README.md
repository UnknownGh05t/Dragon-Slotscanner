# 🛡️ Dragon-SlotScanner: Anti SEO-Poisoning & Slot Spam Detector 🐉

`Dragon-SlotScanner` adalah sebuah alat audit keamanan web pasif berbasis CLI yang dirancang khusus untuk mendeteksi serangan **Silent Defacement** atau **SEO Poisoning** (suntikan kata kunci judi online/slot ilegal). 

Alat ini membantu administrator situs (terutama domain `.go.id` dan `.ac.id`) untuk memeriksa integritas konten halaman mereka dari manipulasi indeks mesin pencari oleh aktor ancaman.

---

## 🎨 Tampilan Alat
```text
  ____  ____    _    ____  ___  _   _ 

 |  _ \|  _ \  / \  / ___|/ _ \| \ | |
 | | | | |_) / _ \| |  _| | | |  \| |
 | |_| |  _ / ___ \ |_| | |_| | |\  |
 |____/|_| \_/_   \_\____|\___/|_| \_|
  ____   ____    _    _   _ _   _ _____ ____  
 / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
 \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
  ___) | |___ / ___ \| |\  | |\  | |___|  _ < 

 |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\ 
==================================================
Tool Name : Dragon SlotScanner v1.1
Author    : UnknownGh05t
Team      : LulzGhost Team
==================================================
```

---

## 💎 Fitur Utama
* **Header & Metadata Deep Scan**: Membedah komponen kritis SEO seperti `<title>` dan `<meta name="description">` yang paling sering dimanipulasi peretas.
* **Signature-Based Detection**: Menggunakan database kata kunci tanda serangan (*attack signature*) judi online terupdate.
* **Passive Inspection**: Melakukan pemeriksaan secara aman tanpa mengeksploitasi atau mengubah struktur data pada server target.
* **Raw String Interface**: Tampilan *Banner ASCII* yang dioptimalkan khusus agar tidak hancur pada layar Terminal Android (Termux).

---

## 🛠️ Persyaratan Sistem & Instalasi

Pastikan modul pemroses HTML Python sudah terpasang di lingkungan Termux Anda:

```bash
# Perbarui sistem manajemen paket Termux
pkg update && pkg upgrade -y

# Instal Python dan Git
pkg install python git -y

# Instal pustaka Requests dan BeautifulSoup4
pip install requests beautifulsoup4
```

---

## 🚀 Cara Penggunaan

Jalankan script utama menggunakan interpreter Python 3:

```bash
python dragon_scanner.py
```

### 📖 Alur Kerja Audit:
1. Masukkan URL website instansi atau target audit yang ingin diperiksa (Contoh: `https://situs-kampus.ac.id`).
2. Alat akan mengunduh kode sumber halaman secara aman.
3. Struktur dokumen dipisahkan dan dicocokkan dengan database kata kunci terlarang.
4. Jika aman, alat memunculkan sinyal **[✅] AMAN**. Jika terinfeksi, alat memunculkan tanda bahaya **[⚠️] PERINGATAN** beserta daftar kata kunci yang ditemukan.

---

## 👤 Profil Pengembang
* **Author:** UnknownGh05t
* **Team:** LulzGhost Team

---

## ⚖️ Penafian (Disclaimer)
*Alat ini dikembangkan murni untuk keperluan riset, edukasi pertahanan siber, dan audit keamanan web secara legal (*authorized security auditing*). Penyalahgunaan alat ini untuk aktivitas yang melanggar hukum siber sepenuhnya berada di luar tanggung jawab pengembang.*
