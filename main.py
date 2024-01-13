import requests
import time 
import random
import threading

def code():
    url = 'https://api.discord.gx.games/v1/direct-fulfillment'
    headers = {
    'authority': 'api.discord.gx.games',
    'accept': '*/*',
    'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/json',
    'origin': 'https://www.opera.com',
    'referer': 'https://www.opera.com/',
    'sec-ch-ua': '"Chromium";v="118", "Opera GX";v="104", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0',
    }

    data = {
    'partnerUserId': '206fc5c0-d22f-4a75-afb3-ce9e84b723a8'
    }

    response = requests.post(url, headers=headers, json=data)

    global link
    link = response.text.split('"')
    link = str(link[3])
    link = "https://discord.com/billing/partner-promotions/1180231712274387115/eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0.." + link
    print(link)
    print("\n")
    with open('links.txt', 'a') as file:
        file.write(link)
        file.write("\n") 
    link = ""
    
    
def func():
    while True:
        try:
            code()
        except:
            print("wait")
            time.sleep(30)
            continue       

func()
