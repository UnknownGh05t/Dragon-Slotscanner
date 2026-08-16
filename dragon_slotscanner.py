import os
import sys
import requests
import urllib.parse
from bs4 import BeautifulSoup

# Kode Warna ANSI untuk Termux
HIJAU = "\033[92m"
MERAH = "\033[91m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
PUTIH = "\033[97m"
RESET = "\033[0m"

def tampilkan_banner():
    os.system('clear')
    # PERBAIKAN: Menggunakan fr""" (Raw String) agar karakter backslash tidak merusak susunan teks
    banner = fr"""
{MERAH}  ____  ____    _    ____  ___  _   _ 

 |  _ \|  _ \  / \  / ___|/ _ \| \ | |
 | | | | |_) / _ \| |  _| | | |  \| |
 | |_| |  _ / ___ \ |_| | |_| | |\  |
 |____/|_| \_/_   \_\____|\___/|_| \_|
  ____   ____    _    _   _ _   _ _____ ____  
 / ___| / ___|  / \  | \ | | \ | | ____|  _ \ 
 \___ \| |     / _ \ |  \| |  \| |  _| | |_) |
  ___) | |___ / ___ \| |\  | |\  | |___|  _ < 

 |____/ \____/_/   \_\_| \_|_| \_|_____|_| \_\ {RESET}
==================================================
{HIJAU}Tool Name : Dragon SlotScanner v1.1
Author    : UnknownGh05t
Team      : LulzGhost Team{RESET}
==================================================
"""
    print(banner)

def pindai_halaman(url_target):
    if not url_target.startswith("http://") and not url_target.startswith("https://"):
        url_target = "https://" + url_target

    print(f"{PUTIH}[*] Menghubungi target: {url_target} ...{RESET}")
    
    signatures = [
        "slot gacor", "judi online", "situs slot", "bandar togel", "live casino", 
        "agen slot", "deposit pulsa", "jackpot besar", "rtp live", "maxwin", 
        "taruhan bola", "sbobet", "pragmatic play", "slot88", "link alternatif"
    ]
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url_target, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"{MERAH}[-] Respons server tidak normal. HTTP Status: {response.status_code}{RESET}")
            return

        soup = BeautifulSoup(response.text, 'html.parser')
        
        judul = soup.title.string.lower() if soup.title else ""
        
        deskripsi = ""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc and meta_desc.get('content'):
            deskripsi = meta_desc.get('content').lower()

        seluruh_teks = soup.get_text().lower()

        print(f"{BIRU}[*] Menganalisis tanda tanda anomali kode...{RESET}")
        
        kata_terdeteksi = []
        for kata in signatures:
            if kata in judul or kata in deskripsi or kata in seluruh_teks:
                kata_terdeteksi.append(kata)

        print(f"\n{CYAN}[ HASIL AUDIT INTEGRITAS KONTEN ]{RESET}")
        if kata_terdeteksi:
            print(f"{MERAH}[⚠️] PERINGATAN: Website Terindikasi Terinfeksi Deface Slot Judi!{RESET}")
            print(f"{PUTIH}    Kata kunci mencurigakan yang ditemukan:{RESET}")
            for item in kata_terdeteksi:
                print(f"    {MERAH}- {item}{RESET}")
        else:
            print(f"{HIJAU}[✅] AMAN: Tidak ditemukan indikasi suntikan kata kunci judi pada halaman ini.{RESET}")

    except requests.exceptions.Timeout:
        print(f"{KUNING}[-] Waktu tunggu habis. Server lambat atau memblokir bot.{RESET}")
    except Exception as e:
        print(f"{MERAH}[-] Gagal melakukan audit halaman: {e}{RESET}")

def main():
    tampilkan_banner()
    print(f"{PUTIH}[ WEB INTEGRITY AUDIT MODE ]{RESET}\n")
    
    target = input(f"{KUNING}Masukkan URL Website (Contoh: ac.id / go.id): {RESET}").strip()
    if target:
        print("==================================================")
        pindai_halaman(target)
        print("==================================================")
    else:
        print(f"{MERAH}[-] URL tidak boleh kosong!{RESET}")

if __name__ == "__main__":
    main()
