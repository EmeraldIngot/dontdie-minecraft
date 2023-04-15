import os, time
from os import path
import sys
import platform
from PyQt6 import QtWidgets, uic, QtCore
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow
from mb1 import Ui_Form as MB1_Form
from mb2 import Ui_Form as MB2_Form
from dontdieui import Ui_MainWindow as DontDie_MainWindow
import shutil
import multiprocess

if getattr(sys, "frozen", False):
    multiprocess.freeze_support()

global playername
global close
close=0
global iconpath
global process
global mainapp
mainapp = QApplication(sys.argv)

osplatform = platform.system()
user = os.getlogin()
if osplatform == "Linux":
    if getattr(sys, 'frozen', False):
        iconpath=os.path.join(sys._MEIPASS, "dontdie.ico")
    else:
        iconpath="dontdie.ico" 

if osplatform == "Darwin":
    if getattr(sys, 'frozen', False):
        iconpath=os.path.join(sys._MEIPASS, "dontdie.ico")
    else:
        iconpath="dontdie.icns"

if osplatform == "Windows":
    if getattr(sys, 'frozen', False):
        iconpath=os.path.join(sys._MEIPASS, "dontdie.ico")
    else:
        iconpath="dontdie.ico"




class MB1(QtWidgets.QWidget, MB1_Form):
    def __init__(self):

        super(MB1, self).__init__()
    # uic.loadUi("mb1.ui", self)
        self.setupUi(self)
        self.setWindowIcon(QIcon(iconpath))
        def closefunction():
            global close
            close=1
            self.close()
        def endfunction():
            global close
            if close != 1:
                print("abort")
                sys.exit()
        self.buttonBox.accepted.connect(closefunction)
        self.buttonBox.rejected.connect(endfunction)
        app.aboutToQuit.connect(endfunction)

app = mainapp
window = MB1()
window.show()
UIWindow = MB1()
app.exec()


class MB2(QtWidgets.QWidget, MB2_Form):
    global close
    close=0
    def __init__(self):
        super(MB2, self).__init__()
    # uic.loadUi("mb2.ui", self)
        self.setupUi(self)
        self.setWindowIcon(QIcon(iconpath))
        def closefunction():
            global close
            close=1
            self.close()
        def endfunction():
            global close
            if close != 1:
                print("abort")
                sys.exit()
        self.buttonBox.accepted.connect(closefunction)
        self.buttonBox.rejected.connect(endfunction)
        app2.aboutToQuit.connect(endfunction)



app2 = mainapp
window = MB2()
window.show()
UIWindow = MB2()
app2.exec()
    
close = 0


def runlistener(finaldeathlist,version,playername):
    
    osplatform = platform.system()
    user = os.getlogin()

    if osplatform == "Linux":
        logpath = path.expandvars(os.path.expanduser('~') + '/.minecraft/logs/latest.log')
        crashcmd = "sudo shutdown -h now"
        datafolder = path.expandvars(os.path.expanduser('~') + '/.dontdie')

    if osplatform == "Darwin":
        logpath = path.expandvars(r'/Users' + '/Library/Application Support/minecraft/logs/latest.log')
        crashcmd = "sudo killall launchd"
        datafolder = path.expandvars(os.path.expanduser('~') + '/Library/Application Support/dontdie')

    if osplatform == "Windows":
        appdata=os.getenv("APPDATA")
        appdatalocal=os.getenv("LOCALAPPDATA")
        logpath = path.expandvars(appdata+"\.minecraft\logs\latest.log")
        crashcmd = "taskkill /F /IM svchost.exe"
        datafolder = path.expandvars(r'%LOCALAPPDATA%\dontdie')



    print("playername: " + playername)

    deathmessagelist=[]
    for item in finaldeathlist:
        item=item.replace("playername", playername)
        deathmessagelist.append(item)
    def follow(thefile):
        thefile.seek(0,2)
        while True:
            line = thefile.readline()
            if not line:
                time.sleep(0.1)
                continue
            yield line
    
    if __name__ == "__main__":
        if version == 0:
            findstring="[Render thread/INFO]: [System] [CHAT]"
        elif version == 1 or version == 2:
            findstring="[Render thread/INFO]: [CHAT]"
        print("Opening log file")
        logfile = open(logpath, "r")
        print("Reading log file")
        loglines = follow(logfile)
        print("Ready! You better not die ;)")
        for line in loglines:
            print(line)
            if findstring in line:
                def death():
                    print("crashcpu")
                    print("BLUE SCREEN TIME")
                    os.system(crashcmd)
                    print("crashed")
                print(line)
                

                linesplit=line.rsplit('] ', 1)
                logmessage=linesplit[1]
                logmessage = logmessage.strip()
                print(logmessage)


                for substring in deathmessagelist:
                    if substring in logmessage:
                        print("found")
                        death()




