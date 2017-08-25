'''
Created on 22-08-2017

@author: instala
'''
from model import AbstractUtilDTO
from roverenum import EnumCommons
from lib.logger import logger as log

class YaiNetwork(AbstractUtilDTO):
    broadcast = None
    netmask = None
    addr = None
    mac = None

class YaiCommand(AbstractUtilDTO):
    execute = False
    printCmd = False
    propagate = False
    message = ""    
    type = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value    
    TIPO_CALL = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    COMMAND = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    P1 = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    P2 = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    P3 = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    P4 = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    P5 = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    P6 = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value    
    P7 = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    address = 0x00
    json = ""

    def __resToObject__(self, msgList = None):
        msg = msgList[0]
        self.message = msg
        resMsgArray = msg.split(",")
        self.type = resMsgArray[0]        
        self.COMMAND = resMsgArray[1]
        self.P1 = resMsgArray[2]
        self.P2 = resMsgArray[3]
        self.P3 = resMsgArray[4]
        self.P4 = resMsgArray[5]
        self.P5 = resMsgArray[6]
        self.P6 = resMsgArray[7]
        self.P7 = resMsgArray[8]
    
    
class YaiResult(AbstractUtilDTO):
    status = None
    content = ""
    message = ""
    R1 = None
    R2 = None
    R3 = None
    R4 = None
    type = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value
    
    def __resToObject__(self, msg = None):
        msg = msg.replace("#", "")
        resMsgArray = msg.split(",")
        self.message = msg
        self.type = resMsgArray[0]
        countR = 0     
        for r in resMsgArray:
            if countR > 0:
                setattr(self, "R%d"%countR, r)
            countR = countR + 1        