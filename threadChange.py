from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time

class Main_pic(QThread):
    time = pyqtSignal(int)    # 사용자 정의 시그널

    def __init__(self):
        super().__init__()
        self.num = 0           # 초깃값 설정
        self.num2=0
    def run(self):
        while True:
            self.time.emit(self.num)     # 방출
            self.num += 1
            time.sleep(1)
            if self.num>=6:
                self.num=0

class Main_game(QThread):
    game = pyqtSignal(int)    # 사용자 정의 시그널
    def __init__(self):
        super().__init__()
        self.num2 = 0             # 초깃값 설정
        self.result=True
    def run(self):
        while True:
            if self.result==True:
                self.game.emit(self.num2)     # 방출
                self.num2 += 1
                time.sleep(0.08)
                if self.num2>=3:
                    self.num2=0

