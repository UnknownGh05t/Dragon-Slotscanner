import os
import sys
import html
import urllib.parse
import urllib.request
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
    banner = f"""
{CYAN} ____ ___ _   _  ____   ____   ___  ____  _  __ 

| __ )_ _| \\ | |/ ___| |  _ \\ / _ \\|  _ \\| |/ / 
|  _ \\| ||  \\| | |  _  | | | | | | | |_) | ' /  
| |_) | || |\\  | |_| | | |_| | |_| |  _ <| . \\  
|____/___|_| \\_|\\____| |____/ \\___/|_| \\_\\_|\\_\\ {RESET}
==================================================
{HIJAU}Author : UnknownGh05t
Team   : LulzGhost Team{RESET}
==================================================
"""
    print(banner)

def cari_bing_bs4(query):
    params = {'q': query}
    query_encoded = urllib.parse.urlencode(params)
    url_lengkap = f"https://bing.com?{query_encoded}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9"
    }
    
    try:
        req = urllib.request.Request(url_lengkap, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            html_content = response.read()
            
            soup = BeautifulSoup(html_content, 'html.parser')
            urls_valid = []
            
            for h2_tag in soup.find_all('h2'):
                a_tag = h2_tag.find('a')
                if a_tag and a_tag.get('href'):
                    link = a_tag.get('href')
                    
                    if link.startswith('http') and not any(x in link for x in ["bing.com", "microsoft", "msn", "live", "go.microsoft"]):
                        if link not in urls_valid:
                            urls_valid.append(link)
                            
            return urls_valid
            
    except Exception as e:
        print(f"{MERAH}[-] Eror Jaringan: {e}{RESET}")
        return []

def main():
    tampilkan_banner()
    
    # Daftar Dork WebDAV
    daftar_dork = [
        'intitle:"Directory Listing For /" inurl:webdav',
        'intitle:"Directory Listing For /" inurl:webdav tomcat',
        'inurl:/webdav/config/',
        'inurl:webdav "Index of /"',
        'ext:txt inurl:webdav'
    ]
    
    print(f"{PUTIH}[ AUTO DORK BING BS4 v5.2 ]{RESET}\n")
    
    # PERBAIKAN: Menampilkan dork berurutan ke bawah agar muat di semua ukuran layar HP
    for i, dork in enumerate(daftar_dork, 1):
        print(f"{CYAN}[{i}]{RESET} {dork}")
        
    print(f"{CYAN}[6]{RESET} Masukkan Dork Kustom")
    print(f"{MERAH}[0]{RESET} Keluar")
    print("==================================================")
    
    pilihan = input(f"{KUNING}Pilih nomor dork (0-6): {RESET}").strip()
    
    if pilihan == "0":
        print(f"\n{HIJAU}Sampai jumpa!{RESET}\n")
        sys.exit()
        
    dork_terpilih = ""
    if pilihan in ["1", "2", "3", "4", "5"]:
        dork_terpilih = daftar_dork[int(pilihan) - 1]
    elif pilihan == "6":
        dork_terpilih = input(f"\n{KUNING}Masukkan dork kustom: {RESET}").strip()
    else:
        print(f"{MERAH}[-] Pilihan tidak valid.{RESET}")
        return

    if dork_terpilih:
        print(f"\n{BIRU}[*] Memulai pencarian dengan BeautifulSoup...{RESET}\n")
        hasil = cari_bing_bs4(dork_terpilih)
        file_output = "listdork.txt"
        
        if hasil:
            with open(file_output, "a") as f:
                for url in hasil:
                    print(f"{HIJAU}[+] Saved:{RESET} {url}")
                    f.write(f"{url}\n")
            print("==================================================")
            print(f"{HIJAU}[+] SELESAI! Berhasil menyimpan {len(hasil)} web ke '{file_output}'.{RESET}")
            print(f"{PUTIH}[*] Ketik 'mv {file_output} list.txt' untuk dipakai di script massal.{RESET}")
            print("==================================================")
        else:
            print(f"{MERAH}[-] Tidak ada hasil web target yang didapat dari Bing.{RESET}")

if __name__ == "__main__":
    main()
