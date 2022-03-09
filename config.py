from PyQt5.QtGui import *

class Config:
   
    def reset(self,joinCheckList,widEtc4List,loginLineList,findIdpageList,joinEnterList):
        for index in range(0,len(joinCheckList)):
            if joinCheckList[index].isChecked()==True:
                joinCheckList[index].toggle()
        if widEtc4List[2].isChecked()==True:
            widEtc4List[2].toggle()
        for index in range(0,len(loginLineList)):
            loginLineList[index].setText("")
        widEtc4List[0].setText("")
        widEtc4List[1].setText("")
        findIdpageList[0].setText("")
        findIdpageList[2].setText("")
        for index in range(0,len(joinEnterList)):
            joinEnterList[index].setText("")


