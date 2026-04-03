# 🌀 SPY-BLUE-SPAM
> **Advanced Bluetooth Connection Flooding & Security Auditing Tool**

![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Raspberry%20Pi%20%7C%20Termux%20(Root)-blue.svg)
![Brand](https://img.shields.io/badge/Brand-SPY--E%20%26%20123Tool-red.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-green.svg)

**SPY-BLUE-SPAM** adalah framework audit keamanan Bluetooth yang dirancang untuk menguji ketahanan tumpukan protokol (protocol stack) pada perangkat target. Tool ini melakukan simulasi "Connection Flooding" untuk mengukur ambang batas saturasi koneksi pada perangkat IoT, Smartphone, dan Audio Bluetooth.

## 🔥 Fitur Utama
- **Deep Scan:** Mencari perangkat Bluetooth di sekitar dengan identifikasi Nama & MAC.
- **Multi-Threaded Attack:** Melakukan flooding koneksi secara simultan untuk hasil maksimal.
- **Automated Handshake:** Memaksa proses autentikasi secara berulang (Stress Test).
- **Clean UI:** Antarmuka terminal profesional dengan skema warna Cyberpunk.

## 📥 Instalasi

### 🐧 Linux (Kali / Ubuntu / Raspberry Pi)
```bash
git clone https://github.com/123tool/Spy-Bluetooth-Spam.git
cd Spy-Bluetooth-Spam
sudo chmod +x install.sh
sudo ./install.sh
```
### Termux (Root Required)
​Pastikan Bluetooth aktif dan HP sudah di-root
```bash
pkg install python bluez tsu -y
git clone https://github.com/123tool/Spy-Bluetooth-Spam.git
cd Spy-Bluetooth-Spam
sudo python3 spy-blue.py
```
### Cara Penggunaan

**​Jalankan tool dengan akses root: sudo python3 spy-blue.py.
​Tunggu proses scanning selesai.
​Pilih nomor target dari daftar yang muncul.
​Masukkan durasi serangan (dalam detik).
​Gasss! Pantau status serangan di layar.**

### ​⚠️ Disclaimer
​**Tool ini dibuat untuk tujuan Edukasi dan Penetration Testing Legal. Segala bentuk penyalahgunaan di luar tanggung jawab SPY-E & 123Tool.**
