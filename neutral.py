from os import listdir
from os.path import isfile,join
from os import walk
import vlc
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget ,QVBoxLayout
import os
mypath="E:\\songs\\neutral\\"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
f = []
f2=[]
for (dirpath, dirnames, filenames) in walk(mypath):
	f.extend(filenames)
	break
for i in f:
	if i.endswith(".mp3") or i.endswith(".flac") or i.endswith(".m4a") or i.endswith(".wav") or i.endswith(".wma"):
		f2.append(i)
count=0

player=vlc.MediaPlayer("E:\\songs\\neutral\\"+str(f2[count]))
def button_pressed():
	# player=vlc.MediaPlayer("B:\\BAPU\\01) I Ain't No Joke.mp3")
	global count
	global player
	player.play()
def button2_pressed():
	global player
	player.pause()
def nextS():
	global count
	# count+=1
	global player 
	player.stop()
	count+=1
	player=vlc.MediaPlayer("E:\\songs\\neutral\\"+str(f2[count]))
	player.play()
	# player=vlc.MediaPlayer("B:\\BAPU\\"+str(f.pop()))
def prevS():
	global count
	global player 
	player.stop()
	count-=1
	player=vlc.MediaPlayer("E:\\songs\\neutral\\"+str(f2[count]))
	player.play()
# def cam():
# 	player.stop()
# 	import os
# 	os.popen("python real_time_video.py")


# while True:
#     pass

app = QApplication([])
win = QMainWindow()
central_widget = QWidget()
button = QPushButton('PLAY')
button.clicked.connect(button_pressed)
button2=QPushButton('PAUSE')
button2.clicked.connect(button2_pressed)
button3=QPushButton("NEXT")
button3.clicked.connect(nextS)
button4=QPushButton('PREV')
button4.clicked.connect(prevS)
# button5=QPushButton('camera')
# button5.clicked.connect(cam)
layout = QVBoxLayout(central_widget)
layout.addWidget(button)
layout.addWidget(button2)
layout.addWidget(button3)
layout.addWidget(button4)
# layout.addWidget(button5)
win.setCentralWidget(central_widget)
# print(vlc.__version__)
player.play()

# win.setCentralWidget(button)
win.show()
app.exit(app.exec_())
# print(f2)


