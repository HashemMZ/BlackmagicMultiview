# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 12:56:01 2023

@author: Hashem Moradmand هاشم مرادمند
github.com/HashemMZ
"""

import sys
import time
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, 
                             QMainWindow,
                             QLabel, 
                             QWidget, 
                             QGridLayout, 
                             QVBoxLayout, 
                             QHBoxLayout, 
                             QPushButton,
                             QLineEdit,
                             QInputDialog
                            
                             )

import telnetlib


class view(QMainWindow):
    '''view-controller class'''
    numOfDevices = [0]
    
    connectOKflag = False
    #later load from an XML file
    nameOfMonitors=[]
    IP=[]
    
    def __init__(self, numOfDevices, model):
        super().__init__()    
        self.connectOKflag = False  
        self.selectedMonitor = 0
        self.loadSettings()                  
        self.numOfDevices = numOfDevices
        self.model = model
        self.setWindowTitle("Blackmagic Multiview16")
        self.setWindowIcon(QIcon('monitor.png'))
        self.layout = QVBoxLayout()
        mainWidget = QWidget()
        mainWidget.setLayout(self.layout)
        self.setCentralWidget(mainWidget)
        self._createMonitorButtons()
        #self._createNodalButtons()
        self._createInputSelectButtons()
        self._createDeviceIPinput()
        self._createSettingsButton()
        self._creatMessageLabel()

        self._connectSignalsAndSlots()
        

        
    
    def _createMonitorButtons(self):
        TVlayout = QHBoxLayout()
        self.TVButton = {}
        for i in range(self.numOfDevices[0]):
            self.TVButton[i] = QPushButton(self.nameOfMonitors[i].format(str(i)))
            self.TVButton[i].setStyleSheet('''background-color: lightgray;''')
            TVlayout.addWidget(self.TVButton[i],i)   
        self.layout.addLayout(TVlayout)
        
        Nodallayout = QHBoxLayout()
        #self.NodalButton = {}
        self.TVButton[4]=QPushButton(self.nameOfMonitors[4])
        self.TVButton[4].setStyleSheet('''background-color: lightgray;''')
        Nodallayout.addWidget(self.TVButton[4],0)         
        
        self.TVButton[5]=QPushButton(self.nameOfMonitors[5])
        self.TVButton[5].setStyleSheet('''background-color: lightgray;''')
        Nodallayout.addWidget(self.TVButton[5],0) 
        self.layout.addLayout(Nodallayout)

    
    def _createInputSelectButtons(self):
        self.layout.addSpacing(10)       
        soloLable = QLabel(' Select solo channel ');
        soloLable.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(soloLable)
        inputChannelLayout = QGridLayout()
        self.soloInButton = {}
        for i in range(4):
            for j in range(4):
                index = (i*4)+j+1
                #print('{} and {}'.format(i, j))
                self.soloInButton[index]=QPushButton(str(index))
                self.soloInButton[index].setStyleSheet('''background-color: lightgray;''')
                inputChannelLayout.addWidget(self.soloInButton[index],j,i)
                
        #self.viewButton = QPushButton("view 4x4")                
        #inputChannelLayout.addWidget(self.viewButton, 4, 1, 1, 2)
        #self.layout.addSpacing(10)
        self.layout.addLayout(inputChannelLayout)
        
    def _createSettingsButton(self):
        
        lastRow = QHBoxLayout()
        self.setIPbutton = QPushButton("Save new IP")
        lastRow.addWidget(self.setIPbutton)
        self.layout.addLayout(lastRow)
        
    def _creatMessageLabel(self):
        self.layout.addSpacing(10)
        self.messageLabel = QLabel("Start")        
        self.layout.addWidget(self.messageLabel)
        
    def _connectSignalsAndSlots(self):
        self.TVButton[0].clicked.connect(lambda: self.setDevice4x4(0))
        self.TVButton[1].clicked.connect(lambda: self.setDevice4x4(1))
        self.TVButton[2].clicked.connect(lambda: self.setDevice4x4(2))
        self.TVButton[3].clicked.connect(lambda: self.setDevice4x4(3))
        self.TVButton[4].clicked.connect(lambda: self.setDevice4x4(4))
        self.TVButton[5].clicked.connect(lambda: self.setDevice4x4(5))
        
        self.soloInButton[1].clicked.connect(lambda: self.selectSoloChannel(1))
        self.soloInButton[2].clicked.connect(lambda: self.selectSoloChannel(2))
        self.soloInButton[3].clicked.connect(lambda: self.selectSoloChannel(3))
        self.soloInButton[4].clicked.connect(lambda: self.selectSoloChannel(4))
        self.soloInButton[5].clicked.connect(lambda: self.selectSoloChannel(5))
        self.soloInButton[6].clicked.connect(lambda: self.selectSoloChannel(6))
        self.soloInButton[7].clicked.connect(lambda: self.selectSoloChannel(7))
        self.soloInButton[8].clicked.connect(lambda: self.selectSoloChannel(8))
        self.soloInButton[9].clicked.connect(lambda: self.selectSoloChannel(9))
        self.soloInButton[10].clicked.connect(lambda: self.selectSoloChannel(10))
        self.soloInButton[11].clicked.connect(lambda: self.selectSoloChannel(11))
        self.soloInButton[12].clicked.connect(lambda: self.selectSoloChannel(12))
        self.soloInButton[13].clicked.connect(lambda: self.selectSoloChannel(13))
        self.soloInButton[14].clicked.connect(lambda: self.selectSoloChannel(14))
        self.soloInButton[15].clicked.connect(lambda: self.selectSoloChannel(15))
        self.soloInButton[16].clicked.connect(lambda: self.selectSoloChannel(16))
        
        self.setIPbutton.clicked.connect(self.setIP)
        
    def setDevice4x4(self, key):
        self.recolorChannelButtons()
        #self.model.disconnect()        
        for i in range(sum(self.numOfDevices)):
            if key == i:
                self.selectedMonitor = i
                self.renumberChannelButtons()
                self.messageLabel.setText('4x4 view selected')
                self.setIPbutton.setIcon(QIcon('NetworkStatus-OK.png'))
                self.TVButton[i].setStyleSheet('''background-color: skyblue;''')
                self.model.disconnect()
                self.ipEdit.setText(str(self.IP[i]))
                self.connectOKflag = self.connectAndSet4x4(self.IP[i])
                if self.connectOKflag == False:
                    self.messageLabel.setText('connection failed')
                    self.setIPbutton.setIcon(QIcon('NetworkStatus-Error.png'))
                #self.model.ping()
                    
            else:
                #self.model.disconnect()
                self.TVButton[i].setStyleSheet('''background-color: lightgray;''')
    def connectAndSet4x4(self, ip):
        self.model.setIP(ip)
        if self.model.connect() == False :
            return False
        else:
            self.model.viewAll()
            return True
        
    def recolorChannelButtons(self):
        self.selectedChannel = -1
        for channel in range(1,17):
            self.soloInButton[channel].setStyleSheet('''background-color: lightgray;''')
    def renumberChannelButtons(self):
        if self.selectedMonitor in range(4):            
            for i in range(4):
                for j in range(4):
                    index = (i*4)+j+1
                    self.soloInButton[index].setText(str(index + 16 * (self.selectedMonitor)))
        else:
            for i in range(4):
                for j in range(4):
                    index = (i*4)+j+1
                    self.soloInButton[index].setText(str(index))


    def selectSoloChannel(self, key):
        if self.connectOKflag == True:
            for channel in range(1,17):
                if key == channel:
                    self.messageLabel.setText('solo selected')
                    self.soloInButton[channel].setStyleSheet('''background-color: skyblue;''')
                    self.model.solo()
                    self.model.route(channel) 
                    time.sleep(0.2)
                    self.model.solo()
                    self.model.route(channel) 
                    self.selectedChannel = channel
                    #self.ipEdit.setText(str(self.IP[i]))
                else:
                    #self.model.closeSession(self.IP[i])
                    self.soloInButton[channel].setStyleSheet('''background-color: lightgray;''')
        
    def _createDeviceIPinput(self):
        self.layout.addSpacing(10)
        self.ipEdit = QLineEdit();
        self.ipEdit.setAlignment(Qt.AlignCenter)
        #self.ipEdit.setInputMask("select a TV");
        self.layout.addWidget(self.ipEdit,0)
    
    def setIP(self):
        self.IP[self.selectedMonitor] = self.ipEdit.text()
        self.storeSettings()
    
    def storeSettings(self):
        with open('settings.txt', 'w') as writer:
            for i, ip in enumerate(self.IP):
                writer.write(ip+'\n')
                writer.write(self.nameOfMonitors[i]+'\n')
        
    
    def loadSettings(self):
        try:
            with open('settings.txt', 'r') as reader:
                 # Read and print the entire file line by line
                 lineIP = reader.readline().strip()
                 while lineIP != '':  # The EOF char is an empty string
                     self.IP.append(lineIP)
                     #print(lineIP, end='')
                     self.nameOfMonitors.append(reader.readline().strip())
                     lineIP  = reader.readline().strip()
        except:
            self.nameOfMonitors=['Rack1','Rack2','Rack3','Rack4','Nodal HD','Nodal SD']
            self.IP=['10.0.9.11','10.0.9.12','10.0.9.13','10.0.9.14','10.0.9.15','10.0.9.16']
                 
class BlackmagicModel:    
    port = 9990
    session = []
    def __init__(self, ip='192.168.1.1'):
        self.ip = ip
    def setIP(self, ip):
        self.ip = ip
    def connect(self):
        try:
            self.session = telnetlib.Telnet(self.ip, port = self.port, timeout = 0.1)
            print(self.session.read_until(b'END PRELUDE:',timeout=0.1))
            return True
        except:
            return False
        
    def disconnect(self):
        try:
            self.session.close()
        except:
            pass
    def solo(self):
        config = 'configuration:'
        solo = 'solo enabled: true'
        self.session.write(self.command(config,solo))
        print(self.session.read_until(b'Take Mode',timeout=0.1))
    def viewAll(self):
        config = 'configuration:'
        solo = 'solo enabled: false'
        self.session.write(self.command(config,solo))
        print(self.session.read_until(b'Take Mode',timeout=0.1))
    def route(self, channel):
        config = 'video output routing:'
        param = '16 '+str(channel-1)
        self.session.write(self.command(config,param))
        print(self.session.read_until(b'Take Mode',timeout=0.1))
    def ping(self):
        config = 'ping:'
        param =''
        self.session.write(self.command(config,param))
        print(self.session.read_until(b'Take Mode',timeout=0.1))

    def command(self,part1,part2):
        return ('%s\n %s\n\n'% (part1, part2)).encode('ascii')

    

    

def main():
    print('Blackmagic Control Software')
    numOfDevices = [4 ,2]
    app = QApplication([])
    blackmagicDevices = BlackmagicModel()
    window = view(numOfDevices, model = blackmagicDevices)
    window.show()
    #controller(numOfDevices, model = blackmagicDevices, view = window)    

    sys.exit(app.exec())
    


if __name__ == '__main__':
    main()
