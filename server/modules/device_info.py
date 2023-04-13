import requests

def sendrequest(url,data):
    r = requests.post(url,data)

sendrequest(URL,DATA)