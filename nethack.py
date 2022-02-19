from base64 import decode
from functools import cache
from posixpath import split
import os
import random, math
import time
import subprocess
from subprocess import *
from unittest import result
from pkg_resources import split_sections
import geocoder
import scapy.all as scapy
import re
import threading


os.system('cls')
aninames = ['/','-', "\ ", '|']
aniframes = 0 


for i in range(12):
        if aniframes == 4:
                aniframes = 0
        print("...", aninames[aniframes])
        time.sleep(0.1)
        aniframes = aniframes + 1
        os.system('cls')


time.sleep(0.5)
lineskip = ("-----------------------------")
print(lineskip, """
     ___   _      _   _   _            _    
    / / \ | | ___| |_| | | | __ _  ___| | __
   / /|  \| |/ _ \ __| |_| |/ _` |/ __| |/ /
  / / | |\  |  __/ |_|  _  | (_| | (__|   < 
 /_/  |_| \_|\___|\__|_| |_|\__,_|\___|_|\_\
""")
print(lineskip)
print("Version 1.7")
print("Copyright 2021-2022, OjanRN/M3D4NG")
print("\n")

def start():

    while True:
        print("")
        print("|")
        usercm1 = input("L@-")
        if usercm1 == "/h":
            print("\n")
            print(lineskip)
            print("Main Commands")
            print(lineskip)
            print(f"get profiles = Scan the network profiles on the current pc")
            print(f"get key = View the password/key of the network profile")
            print(f"get ipc = Get current host's IPv4 Address from ipconfig in cmd")
            print(f"get ipw = Get the IP Adress of a WWW link(example:google.com)")
            print(f"locate me = Get current host's IP Address")
            print(f"locate ip = Locate an IP Adress")
            print(f"connect = Connect to a wifi by using a registered profile")
            print(f"dconnect = Disconnect current connected wifi")
            print(lineskip)
            print("Red Zone:")
            print(f"WARNING!,use these command at your own risk")
            print(lineskip)
            print(f"changehostpass = Change host's password")
            print(f"ping = Ping/Send package to an IP Adress")
            print(f"getlocalsip = Get IP Adress of your local network")
            print(lineskip)
            print("Program Commands")
            print(lineskip)
            print(f"/matrix = Create a hacker style matrix of one and zeros")
            print(f"/credits = Credits")
            print(f"/exit = Exit the program")
            print(f"/h = List commands")
            print(f"/clear = Clears the command line")
            print("\n")
            continue
        elif usercm1 == "get profiles":
            p1 = subprocess.check_output(['netsh', 'wlan', 'show', 'profile'], shell=True).decode('utf=8').split('\n')
            p1 = [i.split(":")[1][1:-1] for i in p1 if "All User Profile" in i]
            print("\n")
            print("Profiles Available:", p1)
            print("\n")
            continue
        elif usercm1 == "get key":
                print("\n")
                print("|")
                netName = input("L@-")
                keycommand = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', netName, 'key=clear'], shell=True).decode('utf-8').split('\n')
                keycommand = [i.split(":")[1][1:-1] for i in keycommand if "Key Content" in i]
                print("\n")
                print("Key Is",  keycommand)
                print("\n")
                print("\n")
                continue
        elif usercm1 == "connect":
                print("\n")
                print("|")
                rqNetName = input("L@-")
                cncommand = subprocess.run(['netsh', 'wlan', 'connect', rqNetName], shell=True)
                print(cncommand.stdout)
                continue
        elif usercm1 == "dconnect":
                print("\n")
                dcncommand = subprocess.run(['netsh', 'wlan', 'disconnect'], shell=True)
                print(dcncommand.stdout)
                print("Disconnected this pc from wifi")
                continue
        elif usercm1 == "get ipc":
                print("\n")
                ipcommand = subprocess.check_output(['ipconfig']).decode('utf-8').split("\n")
                ipcommand = [i.split(":")[1][1:-1] for i in ipcommand if "IPv4 Address. . . . . . . . . . ." in i]
                ipcommand2 = geocoder.ip("me")
                print("current IPv4 Adress:", ipcommand)
                print("GEOCODER IP")
                print(lineskip)
                print(ipcommand2.latlng)
                print(ipcommand2.city)
                print(lineskip)
                print("\n")
                continue
        elif usercm1 =="ping":
                print("\n")
                print("|")
                pingad = input("L@-")
                pingcommand = subprocess.run(['ping','-f', pingad])
                print(pingcommand.stdout)
                print("Pinging")
                continue
        elif usercm1 =="changepass":
                print("\n")
                print("|")
                userinp = input("L@-")
                passinp = input("L@-")
                netusercmd = subprocess.run(['net', 'user', userinp, passinp ])
                print(netusercmd)
                continue
        elif usercm1 == "get ipw":
                print("\n")
                print("|")
                nspinp = input("L@-")
                nspcmd = subprocess.run(['nslookup', nspinp], shell=True)
                print(nspcmd.stdout)
                continue
        elif usercm1 == "getlocalsip":
                print("\n")
                ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
                while True:
                        while True:
                                print("|")
                                ip_add_range_entered = input("L@- ")
                                if ip_add_range_pattern.search(ip_add_range_entered):
                                        print(f"{ip_add_range_entered} is a valid ip address range")
                                        arp_result = scapy.arping(ip_add_range_entered)
                                        break
        elif usercm1 == "locate me":
                print("\n")
                ip = geocoder.ip("me")
                print(lineskip)
                print(ip.ip)
                print(ip)
                print(lineskip)
                continue
        elif usercm1 == "locate ip":
                print("\n")
                print("|")
                location = input("L@-")
                locationdata = geocoder.ip(location)
                print(lineskip)
                print(locationdata.latlng)
                print(locationdata.city)
                print(lineskip)
                continue
        elif usercm1 == "/matrix":
                print("animation starting...,this is a while loop,meaning it won't stop until you close the application")
                time.sleep(5)
                digits = "01"
                matrixout = ""
                while True:
                        matrixout += digits[math.floor(random.random() * 2)]
                        print(matrixout)
        elif usercm1 == "/credits":
                print("\n")
                print(lineskip)
                print("Tools Used:")
                print("VSCode - Text Editor")
                print("PyInstaller - py to exe converter")
                print("Coded in Python 3.9")
                print(lineskip)
                print("Icon Used:")
                print("Icon by Freepik:Flaticon Link \/")
                print("https://www.flaticon.com/free-icons/security Security icons created by Freepik - Flaticon")
                print(lineskip)
                print("Created By:OjanRN")
                print("Github \/")
                print("https://github.com/OjanRN")
                print(lineskip)
                print("\n")
        elif usercm1 == "/clear":
                os.system('cls')
                print(lineskip, """
     ___   _      _   _   _            _    
    / / \ | | ___| |_| | | | __ _  ___| | __
   / /|  \| |/ _ \ __| |_| |/ _` |/ __| |/ /
  / / | |\  |  __/ |_|  _  | (_| | (__|   < 
 /_/  |_| \_|\___|\__|_| |_|\__,_|\___|_|\_\
                """)
                print(lineskip)
                print("Version 1.7")
                print("Copyright 2021-2022, OjanRN/M3D4NG")
                print("\n")
                continue
        elif usercm1 == "/exit":
                print("exiting program...")
                break #
        else:
            continue
start()