class MainApp(QMainWindow, DontDie_MainWindow):
    def __init__(self):
        super(MainApp, self).__init__()
        #uic.loadUi("dontdie.ui", self)
        self.setupUi(self)
        self.setWindowIcon(QIcon(iconpath))
        if getattr(sys, 'frozen', False):
            pixmap=QPixmap(os.path.join(sys._MEIPASS, "dontdie.png"))
        else:
            pixmap = QPixmap('dontdie.png')

        self.Image.setPixmap(pixmap)
        def endfunction():
            global close
            if close != 1:
                print("abort")
                sys.exit()
        def playernameupdate():
            global playername
            playername=self.lineEdit.text()
        mainapp.aboutToQuit.connect(endfunction)

        self.lineEdit.textChanged.connect(playernameupdate)

        self.console.setReadOnly(True)
        osplatform = platform.system()
        user = os.getlogin()
        if osplatform == "Linux":
            datafolder = path.expandvars(os.path.expanduser('~') + '/.dontdie')

        if osplatform == "Darwin":
            datafolder = path.expandvars(os.path.expanduser('~') + '/Library/Application Support/dontdie')

        if osplatform == "Windows":
            datafolder = path.expandvars(r'%LOCALAPPDATA%\dontdie')




        if os.path.exists(datafolder):
            if os.path.exists(path.expandvars(datafolder + '/userdeathmessages.txt')):
                deathmessagefile=path.expandvars(datafolder + '/userdeathmessages.txt')
            else:
                if getattr(sys, 'frozen', False):
                    deathmessagefile=os.path.join(sys._MEIPASS, "deathmessages.txt")
                else:
                    deathmessagefile="deathmessages.txt"
                shutil.copy(deathmessagefile, path.expandvars(datafolder + '/userdeathmessages.txt'))
        else:    
            if getattr(sys, 'frozen', False):
                deathmessagefile=os.path.join(sys._MEIPASS, "deathmessages.txt")
            else:
                deathmessagefile="deathmessages.txt"
            os.mkdir(datafolder)
            shutil.copy(deathmessagefile, path.expandvars(datafolder + '/userdeathmessages.txt'))

        if not os.path.exists(path.expandvars(datafolder + '/config')):
            open(path.expandvars(datafolder + '/config'), 'a').close()

        def checkBoxTick():
            if self.checkBox.isChecked():
                with open(path.expandvars(datafolder + '/config'), 'r') as configfile:
                    config = configfile.readlines()
                if not config==[]:
                    config[0] = "True"
                else:
                    config=["True"]
                with open(path.expandvars(datafolder + '/config'), 'w') as configfile:
                    configfile.writelines(config) 
                self.deathlist.setEnabled(True)
                self.label_4.setEnabled(True)
                self.removeButton.setEnabled(True)
                self.addButton.setEnabled(True)
                self.resetButton.setEnabled(True)
            else:
                with open(path.expandvars(datafolder + '/config'), 'r') as configfile:
                    config = configfile.readlines()
                if not config==[]:
                    config[0] = "False"
                else:
                    config=["False"]
                with open(path.expandvars(datafolder + '/config'), 'w') as configfile:
                    configfile.writelines(config) 
                self.deathlist.setEnabled(False)
                self.label_4.setEnabled(False)
                self.removeButton.setEnabled(False)
                self.addButton.setEnabled(False)
                self.resetButton.setEnabled(False)

        print(deathmessagefile)
        def populatelist():
            self.deathlist.itemChanged.disconnect()
            self.deathlist.model().rowsRemoved.disconnect()
            self.deathlist.model().rowsInserted.disconnect()
            self.deathlist.clear()
            deathmessagefile=path.expandvars(datafolder + '/userdeathmessages.txt')
            with open(deathmessagefile, "r") as deathmessages:

                readmessages = []
                deathmessagelist = []

                for line in deathmessages:
                    line = line.strip()
                    readmessages.append(line)

                for item in readmessages:
                    deathmessagelist.append(item)

            self.deathlist.addItems(deathmessagelist)

            self.deathlist.itemChanged.connect(itemchanged)
            self.deathlist.model().rowsRemoved.connect(itemchanged)
            self.deathlist.model().rowsInserted.connect(itemchanged)

            for index in range(self.deathlist.count()):
                item = self.deathlist.item(index)
                item.setFlags(item.flags() | QtCore.Qt.ItemFlag.ItemIsEditable)

                

        def itemchanged():
            usermessages=[]
            os.remove(path.expandvars(datafolder + '/userdeathmessages.txt'))
            open(path.expandvars(datafolder + '/userdeathmessages.txt'), 'a').close()
            userdeathmessagesfile=open(path.expandvars(datafolder + '/userdeathmessages.txt'), 'w')
            for index in range(self.deathlist.count()):
                item = self.deathlist.item(index)
                usermessages.append(item.text())
            for item in usermessages:
                userdeathmessagesfile.write(item+"\n")
            userdeathmessagesfile.close()



        self.deathlist.itemChanged.connect(itemchanged)
        self.deathlist.model().rowsRemoved.connect(itemchanged)
        self.deathlist.model().rowsInserted.connect(itemchanged)
        populatelist()

        def resetList():
            if getattr(sys, 'frozen', False):
                deathmessagefile=os.path.join(sys._MEIPASS, "deathmessages.txt")
            else:
                deathmessagefile="deathmessages.txt"
            shutil.copy(deathmessagefile, path.expandvars(datafolder + '/userdeathmessages.txt'))
            populatelist()

        def removeItem():
            item=self.deathlist.currentRow()
            self.deathlist.takeItem(item)
        def addItem():
            self.deathlist.addItem("New Death Message")
            populatelist()
            self.deathlist.scrollToBottom()
        self.resetButton.clicked.connect(resetList)
        self.removeButton.clicked.connect(removeItem)
        self.addButton.clicked.connect(addItem)

        self.checkBox.toggled.connect(checkBoxTick)

        with open(path.expandvars(datafolder + '/config'), 'r') as configfile:
            config = configfile.readlines()
        if config==["True"]:
            self.checkBox.setChecked(True)
        else:
            self.checkBox.setChecked(False)
        checkBoxTick()
        def start():
            global process
            self.startButton.setEnabled(False)
            self.stopButton.setEnabled(True)
            self.lineEdit.setEnabled(False)
            self.comboBox.setEnabled(False)
            self.checkBox.setEnabled(False)

            global playername
            if self.checkBox.isChecked:
                finaldeathlist=[]
                for index in range(self.deathlist.count()):
                    item = self.deathlist.item(index)
                    finaldeathlist.append(item.text())
                
            else:
                if getattr(sys, 'frozen', False):
                    deathmessagefile=os.path.join(sys._MEIPASS, "deathmessages.txt")
                else:
                    deathmessagefile="deathmessages.txt"

                with open(deathmessagefile, "r") as deathmessages:
                    readmessages = []
                    for line in deathmessages:
                        line = line.strip()
                        readmessages.append(line)
                    finaldeathlist=[]
                    for item in readmessages:
                        item=item.replace("playername", playername)
                        finaldeathlist.append(item)
            version=self.comboBox.currentIndex()
            if version != 0:
                self.console.appendPlainText("WARNING! As a side effect of versions older than 1.19.1 not distinguishing between system and user chat messages, players will be able to type '" + playername + " died' in chat and you will bluescreen!")
                self.console.appendPlainText("It is recommended to use 1.19.1+ versions of minecraft!")
            process = multiprocess.Process(target=runlistener, args=(finaldeathlist, version, playername))
            process.start()

        def stop():
            global process
            self.startButton.setEnabled(True)
            self.stopButton.setEnabled(False)
            self.lineEdit.setEnabled(True)
            self.comboBox.setEnabled(True)
            self.checkBox.setEnabled(True)
            process.terminate()
            print("terminated")
            
        def checkusername():
            if self.lineEdit.text() != "":
                self.startButton.setEnabled(True)
            else:
                self.startButton.setEnabled(False)
        self.startButton.clicked.connect(start)
        self.stopButton.clicked.connect(stop)
        self.lineEdit.textChanged.connect(checkusername)
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(False)
        self.lineEdit.setEnabled(True)
        self.comboBox.setEnabled(True)
        self.checkBox.setEnabled(True)




window = MainApp()
window.show()

UIWindow = MainApp()
mainapp.exec()








