import random
import json
import xml.etree.ElementTree as ET
import requests
from colorama import Fore, init
import os
import threading
screenlock = threading.Semaphore(value=1) 
import sys
import time

loadingtime = time.time()

init()


print(Fore.RED+"""
  _______ _     _       __ 
 |__   __| |   (_)     / _|
    | |  | |__  _  ___| |_ 
    | |  | '_ \| |/ _ \  _|
    | |  | | | | |  __/ |  
    |_|  |_| |_|_|\___|_|  
                           
            By Avian                               
"""+Fore.RESET)

os.system('title Thief - Miner I Hits: 0')

print(Fore.YELLOW+"Loading..."+Fore.RESET)

hits = 0

def mine(threadindex):
    while True:
        id = random.randint(1000000000,9999999999)

        try:
            e = requests.get("https://assetdelivery.roblox.com/v1/assetid/"+str(id)).content

            e = json.loads(e)

            e = e["location"]

            r = requests.get(e)
            tree = ET.fromstring(r.content)
            item=tree[2]
            numeric_filter = filter(str.isdigit, item[0][0][0].text)
            numeric_string = "".join(numeric_filter)
            global hits
            hits = hits + 1
            os.system("title Thief - Miner I Hits: " + str(hits))
            open('hits.txt', 'a').write("https://www.roblox.com/library/"+numeric_string+"\n")
            screenlock.acquire()
            print("[THREAD "+threadindex+"] "+Fore.GREEN+"Something... https://www.roblox.com/library/"+str(id)+Fore.RESET)
            screenlock.release()

        except Exception as e:
            screenlock.acquire()
            print("[THREAD "+threadindex+"] "+Fore.RED+"Nothing... https://www.roblox.com/library/"+str(id)+Fore.RESET)
            screenlock.release()


print(Fore.GREEN+"Loaded! In "+str(time.time() - loadingtime)+ " seconds." + Fore.RESET)
print(Fore.YELLOW + "Press enter to start..." + Fore.RESET,end="")
input()

for i in range(0,50):
    threading.Thread(target=mine,args=(str(i+1),)).start()
