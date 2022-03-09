from PyQt5 import QtWidgets
from PyQt5.QtGui import *

class Join:
    def __init__ (self,Ui,Db,Con):
        self.Dialog=QtWidgets.QDialog()
        self.ui=Ui
        self.db=Db     
        self.con=Con
        self.count=0
    def joinFlow(self,btn):
        if btn==0:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.con.reset(self.ui.joinCheckList,self.ui.widEtc4List,self.ui.loginLineList,self.ui.findIdpageList,self.ui.joinEnterList)
        else:
            self.membershipJoin()
    def membershipJoin(self):   #signUp
        self.myId=self.ui.joinEnterList[0].text()
        self.myNickname=self.ui.joinEnterList[1].text()
        self.myPw=self.ui.joinEnterList[2].text()
        self.myPwCheck=self.ui.joinEnterList[3].text()
        self.myPhone=self.ui.joinEnterList[4].text()
        Birth=self.ui.calander.selectedDate()
        year=Birth.year()
        month=Birth.month()
        day=Birth.day()
        self.myBirth=str(year)+"-"+str(month)+"-"+str(day)
        self.myMan=self.ui.joinCheckList[2].isChecked()
        self.myWoman=self.ui.joinCheckList[3].isChecked()
        self.checkID=self.ui.joinCheckList[0].isChecked()
        self.checkNick=self.ui.joinCheckList[1].isChecked()
        gender=0
        count=0
        checkIdRepeat=self.db.readData("user",["id"],[self.myId])
        if len(checkIdRepeat)==0:
            count+=1
        else:
            text="The same IDs."
            self.ui.dialog(self.Dialog,text)
            self.Dialog.show()

        if self.myId.isnumeric()==True or self.myId.isalpha()==True:
            text="Id must contain both numbers and letters"
            self.ui.dialog(self.Dialog,text)
            self.Dialog.show()

        else:count+=1

        if self.myPw.isnumeric()==True or self.myPw.isalpha()==True:
            text="Pw must contain both numbers and letters"
            self.ui.dialog(self.Dialog,text)
            self.Dialog.show()

        else:count+=1

        checkNickRepeat=self.db.readData("user",["Nickname"],[self.myNickname])
        if len(checkNickRepeat)==0:
            count+=1
        else:
            text="The same Nicknames."
            self.ui.dialog(self.Dialog,text)
            self.Dialog.show()

        checkPhoneRepeat=self.db.readData("user",["phone"],[self.myPhone])
        if len(checkPhoneRepeat)==0:
            count+=1
        else:
            text="The same Phone Numbers."
            self.ui.dialog(self.Dialog,text)
            self.Dialog.show()

        if len(list(self.myId))<5 or len(list(self.myId))>10 :
            self.ui.dialog(self.Dialog,"Id length must >5 and <10")
            self.Dialog.show()
        else:
            count+=1
        if len(list(self.myNickname))<2 or len(list(self.myNickname))>10 :
            self.ui.dialog(self.Dialog,"Nickname length must >2 and <10")
            self.Dialog.show()
        else:
            count+=1
        if len(list(self.myPw))<5 or len(list(self.myPw))>10 :
            self.ui.dialog(self.Dialog,"Password length must >5 and <10")
            self.Dialog.show()
        elif self.myPw!= self.myPwCheck:
            self.ui.dialog(self.Dialog,"The password doesn't match")
            self.Dialog.show()
        else:
            count+=1
        if len(list(self.myPhone))!=11 :
            self.ui.dialog(self.Dialog,"phoneNumber must =11 EX)01012345678")
            self.Dialog.show()
        elif self.myPhone.isnumeric()==False:
            self.ui.dialog(self.Dialog,"phoneNumber only combination INT")
            self.Dialog.show()
        else:
            count+=1
        
        if self.myMan==True and self.myWoman==True:
            self.ui.dialog(self.Dialog,"Have the same gender")
            self.Dialog.show()
        elif self.myMan==True:
            gender="Man"
            count+=1
        elif self.myWoman==True:
            gender="Woman"
            count+=1
        else:
            self.ui.dialog(self.Dialog,"Check your gender")
            self.Dialog.show()
        if self.checkID!=True or self.checkNick!=True:
            self.ui.dialog(self.Dialog,"Have to check everything")
            self.Dialog.show()
        else:count+=1
        if count==11:
            memberData=[self.myId,self.myNickname,self.myPw,self.myPhone,self.myBirth,gender]
            self.db.insertData("user", self.db.rows, memberData)
            self.ui.stackedWidget.setCurrentIndex(0)
            self.ui.dialog(self.Dialog,"Congratulations. You succeeded in signing up")
            self.Dialog.show() 
            self.con.reset(self.ui.joinCheckList,self.ui.widEtc4List,self.ui.loginLineList,self.ui.findIdpageList,self.ui.joinEnterList)


        #config 에 넣었다면 중복을 해결할수 있습니다 
        # scrollEvent -> scroll change event 함수 구분하기 
        
    def scrollChange(self,value):
        X,Y,high2=value[0],value[1],value[2]
        X+=11
        Y+=45
        if self.ui.verticalScrollBar.value()!=0:
            # high=892/self.ui.verticalScrollBar.value()
            high=self.ui.verticalScrollBar.value() 
            high-=high2
            self.ui.MainWindow.setGeometry(X,Y-high*8,892,1985)
            print(Y-high)

    def location(self): # scroll press event 
        X = self.ui.MainWindow.x()
        Y = self.ui.MainWindow.y()
        high=self.ui.verticalScrollBar.value()

        self.locate=[X,Y,high]
        