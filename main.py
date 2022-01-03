import random
import string
import time
import discord
import urllib.request
import requests
from colorama import Fore


from aiohttp.helpers import proxies_from_env
print(f"{Fore.LIGHTYELLOW_EX}----------------------------------------------------------------------------------------------------------------------")
print(
    "$$$$$$$$\                            $$\      $$\                                         $$\   $$\           $$\       ")
print(
    "$$  _____|                           $$$\    $$$ |                                        $$ |  $$ |          $$ |      ")
print(
    "$$ |    $$$$$$\   $$$$$$\   $$$$$$\  $$$$\  $$$$ | $$$$$$\  $$$$$$$\   $$$$$$\  $$\   $$\ $$ |  $$ |$$\   $$\ $$$$$$$\  ")
print(
    "$$$$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$\$$\$$ $$ |$$  __$$\ $$  __$$\ $$  __$$\ $$ |  $$ |$$$$$$$$ |$$ |  $$ |$$  __$$\ ")
print(
    "$$  __|$$ |  \__|$$$$$$$$ |$$$$$$$$ |$$ \$$$  $$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$ |  $$ |")
print(
    "$$ |   $$ |      $$   ____|$$   ____|$$ |\$  /$$ |$$ |  $$ |$$ |  $$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |")
print(
    "$$ |   $$ |      \$$$$$$$\ \$$$$$$$\ $$ | \_/ $$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\ \$$$$$$$ |$$ |  $$ |\$$$$$$  |$$$$$$$  |")
print(
    "\__|   \__|       \_______| \_______|\__|     \__| \______/ \__|  \__| \_______| \____$$ |\__|  \__| \______/ \_______/ ")
print(
    "                                                                                $$\   $$ |                              ")
print(
    "                                                                                 \$$$$$$ |                              ")
print(
    "                                                                                 \______/                               ")
print(f"{Fore.LIGHTYELLOW_EX}----------------------------------------------------------------------------------------------------------------------")

print(f"{Fore.WHITE} {Fore.CYAN}Dicord Invite Gen Made By FreeMoneyHub & Tadd#0874")
print("")
num = int(input(f'{Fore.RED} How Many Invites Do You Want To Make?  : '))

with open("invites.txt", "w", encoding='utf-8') as file:
    print("Generating Invites Now")

    for i in range(num):
        code = "".join(random.choices(
            string.ascii_uppercase + string.digits + string.ascii_lowercase,
            k=8
        ))

        file.write(f"{code}\n")

        print(f"Generated {num} invites\n")

with open("invites.txt") as file:
    with open("valid.txt", "a") as valid:
        with open("proxy.txt", "r") as proxy:
            proxies = proxy.readlines()
            i=-1
            for line in file.readlines():
                invite = line.strip("\n")
                url = f'https://discord.com/api/v6/invites/{invite}?with_counts=true'
                user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
                headers = {'User-Agent': user_agent, }
                request = urllib.request.Request(url, None, headers)
                i+=1
                try:
                    proxiee = proxies[i % len(proxies)]
                    print(f"{Fore.RED}Using Proxy - {Fore.WHITE}{proxiee}")
                    proxy_support = urllib.request.ProxyHandler({'http': f'https://{proxiee}'})
                    opener = urllib.request.build_opener(proxy_support)
                    urllib.request.install_opener(opener)

                    response = urllib.request.urlopen(request)
                except:
                    print(f"{Fore.RED}{invite} is Invalid")
                    continue
                data = response.read()
                time.sleep(3)
                print(f'{proxiee}')
                valid.write(f"discord.com/{invite}")
                print(f'{Fore.GREEN} {invite} is valid')