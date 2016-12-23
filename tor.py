#!/usr/bin/python3

"""
sudo apt-get install tor privoxy

sudo vi /etc/tor/torrc
MaxCircuitDirtiness 300

sudo /etc/init.d/tor restart

sudo /etc/privoxy/config
listen-address 127.0.0.1:8118
forward-socks5 / localhost:9050 .

sudo /etc/init.d/privoxy restart

sudo /etc/init.d/tor status
sudo /etc/init.d/privoxy status

"""

import requests
import time

proxies = {"http": "127.0.0.1:8118", "https": "127.0.0.1:8118"}
i = 1
ips = []

while True:
    response = requests.get("http://icanhazip.com/", proxies=proxies)
    if response.text.replace('\n', '') not in ips:
        ips.append(response.text.replace('\n', ''))
    print(i, ' - ', len(ips), ' - ', response.status_code, ' - ', ips)
    time.sleep(3)
    i += 1