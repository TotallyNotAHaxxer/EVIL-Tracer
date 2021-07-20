#ip tracker v0.5 provider by Anonymous Pro
#Author Mahfuzur Rahman
#python script
#Follw Me
#visit: www.anonymousproo.com
#github: https://github.com/anonymousproo
#youtube: https://www.youtube.com/anonymouspro1
#Facebook: https://m.facebook.com/anonymousproo1
import os
import requests
import json
import colorama 
import urllib
from urllib.request import urlopen as open
import webbrowser
import os 
from colorama import Fore, Back, Style 
import requests 
from termcolor import colored
import time
from requests import get 
import sys 
import pyfiglet
import sys
import socket
from datetime import datetime
os.system('clear')

#colors 
# RED ++++ print(\033[31m)


print(Fore.RED+"                $$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  ")
print(Fore.MAGENTA+"		\_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\  ")
print(Fore.RED+"  		  $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ | ")
print(Fore.MAGENTA+"  		  $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  | ")
print(Fore.RED+"  		  $$ |  $$  ____/          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$<  ")
print(Fore.MAGENTA+" 		  $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ | ") 
print(Fore.RED+"		$$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ | ")
print(Fore.MAGENTA+"		\______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__| ")

#\033[1;32m = cyan 
print(Fore.CYAN+"|======================================================================================================|")
print(Fore.BLUE+"|Github: ArkAngeL43 | https://github.com/ArkAngeL43                                                    |")
print(Fore.MAGENTA+"|instagram ark_angel6                                                                                  |")
print(Fore.BLUE+"|NOTES:::::: if you want to exit the script just type exit, its easier than ctrl+c+d                   |")
print(Fore.CYAN+"|======================================================================================================|")

#LOOP WITHOUT ELSE +++ while True:
global ip
ip = input("\033[1;36mEnter Your Target IP: \033[1;36m")

if 'Exit' in ip:
          os.system(' clear ')
          time.sleep(1)
          print(" [+] Thanks for stopping by [+] ")
          print(" [=] Have a good one :D     [=]")
          time.sleep(2)
          sys.exit()

elif 'exit' in ip:
            os.system(' clear ')
            time.sleep(1)
            print(" [+] Thanks for stopping by [+] ")
            print(" [=] Have a good one :D     [=]")
            time.sleep(2)
            sys.exit()

url = "http://ip-api.com/json/"
response = open(url + ip)
data = response.read()
values = json.loads(data)
status = values['status']
success = "success"
lat = str(values['lat'])
lon = str(values['lon'])
a = lat + ","
b = lon + "/"
c = b + "data=!3m1!1e3?hl=en"
location = a + c

time.sleep(1)
os.system(' clear ')
os.system(' mpg123 loc.mp3 ')
os.system(' clear ')
time.sleep(1)
print(Fore.RED+"                $$$$$$\ $$$$$$$\        $$$$$$$$\ $$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$$$\ $$$$$$$\  ")
time.sleep(0.1)
print(Fore.RED+"		\_$$  _|$$  __$$\       \__$$  __|$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  _____|$$  __$$\  ")
time.sleep(0.1)
print(Fore.RED+"  		  $$ |  $$ |  $$ |         $$ |   $$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ |      $$ |  $$ | ")
time.sleep(0.1)
print(Fore.RED+"  		  $$ |  $$$$$$$  |         $$ |   $$$$$$$  |$$$$$$$$ |$$ |      $$$$$  /  $$$$$\    $$$$$$$  | ")
time.sleep(0.1)
print(Fore.RED+"  		  $$ |  $$  ____/          $$ |   $$  __$$< $$  __$$ |$$ |      $$  $$<   $$  __|   $$  __$$<  ")
time.sleep(0.1)
print(Fore.RED+" 		  $$ |  $$ |               $$ |   $$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$ |      $$ |  $$ | ") 
time.sleep(0.1)
print(Fore.RED+"		$$$$$$\ $$ |               $$ |   $$ |  $$ |$$ |  $$ |\$$$$$$  |$$ | \$$\ $$$$$$$$\ $$ |  $$ | ")
time.sleep(0.1)
print(Fore.RED+"		\______|\__|               \__|   \__|  \__|\__|  \__| \______/ \__|  \__|\________|\__|  \__| ")
time.sleep(0.1)
print("---------------------------------")
time.sleep(0.1)
print(" [=] IP: " + values['query']        )
time.sleep(0.1)
print(" [=] Status: " + values['status']   )
time.sleep(0.1)
print(" [=] city: " + values['city']       )
time.sleep(0.1)
print(" [=] ISP: " + values['isp']         )
time.sleep(0.1)
print(" [=] latitude: " + lat              )
time.sleep(0.1)
print(" [=] longitude: " + lon             )
time.sleep(0.1)
print(" [=] country: " + values['country'] )
time.sleep(0.1)
print(" [=] region: " + values['regionName'])
time.sleep(0.1)
print(" [=] city: " + values['city']       )
time.sleep(0.1)
print(" [=] zip: " + values['zip']         )
time.sleep(0.1)
print(" [=] AS: " + values['as']           )
time.sleep(0.1)
print("---------------------------------")
time.sleep(1)
print(" [+] opening location LINK [+] ")
maps = "https://www.google.com/maps/search/"
webbrowser.open(maps + location)
print(" [-] would you like to scan the ports of this IP? ")
time.sleep(2)
B = str(input(" ┌─[User7]-[~/main/IPTracer]──╼"))
time.sleep(1)

if 'yes' in B:
         time.sleep(1)
         print(" [+] cleaning up [+] ")
         time.sleep(1)
         os.system(' clear ')
         os.system(f' python3 Scan.py {ip} ')

elif 'no' in B:
          os.system(' clear ')
          print(" [-] cleaning up [-] ")
          time.sleep(1)
          sys.exit()

elif 'No' in B:
          os.system(' clear ')
          pritn(" [-] cleaning up [-] ")
          time.sleep(1)
          sys.exit()

elif 'Yes' in B:
           time.sleep(1)
           print(" [+] cleaning up [+] ")
           time.sleep(1)
           os.system(' clear ')
           os.system(f' python3 Scan.py {ip} ')            


elif 'sure' in B:
            time.sleep(1)
            print(" [+] cleaning up [+] ")
            time.sleep(1)
            os.system(' clear ')
            os.system(f' python3 Scan.py {ip} ')      

elif 'YE' in B:
          time.sleep(1)
          print(" [+] cleaning up [+] ")
          time.sleep(1)
          os.system(' clear ')
          os.system(f' python3 Scan.py {ip} ')      

elif 'YEE' in B:
           time.sleep(1)
           print(" [+] cleaning up [+] ")
           time.sleep(1)
           os.system(' clear ')
           os.system(f' python3 Scan.py {ip} ')      

#track = get(f'https://ipapi.co/{ip}/json/')
#print(track.json())
