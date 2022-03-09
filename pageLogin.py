from PyQt5 import QtWidgets
from PyQt5.QtGui import *

class Login:
    def __init__ (self,Ui,Db,Con):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui
        self.db=Db
        self.con=Con    
    def loginFlow(self,btnNumber):
        id,pw=self.ui.loginLineList[0].text(),self.ui.loginLineList[1].text()
        if btnNumber==0:
            self.login_event(id,pw)
        elif btnNumber==1:
            self.ui.stackedWidget.setCurrentIndex(2)
        elif btnNumber==2 :
            self.ui.chooseIDPW.setCurrentIndex(1)
            self.ui.stackedWidget.setCurrentIndex(1)
        elif btnNumber==3:
            self.ui.chooseIDPW.setCurrentIndex(0)
            self.ui.stackedWidget.setCurrentIndex(1)
        else:
            self.ui.stackedWidget.setCurrentIndex(4)
            
    def login_event(self,id,pw):
        if len(self.db.readData("user",["id","pw"],[id,pw]))!=0:
            self.ui.stackedWidget.setCurrentIndex(3)
            id=self.ui.loginLineList[0].text()
            userData=self.db.readData("user",["id"],[id])
            print(id)
            print(userData)
            text="Welcome to Nexon \nID : "+str(userData[0][1])+"\nNickname: "+str(userData[0][3])+"\nphonenumber :"+str(userData[0][4])+"\nbirth : "+str(userData[0][5])+"\nSTRONG "+str(userData[0][6])
            self.ui.mainPic3List[0].setText(text)

        else:
            self.ui.dialog(self.Dialog,"Nexon ID or password is not registered")
            self.Dialog.show()
            

