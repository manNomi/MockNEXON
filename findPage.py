from PyQt5 import QtWidgets
from PyQt5.QtGui import *
class Find:
    def __init__ (self,Ui,Db,Con):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui
        self.db=Db     
        self.con=Con
    def findFlow(self,btn):
        if btn==0:
            self.pwFind()
        elif btn==1:
            self.idFind()
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.con.reset(self.ui.joinCheckList,self.ui.widEtc4List,self.ui.loginLineList,self.ui.findIdpageList,self.ui.joinEnterList)
            
    def idFind(self):
        phoneNumber=self.ui.findIdpageList[0].text()
        id=self.db.readData("user",["phone"],[phoneNumber])
        if len(id)==0:
            self.ui.dialog(self.Dialog,"It's an PhoneNumber that doesn't exist")
            self.Dialog.show()
        else:
            text="ID="+str(id[0][1])
            self.ui.dialog(self.Dialog,text)
            self.Dialog.show()
    def pwFind(self):
        idvalue=self.ui.findIdpageList[3].text()
        password=self.db.readData("user",["id"],[idvalue])
        if len(password)==0:
            self.ui.dialog(self.Dialog,"It's an ID that doesn't exist")
            self.Dialog.show()
        else:
            self.ui.dialog(self.Dialog,"PASSWORD="+str(password[0][2]))
            self.Dialog.show()
