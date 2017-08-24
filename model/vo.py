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
    
class YaiResult(AbstractUtilDTO):
    status = None
    content = ""
    message = ""
    R1 = None
    R2 = None
    R3 = None
    R4 = None
    type = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_NONE.value   
        