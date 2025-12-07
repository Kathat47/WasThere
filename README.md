# WasThere

WasThere is a *CLI-Tool* That Automates Visiting a Ton of Websites and Take a ScreenShots From Them & Saving the Source Code of Each Page in the Same Time, We as WebPentester If We Did a Dir-Discovery and Found A lot of Directories Or We Have A Lot of WebPages to Visit and Take a Look of it ,It's a Big **Time-Consuming** Process .

### Installation :

After You Cloned the Repo :

```bash
git clone https://github.com/Kathat47/WasThere
```

Install Dependencies :

```bash
sh install.sh
```

Run The Tool :

```bash
chmod +x WasThere.py
./WasThere.py -h
```

```
__        __       _____ _                   
\ \      / /_ _ __|_   _| |__   ___ _ __ ___ 
 \ \ /\ / / _` / __|| | | '_ \ / _ \ '__/ _ \
  \ V  V / (_| \__ \| | | | | |  __/ | |  __/
   \_/\_/ \__,_|___/|_| |_| |_|\___|_|  \___|
                                             

Medium : https://medium.com/@kathat
GitHub : https://github.com/Kathat47

usage: Take Snapshots of Websites in Your Terminal  [-h] [-u URLS [URLS ...]]
                                                             [-f FILES [FILES ...]] [-d DESTINATION]

options:
  -h, --help            show this help message and exit
  -u, --urls URLS [URLS ...]
                        Urls To Take Snapshots From .
  -f, --files FILES [FILES ...]
                        Files of Urls To Take Snapshots From .
  -d, --destination DESTINATION
                        Snapshot Saving Destination .
```

### Explaining Arguments :

-u : Url(S) That The Shell Browser Will Go To and Take Snapshots From, -u 'example.com' '....'

-f : File(S) That Have Urls on It The Script Will Take Urls Line By Line and Visit it All, -f '/home/user/urls_1.txt' '/home/user/urls_2.txt'

-d : the Destination Directory the Results Will Be Saved Inside 
