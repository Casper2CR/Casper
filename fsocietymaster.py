import os
import sys
import time
import socket
import subprocess
from datetime import datetime

import sys,time
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10 / 10000)
slowprint('''\033[92m
XX   MMMMMMMMMMMMMMMMss'''                          '''ssMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMyy''                                    ''yyMMMMMMMMMMMM   XX
XX   MMMMMMMMyy''                                            ''yyMMMMMMMM   XX
XX   MMMMMy''                                                    ''yMMMMM   XX
XX   MMMy'                                                          'yMMM   XX
XX   Mh'                                                              'hM   XX
XX   -                                                                  -   XX
XX                                                                          XX
XX   ::                                                                ::   XX
XX   MMhh.        ..hhhhhh..                      ..hhhhhh..        .hhMM   XX
XX   MMMMMh   ..hhMMMMMMMMMMhh.                .hhMMMMMMMMMMhh..   hMMMMM   XX
XX   ---MMM .hMMMMdd:::dMMMMMMMhh..        ..hhMMMMMMMd:::ddMMMMh. MMM---   XX
XX   MMMMMM MMmm''      'mmMMMMMMMMyy.  .yyMMMMMMMMmm'      ''mmMM MMMMMM   XX
XX   ---mMM ''             'mmMMMMMMMM  MMMMMMMMmm'             '' MMm---   XX
XX   yyyym'    .              'mMMMMm'  'mMMMMm'              .    'myyyy   XX
XX   mm''    .y'     ..yyyyy..  ''''      ''''  ..yyyyy..     'y.    ''mm   XX
XX           MN    .sMMMMMMMMMss.   .    .   .ssMMMMMMMMMs.    NM           XX
XX           N`    MMMMMMMMMMMMMN   M    M   NMMMMMMMMMMMMM    `N           XX
XX            +  .sMNNNNNMMMMMN+   `N    N`   +NMMMMMNNNNNMs.  +            XX
XX              o+++     ++++Mo    M      M    oM++++     +++o              XX
XX                                oo      oo                                XX
XX           oM                 oo          oo                 Mo           XX
XX         oMMo                M              M                oMMo         XX
XX       +MMMM                 s              s                 MMMM+       XX
XX      +MMMMM+            +++NNNN+        +NNNN+++            +MMMMM+      XX
XX     +MMMMMMM+       ++NNMMMMMMMMN+    +NMMMMMMMMNN++       +MMMMMMM+     XX
XX     MMMMMMMMMNN+++NNMMMMMMMMMMMMMMNNNNMMMMMMMMMMMMMMNN+++NNMMMMMMMMM     XX
XX     yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy     XX
XX   m  yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy  m   XX
XX   MMm yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy mMM   XX
XX   MMMm .yyMMMMMMMMMMMMMMMM     MMMMMMMMMM     MMMMMMMMMMMMMMMMyy. mMMM   XX
XX   MMMMd   ''''hhhhh       odddo          obbbo        hhhh''''   dMMMM   XX
XX   MMMMMd             'hMMMMMMMMMMddddddMMMMMMMMMMh'             dMMMMM   XX
XX   MMMMMMd              'hMMMMMMMMMMMMMMMMMMMMMMh'              dMMMMMM   XX
XX   MMMMMMM-               ''ddMMMMMMMMMMMMMMdd''               -MMMMMMM   XX
XX   MMMMMMMM                   '::dddddddd::'                   MMMMMMMM   XX
XX   MMMMMMMM-                                                  -MMMMMMMM   XX
XX   MMMMMMMMM                                                  MMMMMMMMM   XX
XX   MMMMMMMMMy                                                yMMMMMMMMM   XX
XX   MMMMMMMMMMy.       SOCIETY IS BORN TO BE F**KED         .yMMMMMMMMMM   XX
XX   MMMMMMMMMMMMy.                                        .yMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMy.                                    .yMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMs.                                .sMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMss.                          .ssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMsss.                        .sssMMMMMMMMMMMMMMMMMM   XX
XX   MMMMMMMMMMMMMMMMMMMMNoo......................ooNMMMMMMMMMMMMMMMMMMMM   XX
''')
(input)

