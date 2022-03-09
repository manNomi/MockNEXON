from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
import time
class MainPage:
    def __init__ (self,Ui,Db,Con):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui
        self.db=Db     
        self.con=Con
        self.qPixmapVar = QPixmap() 
        self.rspPicture=["image/paper.PNG","image/Scissors.PNG","image/rock.PNG"]
        self.nexonImage=["image/nexon1.PNG","image/nexon2.PNG","image/nexon3.PNG","image/nexon4.PNG","image/nexon5.PNG","image/nexon6.png"]
        self.planeGame=["image/plane.PNG","image/attack.jpg","image/monster.PNG","image/attack2.jpg"]
        self.pictureSet(1800,300,2,self.nexonImage[0])
        self.monTrue=1
        for index in range(0,3):
            number=6+index
            if number==7:
                self.pictureSet(80,30,number,self.planeGame[3])
            else:self.pictureSet(150,120,number,self.planeGame[index])
        self.locate=0
        self.num=0
        self.playerNum=0
        self.score=0
    def mainFlow(self,value):
        if value==4:
            pass
        elif value==5:
            pass
        elif value==3:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.gameReset()
            self.con.reset(self.ui.joinCheckList,self.ui.widEtc4List,self.ui.loginLineList,self.ui.findIdpageList,self.ui.joinEnterList)
        else:
            self.playerRSP(value)
   
    def pictureSet(self,wid,high,num,image):
        self.qPixmapVar.load(image)
        self.qPixmapVar = self.qPixmapVar.scaledToWidth(wid)
        self.qPixmapVar = self.qPixmapVar.scaledToHeight(high)
        self.ui.mainPic3List[num].setPixmap(self.qPixmapVar)

    def playerRSP(self,value):
        self.playerNum=value
        self.pictureSet(120,80,4,self.rspPicture[value])
        self.enemy(value)

    def rspAiPrint(self,random): # computer 와 같이 변환 가능 
        self.pictureSet(120,80,5,self.rspPicture[random])

    def enemy(self,player):
        randAi=random.randint(0,2)
        self.pictureSet(120,80,5,self.rspPicture[randAi])
        if player==randAi:
            self.result="DRAW"
        elif player==2 and randAi==1:
            self.result="WIN"
        elif player==1 and randAi==0:
            self.result="WIN"
        elif player==0 and randAi==2:
            self.result="WIN"
        else:
            self.result="ROSE"
        self.ui.mainPic3List[3].setText(self.result)

    def mainPictureChange(self,num):
        self.pictureSet(1800,300,2,self.nexonImage[num])
        self.ui.mainPic3List[1].setText(str(num+1)+"/6")

    def scrollChange(self,value):
        X,Y,high2=value[0],value[1],value[2]
        X+=11
        Y+=45
        if self.ui.verticalScrollBar2.value()!=0:
            high=self.ui.verticalScrollBar2.value() 
            high-=high2
            self.ui.MainWindow.setGeometry(X,Y-high*8,892,1985)
            print(Y-high)

    def location(self):
        X = self.ui.MainWindow.x()
        Y = self.ui.MainWindow.y()
        high=self.ui.verticalScrollBar2.value()
        self.locate=[X,Y,high]

    def attack(self,X):
        self.pictureSet(80,30,7,self.planeGame[1])
        self.ui.mainPic3List[7].setGeometry(220+X,1850,80,30)

        if X>=350:
            self.pictureSet(150,120,8,self.planeGame[3])
            self.pictureSet(80,30,7,self.planeGame[3])
            self.ui.mainPic3List[7].setGeometry(220,1850,80,30)
            self.score+=1
            self.ui.mainLogo3List[8].setText("score :"+str(self.score))
            self.monTrue=0

    def gameReset(self):
        self.monTrue=1
        self.pictureSet(150,120,8,self.planeGame[2])

        
        
            

