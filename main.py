import mainUi
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot
import data
import pageLogin
import joinPage
import widPage
import mainPage
import findPage
import config
import threadChange
import threadPlane


class Event:
    def __init__(self):
        self.index=0
        self.key=threadPlane.keyPress()
        self.move=threadPlane.Move()
        self.Dialog=QtWidgets.QDialog()
        self.mPic = threadChange.Main_pic()
        self.mGame = threadChange.Main_game()
        self.con=config.Config()
        self.db=data.Database()
        self.ui=mainUi.Ui()
        self.MainWindow = QtWidgets.QMainWindow()
        self.qPixmapVar = QPixmap()
        self.pLog=pageLogin.Login(self.ui,self.db,self.con)
        self.pFind=findPage.Find(self.ui,self.db,self.con)
        self.pJoin=joinPage.Join(self.ui,self.db,self.con)
        self.pWid=widPage.Wid(self.ui,self.db,self.con)
        self.pMain=mainPage.MainPage(self.ui,self.db,self.con)
        self.ui.MainWindow.show()
        self.event()

    def event(self):
        # login Page Btn
        for index in range(0,len(self.ui.loginBtnList)):
            self.ui.loginBtnList[index].clicked.connect(lambda event,value=index : self.pLog.loginFlow(value))

        #find Page Btn
        for index in range(0,len(self.ui.findBtnList)):
            self.ui.findBtnList[index].clicked.connect(lambda event,value=index : self.pFind.findFlow(value))

        #join Page Btn
        for index in range(0,len(self.ui.joinBtnList)):
            self.ui.joinBtnList[index].clicked.connect(lambda event,value=index : self.pJoin.joinFlow(value))
        self.ui.verticalScrollBar.sliderPressed.connect(self.pJoin.location)
        self.ui.verticalScrollBar.valueChanged.connect(lambda event:self.pJoin.scrollChange(self.pJoin.locate))

        #main Page Btn
        for index in range(0,len(self.ui.mainBtn3List)):
            self.ui.mainBtn3List[index].clicked.connect(lambda event,value=index : self.pMain.mainFlow(value))
        
        self.ui.verticalScrollBar2.sliderPressed.connect(self.pMain.location)
        self.ui.verticalScrollBar2.valueChanged.connect(lambda event:self.pMain.scrollChange(self.pMain.locate))
        for index in range(0,3):
            self.ui.mainBtn3List[index].clicked.connect(self.game_click)
        self.ui.mainBtn3List[4].clicked.connect(self.start_click)
        self.ui.mainBtn3List[5].clicked.connect(self.pMain.gameReset)


        #widdrawla page Btn
        for index in range(0,len(self.ui.widBtnList)):
            self.ui.widBtnList[index].clicked.connect(lambda event,value=index : self.pWid.widFlow(value))

        #currentChange Event
        self.ui.stackedWidget.currentChanged.connect(self.thread_pic)
        # self.ui.stackedWidget.currentChanged.connect(self.thread_game)

    def thread_pic(self,tab):
        if tab==3:
            self.mPic.start()
            self.mPic.time.connect(self.pMain.mainPictureChange)
            self.mGame.start()
            self.mGame.game.connect(self.pMain.rspAiPrint)
            self.key.start()
            self.key.keyEvent.connect(self.attack)
            self.key.result2=True
        else:
            self.key.result2=False

    def attack(self,num):
        print(str(num)+"숫자")
        if num==1 and self.pMain.monTrue==1:
            self.move.result3=True
            self.move.start()
            self.move.moveEvent.connect(self.pMain.attack)
        elif num==1 and self.pMain.monTrue==0:
            self.ui.dialog(self.Dialog,"pls press RESTART")
            self.Dialog.show()
            self.result3=False
        else:
            self.result3=False
    def start_click(self):
        self.mGame.result=True
    def game_click(self):
        self.mGame.result=False

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    start=Event()
    sys.exit(app.exec_())




































