#!/bin/bash
# ==========================================
# INSTALLER : SPY-BLUE-SPAM
# BRAND     : SPY-E & 123Tool
# ==========================================

GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}[*] Menyiapkan Lingkungan SPY-BLUE-STORM...${NC}"

if [[ -d /data/data/com.termux ]]; then
    pkg update && pkg upgrade -y
    pkg install python bluez tsu -y
else
    sudo apt-get update
    sudo apt-get install -y python3 bluez bluez-tools
fi

chmod +x spy-blue.py
echo -e "${GREEN}[+] Instalasi Selesai! Jalankan dengan: sudo python3 spy-blue.py${NC}"
