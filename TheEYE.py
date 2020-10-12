import requests
import re
import subprocess
import sys
import colorama
from colorama import Fore

colorama.init()

print("""

by >>>Retr0
                                
           _----------_
        __/     /\     \__
      _/       /  \       \_
     /        / ## \        \     
     \        \ ## /        /
       \__     \  /     __/ 
          \_    \/    _/
            ----------
""")




pattern = r'[{/}/"/]'


def location(ip):
    geo = requests.get(f"http://ip-api.com/json/{ip}")

    firstFormat = re.sub(pattern, "", geo.text)

    secondFormat = re.sub(',', "\n", firstFormat)

    print("\n\n",Fore.GREEN, secondFormat)


try:
    argument = sys.argv[1]
    address = sys.argv[2]

    if argument == "-u":
        ping = str(subprocess.Popen(["nslookup", address], stdout = subprocess.PIPE).stdout.read())
        ipmatch = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", ping)
        print("\n\n ",Fore.GREEN,"[+]", ipmatch[1])
        location(ipmatch[1])

    elif argument == "-i":
        location(address)

except IndexError:
    print("""
Usage:
    
    -u     uses for url address                   TheEYE.py -u www.example.com
           use address without files or folders
    
    -i     uses for ipv4 address                  TheEYE.py -i 0.0.0.0
    ______________________________________________________________

    lat is latitude |
    lon is longitude -

    Made by >>>Retr0
    """)
