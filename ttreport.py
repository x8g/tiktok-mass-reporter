import requests, time, sys, os, threading
from colorama import Fore
from pystyle import *
from itertools import cycle
from tkinter import Tk
from tkinter.filedialog import askopenfilename

menu = """╦═╗┌─┐┌─┐┌─┐┬─┐┌┬┐
╠╦╝├┤ ├─┘│ │├┬┘ │ 
╩╚═└─┘┴  └─┘┴└─ ┴ """
os.system(f'title tiktok reporter ^| github/x8g')
Anime.Fade(Center.Center(menu), Colors.blue_to_purple, Colorate.Vertical, interval=0.05, time=5)
Anime.Fade(Center.Center("Tiktok Mass Reporter"), Colors.blue_to_purple, Colorate.Vertical, interval=0.05, time=2)
Anime.Fade(Center.Center("By zt#7380"), Colors.blue_to_purple, Colorate.Vertical, interval=0.01, time=3)
Anime.Fade(Center.Center("sends reports"), Colors.blue_to_purple, Colorate.Vertical, interval=0.05, time=2)
# ---
threads = 50
# ---
f = open('proxies.txt','wb')
proxytype = 'http'
if proxytype not in ['http', 'https', 'socks4', 'socks5']:
    print(f'Invalid Choice.')
    time.sleep(0)
r1 = requests.get(f"https://api.proxyscrape.com/v2/?request=getproxies&protocol={proxytype}&timeout=10000&country=all")
f.write(r1.content)
f.close()
# --- proxy scraping feel free to add proxy usage!
print(Colorate.Horizontal(Colors.blue_to_purple, 'Successfully scraped proxies.'))
url = input(Colorate.Horizontal(Colors.blue_to_purple, 'Url?: '))
def report():
    while True:
        r = requests.get(url)
        if "Thanks for your feedback" in r.text:
            print(Colorate.Horizontal(Colors.green_to_red, f'reported that fag!'))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, f'User couldn\'t be reported due to rate limitations'))
while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=report).start() 