# ---------------------------
# YAVAŞ YAZDIRMA
# ---------------------------
def slow_print(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ---------------------------
# RGB GEÇİŞ
# ---------------------------
def rgb_gradient(text, start_color=(255,0,0), end_color=(0,255,255)):
    result = ""
    length = len(text)
    r1, g1, b1 = start_color
    r2, g2, b2 = end_color
    for i, char in enumerate(text):
        r = int(r1 + (r2 - r1) * i / max(length-1,1))
        g = int(g1 + (g2 - g1) * i / max(length-1,1))
        b = int(b1 + (b2 - b1) * i / max(length-1,1))
        result += f"\033[38;2;{r};{g};{b}m{char}\033[0m"
    return result

# ---------------------------
# LOG KAYDI
# ---------------------------
def log_yaz(mesaj):
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(mesaj + "\n")

# ---------------------------
# BANNER GÖSTERME
# ---------------------------
def show_banner():
    os.system("cls" if os.name=="nt" else "clear")
    banner = """
====================================
     ██████╗ █████╗ ███████╗██████╗ ███████╗██████╗ 
██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗
██║     ███████║███████╗██████╔╝█████╗  ██████╔╝
██║     ██╔══██║╚════██║██╔═══╝ ██╔══╝  ██╔══██╗
╚██████╗██║  ██║███████║██║     ███████╗██║  ██║
 ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                     
====================================
"""
    for line in banner.split("\n"):
        print(rgb_gradient(line, start_color=(255,0,0), end_color=(0,255,255)))
        time.sleep(0.1)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Güncel Tarih ve Saat: \033[93m{now}\033[0m\n")
    time.sleep(0.1)

# ---------------------------
# MENÜ
# ---------------------------
def menu():
    slow_print("1 - URL'den IP bulma ", delay=0.01)
    slow_print("2 - IP ve PORT bağlantı testi", delay=0.01)
    slow_print("3 - DDOS TOOL ÇALIŞTIRMA", delay=0.01)
    slow_print("0 - Çıkış", delay=0.01)

# ---------------------------
# 1 → URL → IP + LOG
# ---------------------------
def url_ip_bul():
    try:
        url = input("\nURL girin (örn: google.com): ").strip()
        if any(c in url for c in "!'^+%&/()=?_*$#{}[]|<>"):
            print("\033[31mGeçersiz karakter!\033[0m")
            return
        ip = socket.gethostbyname(url)
        print(f"IP adresi: \033[92m{ip}\033[0m")
        log_yaz(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] URL sorgusu: {url} → {ip}")
    except Exception:
        print("\033[31mHata: URL çözümlenemedi!\033[0m")

# ---------------------------
# 2 → IP + PORT TESTİ
# ---------------------------
def port_test():
    ip = input("\nIP adresi: ").strip()
    try:
        socket.inet_aton(ip)
    except:
        print("\033[31mGeçersiz IP!\033[0m")
        return
    port = input("Port: ").strip()
    if not port.isdigit():
        print("\033[31mPort sadece sayı olabilir!\033[0m")
        return
    port = int(port)
    s = socket.socket()
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print("\033[92m+ AÇIK\033[0m")
    except:
        print("\033[31m- KAPALI\033[0m")

# ---------------------------
# 3 → Girilen Python dosyası ara ve CMD'de aç
# ---------------------------
def py_dosya_ac(dosya_adi):
    if not dosya_adi.lower().endswith(".py"):
        dosya_adi += ".py"

    arama_yerleri = [
        os.path.join(os.path.expanduser("~"), "Desktop"),
        os.path.join(os.path.expanduser("~"), "Documents")
    ]

    print("\nDosya aranıyor...\n")
    bulunan_yol = None

    for yer in arama_yerleri:
        if os.path.exists(yer):
            for root, dirs, files in os.walk(yer):
                if dosya_adi in files:
                    bulunan_yol = os.path.join(root, dosya_adi)
                    break
            if bulunan_yol:
                break

    if not bulunan_yol:
        print("\033[31mHATA: Dosya bulunamadı!\033[0m")
        print("Aranan yerler: Masaüstü ve Belgeler\n")
        return

    print(f"\033[32mBulundu:\033[0m {bulunan_yol}")
    print("\033[36mCMD üzerinden çalıştırılıyor...\033[0m")
    subprocess.Popen(f'cmd /c python "{bulunan_yol}"', shell=True)
    print("\033[32mDosya başarıyla çalıştırıldı.\033[0m\n")

# ---------------------------
# ANA DÖNGÜ
# ---------------------------
while True:
    show_banner()
    menu()
    secim = input("\nSeçiminiz: ").strip()
    if secim == "1":
        url_ip_bul()
        input("\nDevam etmek için ENTER'a bas...")
    elif secim == "2":
        port_test()
        input("\nDevam etmek için ENTER'a bas...")
    elif secim == "3":
        dosya_adi = input("Python dosyası adı (örn: test.py): ").strip()
        py_dosya_ac(dosya_adi)
        input("\nDevam etmek için ENTER'a bas...")
    elif secim == "0":
        print("Çıkıyor...")
        break
    else:
        print("\033[31mGeçersiz seçim!\033[0m")
        input("Tekrar denemek için ENTER'a bas...")
