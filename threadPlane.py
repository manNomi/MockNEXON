import keyboard
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
class keyPress(QThread):
    keyEvent=pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.attack=0
        self.result2=False

    def run(self):
        while True:
            if self.result2==True:
                self.keyEvent.emit(self.attack)
                if keyboard.read_key() == "r":
                    self.attack=1
                else:
                    self.keyEvent.emit(0)

            time.sleep(0.5)

class Move(QThread):
    moveEvent=pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.moveNumber=0
        self.result3=False

    def run(self):
        while True:
            if self.result3==True:
                for index in range(0,90):
                    self.moveEvent.emit(self.moveNumber) 
                    self.moveNumber+=5
                    time.sleep(0.025)
                self.moveNumber=0
                self.result3=False
           

