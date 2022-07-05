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

print(menu)

def report():
    global proxies
    while True:
        r = requests.get(f'https://us.tiktok.com/aweme/v1/aweme/feedback/?aid=1988&app_language=en&app_name=tiktok_web&battery_info=0.42&browser_language=en-US&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F103.0.5060.66%20Safari%2F537.36%20Edg%2F103.0.1264.44&channel=tiktok_web&cookie_enabled=true&current_region=US&device_id=7116707009827718698&device_platform=web_pc&focus_state=true&from_page=user&history_len=8&is_fullscreen=false&is_page_visible=true&lang=en&nickname=ben.%20runs12gangddf2&object_id=7116236332540232750&os=windows&owner_id=7116236332540232750&priority_region=NL&reason=9013&referer=https%3A%2F%2Fwww.tiktok.com%2F%40ben.runs12gangg&region=US&report_type=user&reporter_id=7116518794030531630&root_referer=https%3A%2F%2Fwww.tiktok.com%2Flogout%3Fredirect_url%3Dhttps%253A%252F%252Fwww.tiktok.com%252F%2540ztlollollol2doxed&screen_height=864&screen_width=1536&secUid=MS4wLjABAAAA-5y6BCfw4PNw8m9u7L90AfzvbNoIgfoopB2wZSZukVvpRDo0UxiTHQ7EJ5qkNIhv&target=7116236332540232750&tz_name=America%2FNew_York&verifyFp=verify_55f301cb25c403104636169dcceb05e1&webcast_language=en&msToken=Q4zHGi2O2ekK91VlOZzf7q0_6jLvEhiXCl7eONtdUdLDGtGm6GdHrVfyVCSaJIo1EelBB3SwZdGrjhqJRpNUHX6N8L1S8JqKhBqfcss7SVNs_vDaBZ1INHKOQG4D2w==&X-Bogus=DFSzswVuFaTANS8-S1U9GcYklTIk&_signature=_02B4Z6wo000014rzKnwAAIDCVIVy2oUTGa-K8y7AAICH48')
        if r.status_code == 200:
            print(Fore.MAGENTA, r.text)
            print(Colorate.Horizontal(Colors.green_to_red, 'reported that fag!'))
        else:
            print(Colorate.Horizontal(Colors.red_to_white, 'User couldn\'t be reported due to rate limitations'))
while True:
        if threading.active_count() < int(threads):
            threading.Thread(target=report).start() 
