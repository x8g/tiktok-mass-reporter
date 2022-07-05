import requests, time, sys, os, threading
from colorama import Fore
from pystyle import *
from itertools import cycle
from tkinter import Tk
from tkinter.filedialog import askopenfilename

menu = """╦═╗┌─┐┌─┐┌─┐┬─┐┌┬┐
╠╦╝├┤ ├─┘│ │├┬┘ │ 
╩╚═└─┘┴  └─┘┴└─ ┴ """
threads = 500
proxiesloaded = False
proxies = []
proxy = []
os.system(f'title tiktok reporter ^| github/x8g')
Anime.Fade(Center.Center(menu), Colors.blue_to_purple, Colorate.Vertical, interval=0.05, time=5)
Anime.Fade(Center.Center("Tiktok Mass Reporter"), Colors.blue_to_purple, Colorate.Vertical, interval=0.05, time=2)
Anime.Fade(Center.Center("By zt#7380"), Colors.blue_to_purple, Colorate.Vertical, interval=0.01, time=3)
Anime.Fade(Center.Center("sends reports"), Colors.blue_to_purple, Colorate.Vertical, interval=0.05, time=5)

f = open('proxies.txt','wb')
proxytype = 'http'
if proxytype not in ['http', 'https', 'socks4', 'socks5']:
    print(f'Invalid Choice.')
    time.sleep(0)
r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxytype}&timeout=10000&country=all")
f.write(r1.content)
f.close()

print(Colorate.Horizontal(Colors.blue_to_purple, 'Successfully scraped proxies.'))

def load_proxies():
    global filename
    if not os.path.exists(filename):
        print("File Error")
        time.sleep(10)
        sys.exit()
    with open(filename, "r", encoding = "UTF-8") as f:
        for line in f.readlines():
            line = line.replace("\n", "")
            proxies.append(line)
            proxiesloaded = True
        if not len(proxies):
            print("No proxies in file")
            time.sleep(10)
            sys.exit()

option = int(input(Colorate.Horizontal(Colors.blue_to_purple, "(1) proxies | (2) proxyless ")))
if option == 1:
    if os.name == 'nt':
        print(Colorate.Horizontal(Colors.blue_to_purple,"Please select your proxies file"))
        Tk().withdraw()
        filename = askopenfilename()
        #print(filename)
    else:
        filename = input("Please enter where your proxies are stored. (eg etc/home/proxies.txt): ")
    load_proxies()


def report():
    global proxies
    while True:
        r = requests.get(f'your url')
        if r.status_code == 200:
            print(Fore.MAGENTA, r.text)
            print(Colorate.Horizontal(Colors.green_to_red, 'reported that fag!'))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, 'User couldn\'t be reported due to rate limitations'))
while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=report).start() 
