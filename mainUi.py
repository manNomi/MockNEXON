from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
import sys
import config
class Ui(object):

    def __init__(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.MainWindow.setGeometry(800,60,892,1985)
        self.MainWindow.setMinimumSize(892, 1985)
        self.MainWindow.setMaximumSize(892, 1985)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(40, 10, 800, 2000))
        self.stackedWidget.setStyleSheet("background-color : #ffffff;")
        self.stackedWidget.setObjectName("stackedWidget")

        #1  login page
        self.PageLogin = QtWidgets.QWidget()
        self.PageLogin.setObjectName("PageLogin")

        main1LogoXY=[[315, 69, 210, 51],[330, 130, 136, 24],[100, 230, 136, 24],[100, 330, 136, 24]]
        main1LogoText=["NEXON","Nexon ID Login","ID","PASSWORD"]
        mainLogoList=[]
        for index in range(0,4):
            loginLogo=QtWidgets.QLabel(self.PageLogin)
            loginLogo.setGeometry(main1LogoXY[index][0],main1LogoXY[index][1],main1LogoXY[index][2],main1LogoXY[index][3])
            font = QtGui.QFont()
            font.setFamily("Berlin Sans FB Demi")
            if index==0:
                font.setPointSize(26)
            else:   
                font.setPointSize(10)
            loginLogo.setFont(font)
            loginLogo.setText(main1LogoText[index])
            mainLogoList.append(loginLogo) 

        loginLineJoin=[[100,260,600,70],[100,360,600,70]]
        loginLineineText=["",""]
        self.loginLineList=[]
        for index in range(0,len(loginLineJoin)):
            loginLine=QtWidgets.QLineEdit(self.PageLogin)
            loginLine.setGeometry(loginLineJoin[index][0],loginLineJoin[index][1],loginLineJoin[index][2],loginLineJoin[index][3])
            font = QtGui.QFont()
            font.setFamily("Berlin Sans FB Demi")
            loginLine.setFont(font)
            loginLine.setText(loginLineineText[index])
            loginLine.setStyleSheet("background-color: #ffffff;\n"+"border:2px solid #EEEEEE;")
            self.loginLineList.append(loginLine) 
   

        loginBtnJoin=[[100, 470, 600, 70],[100,560,101, 31],[220,560, 101, 31],[330, 560, 161, 31],[490, 560, 161, 31]]
        loginBtnText=["Login","JOIN","FIND ID","FIND PASSWORD","WITHDRAWAL"]
        self.loginBtnList=[]
        for index in range(0,len(loginBtnJoin)):
            loginBtn=QtWidgets.QToolButton(self.PageLogin)
            loginBtn.setGeometry(loginBtnJoin[index][0],loginBtnJoin[index][1],loginBtnJoin[index][2],loginBtnJoin[index][3])
            font = QtGui.QFont()
            if index!=0:
                loginBtn.setStyleSheet("background-color: #ffffff;\n"+"border:0px solid #EEEEEE;")
                font.setFamily("Berlin Sans FB Demi")
            else:
                loginBtn.setStyleSheet("background-color: #0F0E0E;\n"+"color: #ffffff;")
                font.setFamily("Berlin Sans FB Demi")
                font.setBold(True)
            font.setPointSize(10)
            loginBtn.setFont(font)
            loginBtn.setText(loginBtnText[index])
            loginBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.loginBtnList.append(loginBtn)     
        self.stackedWidget.addWidget(self.PageLogin)

        
        #2  find page

        self.PageFind = QtWidgets.QWidget()
        self.PageFind.setObjectName("PageFind")
        self.chooseIDPW = QtWidgets.QTabWidget(self.PageFind)
        self.chooseIDPW.setGeometry(70, 50, 661, 361)
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.chooseIDPW.setFont(font)
        self.chooseIDPW.setObjectName("chooseIDPW")
        self.findID = QtWidgets.QWidget()
        self.findID.setObjectName("findID")
        self.findPW = QtWidgets.QWidget()
        self.findPW.setObjectName("findPW")

        findIdpage=[[20, 60, 500, 50],[20, 20, 491,24],[20, 20, 491,24],[20, 60, 500, 50],[340, 170, 181, 70]]
        findIdpageText=["","PHONE NUMBER","ID","","NEXON ID"]
        self.findIdpageList=[]
        for index in range(0,len(findIdpage)):
            font = QtGui.QFont()
            if index==0:
                find = QtWidgets.QLineEdit(self.findID)
                find.setStyleSheet("background-color: #D8E3E7;\n")
            elif index==1 :
                find = QtWidgets.QLabel(self.findID)
                find.setStyleSheet("color : #D5D5D5;")
            elif index==2:
                find = QtWidgets.QLabel(self.findPW)
                find.setStyleSheet("color : #D5D5D5;")
            elif index==3:
                find = QtWidgets.QLineEdit(self.findPW)
                find.setStyleSheet("background-color: #D8E3E7;\n")
            else:
                find= QtWidgets.QLabel(self.findPW)
                find.setStyleSheet("color : #D5D5D5;")
                
            find.setGeometry(findIdpage[index][0],findIdpage[index][1],findIdpage[index][2],findIdpage[index][3])
            font.setFamily("Berlin Sans FB Demi")
            font.setPointSize(10)
            find.setText(findIdpageText[index])
            find.setFont(font)
            self.findIdpageList.append(find) 

        findBtnGeo=[[340, 170, 181, 70],[340, 170, 181, 70],[620, 20, 101, 41]]
        findBtnText=["CHECK","CHECK","BACK"]
        self.findBtnList=[]
        for index in range(0,len(findBtnGeo)):
            if index==0:
                findBtn = QtWidgets.QToolButton(self.findPW)
            elif index==1:
                findBtn = QtWidgets.QToolButton(self.findID)
            else:
                findBtn = QtWidgets.QToolButton(self.PageFind)
            findBtn.setStyleSheet("background-color: #0F0E0E;\n"+"color: #ffffff;")
            findBtn.setGeometry(findBtnGeo[index][0],findBtnGeo[index][1],findBtnGeo[index][2],findBtnGeo[index][3])
            findBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            font = QtGui.QFont()
            font.setPointSize(10)
            font.setFamily("Berlin Sans FB Demi")
            findBtn.setFont(font)
            findBtn.setText(findBtnText[index])
            findBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.findBtnList.append(findBtn)    

        self.chooseIDPW.addTab(self.findPW, "")
        self.chooseIDPW.addTab(self.findID, "")

        self.chooseIDPW.setTabText(self.chooseIDPW.indexOf(self.findPW),"PASSWORD")
        self.chooseIDPW.setTabText(self.chooseIDPW.indexOf(self.findID),"ID")
        self.stackedWidget.addWidget(self.PageFind)




        #3  Join Page
        self.qPixmapVar = QPixmap() 
        self.PageJoin = QtWidgets.QWidget()
        self.PageJoin.setObjectName("PageJoin")

        image=["image/wellcom","image/image1","image/image2","image/image3","image/image4"]
        joinPictrure=[[280, 100, 190, 190],[18, 520, 90, 90],[18, 730, 90, 90],[18, 940, 90, 90],[18, 1160, 90, 90]]
        joinPictrureList=[]
        for index in range(0,len(joinPictrure)):
            picture = QtWidgets.QLabel(self.PageJoin)
            picture.setGeometry(joinPictrure[index][0],joinPictrure[index][1],joinPictrure[index][2],joinPictrure[index][3])
            picture.setStyleSheet("background-color : white;")   
            self.qPixmapVar.load(image[index])
            self.qPixmapVar = self.qPixmapVar.scaledToWidth(joinPictrure[index][2])
            self.qPixmapVar = self.qPixmapVar.scaledToHeight(joinPictrure[index][3])
            picture.setPixmap(self.qPixmapVar)
            joinPictrureList.append(picture)
          
            
        joinLogo=[[30, 10, 162, 50],[190, 30, 136, 24],[243, 280, 271, 61]]
        joinLogoList=[]
        fontlogo=[22,10,14]
        joinLogoText=["NEXON ","MEMBERS","wellcome to NEXON"]
        for index in range(0,len(joinLogo)):
            logo2 = QtWidgets.QLabel(self.PageJoin)
            font = QtGui.QFont()
            logo2.setText(joinLogoText[index])
            font.setFamily("Berlin Sans FB Demi")
            font.setPointSize(fontlogo[index])
            if index==1:
                logo2.setStyleSheet("color : #D5D5D5;")
            else:
                logo2.setStyleSheet("color : black;")   
            logo2.setFont(font)
            logo2.setGeometry(joinLogo[index][0],joinLogo[index][1],joinLogo[index][2],joinLogo[index][3])
            joinLogoList.append(logo2)


        joinCheck=[[170, 740, 551, 31],[170, 910, 551, 31],[160, 1740, 91, 31],[160, 1780, 116, 22]]
        self.joinCheckList=[]
        joinCheckText=["It receives events and various game information and service guidance provided by Nexon.","If you use an inappropriate nickname, you may be subject to operational sanctions","MEN","WOMAN"]
        for index in range(0,len(joinCheck)):
            check1 = QtWidgets.QCheckBox(self.PageJoin)
            font = QtGui.QFont()
            check1.setText(joinCheckText[index])
            font.setFamily("Berlin Sans FB Demi")
            font.setPointSize(10)
            if index==0 or index==1:
                check1.setStyleSheet("color : #D5D5D5;")
            else:
                check1.setStyleSheet("color : black;")   
            check1.setFont(font)
            check1.setGeometry(joinCheck[index][0],joinCheck[index][1],joinCheck[index][2],joinCheck[index][3])
            check1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            self.joinCheckList.append(check1)


        joinBtn=[[660, 10, 101, 41],[330, 1880, 181, 70]]
        self.joinBtnList=[]
        joinBtnText=["BACK","CHECK"]
        for index in range(0,len(joinBtn)):
            btn1 = QtWidgets.QToolButton(self.PageJoin)
            btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            font = QtGui.QFont()
            btn1.setText(joinBtnText[index])
            font.setFamily("Berlin Sans FB Demi")

            btn1.setStyleSheet("background-color: #0F0E0E;\n"+"color: #ffffff;")
            btn1.setFont(font)
            
            btn1.setGeometry(joinBtn[index][0],joinBtn[index][1],joinBtn[index][2],joinBtn[index][3])
            self.joinBtnList.append(btn1)
                

        joinWord=[[170, 470, 501, 81],[240, 550, 491, 24],[170, 630, 491, 24],[170, 800, 491, 24],[170, 960, 491, 24],[170, 1060, 491, 24],[170, 1170, 491, 24],[170, 1320, 491, 24],[160, 1700, 491, 24]]
        joinWordList=[]
        joinWordText=["Enter basic information","Please enter the basic information correctly.","NEXON ID (E-Mail)","NICKNAME","PASSWORD","PASSWORD CHECK","PHONE NUMBER","DATE OF BIRTH","GENDER"]
        for index in range(0,len(joinWord)):
            word1 = QtWidgets.QLabel(self.PageJoin)
            font = QtGui.QFont()
            word1.setText(joinWordText[index])
            font.setFamily("Berlin Sans FB Demi")
            if index==0:
                word1.setStyleSheet("color : black;")
                font.setPointSize(22)
            else:
                word1.setStyleSheet("color : #D5D5D5;")
                font.setPointSize(10)
            word1.setFont(font)
            word1.setGeometry(joinWord[index][0],joinWord[index][1],joinWord[index][2],joinWord[index][3])
            joinWordList.append(word1)
        
        joinLine=[[0, 60, 800, 2],[0, 460, 791, 3],[130, 460, 5, 1400],[160, 600, 561, 2],[160, 1830, 500, 2],[160, 338, 441, 2]]
        joinLineList=[]
        for index in range(0,len(joinLine)):
            line1 = QtWidgets.QLabel(self.PageJoin)
            if index==3 or index ==5:
                line1.setStyleSheet("background-color :  #D5D5D5;")       
            else:
                line1.setStyleSheet("background-color : #0F0E0E;")   
            line1.setGeometry(joinLine[index][0],joinLine[index][1],joinLine[index][2],joinLine[index][3])
            joinLineList.append(line1)

        joinEnter=[[170, 670, 500, 50],[170, 840, 500, 50],[170, 1000, 500, 50],[170, 1100, 500, 50],[170, 1210, 500, 50]]
        self.joinEnterList=[]
        for index in range(0,len(joinEnter)):
            enter1 = QtWidgets.QLineEdit(self.PageJoin)
            enter1.setStyleSheet("background-color: #D8E3E7;\n")
            enter1.setGeometry(joinEnter[index][0],joinEnter[index][1],joinEnter[index][2],joinEnter[index][3])
            self.joinEnterList.append(enter1)
        
        
        self.calander = QtWidgets.QCalendarWidget(self.PageJoin)
        self.calander.setGeometry(170, 1370, 501, 301)
        self.calander.setStyleSheet("background-color : #D8E3E7;\n"+"color : black;")
        self.calander.setSelectedDate(QtCore.QDate(2000, 1, 11))
        self.calander.setGridVisible(True)
        self.calander.setObjectName("calander")


        self.verticalScrollBar = QtWidgets.QScrollBar(self.PageJoin)
        self.verticalScrollBar.setGeometry(780, 70, 10, 1800)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.verticalScrollBar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.stackedWidget.addWidget(self.PageJoin)


        #4 page Main
        self.PageMain = QtWidgets.QWidget()
        self.PageMain.setObjectName("PageMain")
        mainLogo3=[[340, 0, 162, 50],[130, 780, 511, 81],[0, 60, 800, 2],[30,510,690,2],[30,510,2,280],[720,510,2,280],[30,790,690,2],[300,1600, 511, 81],[550,1650, 150,120]]
        self.mainLogo3List=[]
        mainLogo3Text=["NEXON","Rock paper scissors game","","","","","","PlaneGame\nattack=r","score"]
        for index in range(0,len(mainLogo3)):
            logo3 = QtWidgets.QLabel(self.PageMain)
            font = QtGui.QFont()
            logo3.setText(mainLogo3Text[index])
            font.setFamily("Berlin Sans FB Demi")
            if index==0 or index==1 or index==7:
                logo3.setStyleSheet("color : black;")
                font.setPointSize(22)
            elif index==8 :
                logo3.setStyleSheet("color : black;")
                font.setPointSize(15)
            else:
                logo3.setStyleSheet("background-color : #0F0E0E;")
            logo3.setFont(font)
            logo3.setGeometry(mainLogo3[index][0],mainLogo3[index][1],mainLogo3[index][2],mainLogo3[index][3])
            self.mainLogo3List.append(logo3)


        mainBtn3=[[290, 1400, 151, 131],[510, 1400, 151, 131],[70, 1400, 151, 131],[580, 10, 112, 34],[70, 1120, 112, 34],[70, 1600, 112, 34]]
        self.mainBtn3List=[]
        mainBtn3Text=["PAPER","SCISSORS","ROCK","LOGOUT","START","RESTART"]
        for index in range(0,len(mainBtn3)):
            btn3 = QtWidgets.QToolButton(self.PageMain)
            btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            font = QtGui.QFont()
            btn3.setText(mainBtn3Text[index])
            font.setFamily("Berlin Sans FB Demi")
            if index==0 or index==1 or index==2:
                btn3.setStyleSheet("background-color: #D8E3E7;border-radius: 10px ;")
                font.setPointSize(9)
            if index==4 or index==5:
                btn3.setStyleSheet("background-color :black ;\ncolor:#ffffff")
            else:
                btn3.setStyleSheet("background-color : #ffffff;\ncolor:black")
            btn3.setFont(font)
            btn3.setGeometry(mainBtn3[index][0],mainBtn3[index][1],mainBtn3[index][2],mainBtn3[index][3])
            self.mainBtn3List.append(btn3)

        mainPic3=[[50, 540, 670, 250],[350, 450, 101, 31],[0, 90, 800, 351],[300,930, 171, 131],[330,1210, 121, 81],[330,1070, 121, 81],[70,1800, 150, 120],[270,1700, 80,30],[550,1800, 150,120]]
        self.mainPic3List=[]
        mainPic3Text=["Name","1/6","picture","WIn or LOSE","PLAYER","ENEMY","plane","atack","monster"]
        for index in range(0,len(mainPic3)):
            pic3 = QtWidgets.QLabel(self.PageMain)
            font = QtGui.QFont()
            pic3.setText(mainPic3Text[index])
            font.setFamily("Berlin Sans FB Demi")
            font.setPointSize(15)
            pic3.setStyleSheet("background-color : #ffffff;\ncolor:black")
            pic3.setFont(font)
            pic3.setGeometry(mainPic3[index][0],mainPic3[index][1],mainPic3[index][2],mainPic3[index][3])
            self.mainPic3List.append(pic3)

        self.verticalScrollBar2 = QtWidgets.QScrollBar(self.PageMain)
        self.verticalScrollBar2.setGeometry(780, 70, 10, 1800)
        self.verticalScrollBar2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar2.setObjectName("verticalScrollBar2")
        self.verticalScrollBar2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stackedWidget.addWidget(self.PageMain)
      

        self.stackedWidget.addWidget(self.PageMain)
        self.MainWindow.setCentralWidget(self.centralwidget)

        self.changeNumber=0

        
        #5 page WID

        self.Pagewid = QtWidgets.QWidget()
        self.Pagewid.setObjectName("pagewid")

        widLogo4=[[30, 20, 162, 50],[190, 40, 136, 24],[40, 110, 136, 24],[40, 280, 136, 24],[0, 80, 800, 2]]
        widLogo4List=[]
        widLogo4Text=["NEXON","MEMBERS","ENTER ID","ENTER PW",""]
        for index in range(0,len(widLogo4)):
            Logo4 = QtWidgets.QLabel(self.Pagewid)
            font = QtGui.QFont()
            Logo4.setText(widLogo4Text[index])
            font.setFamily("Berlin Sans FB Demi")
            if index==0:
                font.setPointSize(22)      
                Logo4.setStyleSheet("color :black ;background-color :white;")
            elif index==len(widLogo4)-1:
                Logo4.setStyleSheet("background-color :black")
            else:
                Logo4.setStyleSheet("color :#D5D5D5;background-color :white;")
                font.setPointSize(10)
            Logo4.setFont(font)
            Logo4.setGeometry(widLogo4[index][0],widLogo4[index][1],widLogo4[index][2],widLogo4[index][3])
            widLogo4List.append(Logo4)

        widEtc4=[[40, 150, 600, 70],[40, 310, 600, 70],[40, 410, 551, 31]]
        self.widEtc4List=[]
        widEtc4Text=["","","If you really want to leave, please press the check box."]
        for index in range(0,len(widEtc4)):
            if index==0 or index==1:
                Etc4 = QtWidgets.QLineEdit(self.Pagewid)
                Etc4.setStyleSheet("color :black ;background-color :white;")
            else:
                Etc4 = QtWidgets.QCheckBox(self.Pagewid)
                Etc4.setStyleSheet("color :#D5D5D5 ; background-color :white;")
            font = QtGui.QFont()
            Etc4.setText(widEtc4Text[index])
            font.setFamily("Berlin Sans FB Demi")
            Etc4.setFont(font)
            Etc4.setGeometry(widEtc4[index][0],widEtc4[index][1],widEtc4[index][2],widEtc4[index][3])
            self.widEtc4List.append(Etc4)


        widBtn4=[[660, 20, 101, 41],[450, 480, 181, 70]]
        self.widBtnList=[]
        widText=["BACK","CHECK"]
        for index in range(0,len(widBtn4)):
            Btn = QtWidgets.QToolButton(self.Pagewid)
            Btn.setStyleSheet("color :white ;background-color :black;")
            Btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
            font = QtGui.QFont()
            Btn.setText(widText[index])
            font.setFamily("Berlin Sans FB Demi")
            Btn.setFont(font)
            Btn.setGeometry(widBtn4[index][0],widBtn4[index][1],widBtn4[index][2],widBtn4[index][3])
            self.widBtnList.append(Btn)


        self.stackedWidget.addWidget(self.Pagewid)


        self.stackedWidget.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def dialog(self,Dialog,text):
        Dialog.setObjectName("Dialog")
        Dialog.resize(600, 300)
        Dialog.setStyleSheet("background-color : #9B0000;")
        self.dialogLabel = QtWidgets.QLabel(Dialog)
        self.dialogLabel.setGeometry(QtCore.QRect(0, 0, 600, 300))
        font = QtGui.QFont()
        font.setFamily("Berlin Sans FB Demi")
        font.setPointSize(12)
        self.dialogLabel.setFont(font)
        self.dialogLabel.setStyleSheet("color : white;")
        self.dialogLabel.setObjectName("label")
        self.dialogLabel.setText(text)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv)
    Main=Ui()
    Main.MainWindow.show()
    sys.exit(app.exec_())
    