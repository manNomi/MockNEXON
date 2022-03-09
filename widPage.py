from PyQt5 import QtWidgets
from PyQt5.QtGui import *

class Wid:
    def __init__ (self,Ui,Db,Con):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui
        self.db=Db 
        self.count=0
        self.con=Con
    def widFlow(self,btn):
        if btn==1:
            self.membershipWithdrawal()
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.con.reset(self.ui.joinCheckList,self.ui.widEtc4List,self.ui.loginLineList,self.ui.findIdpageList,self.ui.joinEnterList)
    def membershipWithdrawal(self):
        myId=self.ui.widEtc4List[0].text()
        myPw=self.ui.widEtc4List[1].text()
        checkRepeat=self.db.readData("user",["id","pw"],[myId,myPw])
        checkWid=self.ui.widEtc4List[2].isChecked()
        self.count=0
        if len(checkRepeat)==0:
            self.ui.dialog(self.Dialog,"Invalid ID or password")
            self.Dialog.show()
        else:
            self.count+=1
        if checkWid==False:
            self.ui.dialog(self.Dialog,"please check")
            self.Dialog.show()
        else:
            self.count+=1
        if self.count==2:
            rdData=self.db.readData("user",["id","pw"],[myId,myPw])
            print(rdData)
            sequance=["sequance",rdData[0][0]]
            self.db.deleteData("user",sequance)
            self.ui.dialog(self.Dialog,"You quit being a member.")
            self.Dialog.show()
            self.ui.stackedWidget.setCurrentIndex(0)
            self.count=0
            self.con.reset(self.ui.joinCheckList,self.ui.widEtc4List,self.ui.loginLineList,self.ui.findIdpageList,self.ui.joinEnterList)
