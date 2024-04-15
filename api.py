__author__ = "Jatin Tiwari"
__copyright__ = "Copyright (C) 2024"
__license__ = "Public Domain"
__version__ = "1.0"

import threading
import requests
import os
import time
import sys
import webbrowser
from fake_useragent import UserAgent


E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(23.0 / 8000)

to(
    f"""{G}|{C}=============================================={G}|
{G}| Creator     :  @Jatin Tiwari{G}              |
{G}| {Y}Tools      :  Truecaller Call and Sms Api{G}  |
{G}| {PN}Expire     :  LIFETIME {G}                   |
{G}| {W}Link       :  github.com/jatintiwari0 {G} |
{G}|{C}=============================================={G}|"""
)

webbrowser.open("https://github.com/jatintiwari0")

import requests,random
NUMS = '1234567890'
LETTS = 'abcdefghijklmnopqrstuvwxyz'
num = input('[+] 🙂Enter Number With Country Code🙂 : ')
req = requests.post('https://account-asia-south1.truecaller.com/v2/sendOnboardingOtp',headers= {'content-type':'application/json; charset=UTF-8','accept-encoding':'gzip','user-agent':'Truecaller/11.75.5 (Android;10)','clientsecret':'lvc22mp3l1sfv6ujg83rd17btt'},json={'countryCode':'','dialingCode':None,'installationDetails': {'app': {'buildVersion':5,'majorVersion':11,'minorVersion':75,'store':'GOOGLE_PLAY'},'device': {'deviceId':''.join(random.choices(NUMS+LETTS, k=16)),'language':'en','manufacturer':'Xiaomi','mobileServices':['GMS'],'model':'M2010J19SG','osName':'Android','osVersion':'10','simSerials':[''.join(random.choices(NUMS, k=19)), ''.join(random.choices(NUMS, k=20))]},'language':'en','sims': [{'imsi':''.join(random.choices(NUMS, k=15)),'mcc':'413','mnc':'2','operator':None}]},'phoneNumber':num,'region':'region-2','sequenceNo':random.randint(1,2)})
if req.json()['status'] == 1 or req.json()['status'] == 9:
 print(req.json()['message'])
else:
 print(req.json()['message'])
