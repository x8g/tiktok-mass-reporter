import httpx, time, os, threading
from colorama import Fore
from pystyle import *

threads = 50

menu = """╦═╗┌─┐┌─┐┌─┐┬─┐┌┬┐
╠╦╝├┤ ├─┘│ │├┬┘ │ 
╩╚═└─┘┴  └─┘┴└─ ┴ """
os.system(f'title tiktok reporter ^| github/x8g')
Anime.Fade(Center.Center(menu), Colors.blue_to_purple, Colorate.Vertical, interval=0.05, time=5)


url = input(Colorate.Horizontal(Colors.blue_to_purple, 'Url?: '))
def report():
    while True:
        r = httpx.get(url)
        if "Thanks for your feedback" in r.text:
            print(Colorate.Horizontal(Colors.green_to_red, f'reported that fag!'))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, f'User couldn\'t be reported due to rate limitations'))
while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=report).start() 
