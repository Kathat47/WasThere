#!/usr/bin/env python3

from sys import path
path.append("/media/kiro/154c85ac-9d56-4bea-8a21-20994f9ed585/myland/")
path.append("/media/kiro/154c85ac-9d56-4bea-8a21-20994f9ed585/myland/lib/python3.13/site-packages")

from playwright.sync_api import sync_playwright
from pyfiglet import figlet_format
from termcolor import colored
from random import randint
from string import ascii_letters, digits
from time import sleep
from rich.console import Console
from sys import exit
from datetime import datetime
from os import getcwd
from os.path import exists
from argparse import ArgumentParser

def rg(webname:str,t:str) -> str :

    t = t[0].strip().lower()

    words = f"{ascii_letters}{digits}"

    m = f"{'-'.join(webname.split('/')[2:])}_"

    for x in range(5) :

        m += words[randint(0, len(words)-1)]

    if t == 'i' :

        ext = '.png'

    else :

        ext = '.html'

    return m + ext

print(colored(figlet_format("WasThere"), "magenta"))

print(colored("Medium : https://medium.com/@kathat", "cyan"))

print(colored("GitHub : https://github.com/Kathat47\n", "yellow"))

initx = ArgumentParser(prog=colored("Take Snapshots of Websites in Your Terminal ", "blue"))

initx.add_argument("-u", "--urls", nargs='+', default=False, help="Urls To Take Snapshots From .")

initx.add_argument("-f", "--files", nargs='+', default=False, help="Files of Urls To Take Snapshots From .")

initx.add_argument("-d", "--destination", type=str, default=getcwd()+'/', help="Snapshot Saving Destination .")

initx.add_argument("-s", "--sleep", type=float, default=5.0, help="Sleep Between Every Request .")

parseit = initx.parse_args()

urls = parseit.urls

files = parseit.files

dest = parseit.destination

sleep_time = parseit.sleep

if dest[-1] != '/' :

    dest += '/'

# Checks

rcon = Console()

if not urls and not files :

    rcon.print("[i bold reverse red]- No Provided Urls :[[/i bold reverse red]")

    exit()

if files :

    resources = []

    for file in files :

        if not exists(file) :

            rcon.print(f"[i bold reverse red]- Files Doesn't Exist({files.index(file)+1})[/i bold reverse red] [bold white]:[/bold white] [bold yellow]{file}[/bold yellow]")

            exit()

        with open(file, 'r') as rf :

            resources.extend(rf.read().splitlines())

    if len(resources) == 0 :

        print(colored(f"(-) File(S) Doesn't Have Url Resources At All", "red"))

        exit()

else :

    resources = urls

# Checks

# Info

info = (f"Current Date : {str(datetime.now()).replace(':', '/')}", f"Urls-Resources : {len(resources)}", f"ScreenShot-Dest : {dest}", f"Sleep-Time : {sleep_time:.1f} Sec")

for poi in info :

    p2 = poi.split(':')

    rcon.print(f"[bold yellow]{p2[0]}[/bold yellow] [bold white]:[/bold white] [bold cyan]{p2[1]}[/bold cyan]")

print('\n')

# Info

passed = 0

with sync_playwright() as spoint :

    browser = spoint.chromium.launch(headless=True)

    search = browser.new_page()

    for eurl in resources :

        http = "http://"

        if http not in eurl :

            eurl = http + eurl

        print(colored(f"[*] Taking ScreenShot and Write SourceCode of {eurl}", "cyan"))

        try :

            search.goto(eurl)

            search.screenshot(path=dest+rg(eurl, 'i'))

            code = dest + rg(eurl, 'c')

            with open(code, "a") as writeCode :

                writeCode.write(search.content())

        except Exception as Error :

            print(f"{colored('(-)', on_color='on_red')} : {colored(str(Error).strip(), 'red')}")

        if len(resources) > 1 :



            passed += 1

            print(colored(f"(*) Passed= {passed}, Remain= {len(resources)-passed}", "yellow"))

            if passed != len(resources) - 1 :

                print(colored(f"(*) Sleeping For {sleep_time:.1f} Second", "magenta"))

                sleep(sleep_time)

        print('\n')

    browser.close()
