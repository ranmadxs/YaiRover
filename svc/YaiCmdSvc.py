'''
Created on 22-08-2017

@author: instala
'''
from lib.logger import logger as log
from model.vo import YaiCommand, YaiResult
from roverenum import EnumCommons
from svc.YaiCommunicatorSvc import I2c
from utils.exception import YaiRoverException
import socket
from uuid import getnode as get_mac

class YaiCommandSvc():
    
    yaiCommunicator = I2c()
    
    def buildMessage(self, yaiCommand = None):
    
        if yaiCommand is None:
            raise YaiRoverException("yaiCommand no puede ser nulo")
    
        if yaiCommand.type is None:
            raise YaiRoverException("yaiCommand.type no puede ser nulo")
    
        yaiCommand.message = "%s,%s,%s,%s,%s,%s,%s,%s,%s" %(yaiCommand.TIPO_CALL, yaiCommand.COMMAND, 
                                                      yaiCommand.P1, yaiCommand.P2, yaiCommand.P3, yaiCommand.P4, 
                                                      yaiCommand.P5, yaiCommand.P6, yaiCommand.P7)
        
        yaiCommand.execute = False
        
        if((yaiCommand.type == EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_SERIAL.value) 
            or (yaiCommand.type == EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_I2C.value)):
            yaiCommand.execute = True
            
            
        return yaiCommand
        
        # if (not yaiCommand is None): <- debo tirar trow en este caso
    
    def execute(self, yaiCommand = None):
        
        if yaiCommand is None:
            raise YaiRoverException("yaiCommand no puede ser nulo")
    
        if yaiCommand.execute is None:
            raise YaiRoverException("yaiCommand.execute no puede ser nulo")      
        
        log.debug("Execute Command")
        propagate = False;
        content = "Command not found";
        resultStr = EnumCommons.StatusEnum.STATUS_NOK.value;
        
        yaiResult = YaiResult()
         
        if(yaiCommand.execute):
            #self.yaiCommunicator.sendCommand("I2C,100001,1001,0,0,10002,None,None,None", I2c.CLIENT_ADDR_YAI_MOTOR)            
            command = yaiCommand.COMMAND
            
            log.debug("cmd::" + command)
            
            if command is None:
                raise YaiRoverException("yaiCommand.COMMAND no puede ser nulo")
            
            if(command == EnumCommons.CommandsEnum.YAI_GET_CURRENT_LOG.value):
                raise YaiRoverException("cmd YAI_GET_CURRENT_LOG No ha sido implementado")
            
            if(command == EnumCommons.CommandsEnum.YAI_SERIAL_CMD_GET_IP.value):
                log.debug("ejecutando get IP")
                resultStr = EnumCommons.StatusEnum.STATUS_OK.value;
                clientIp = socket.gethostbyname(socket.gethostname())
                content = "{\"CLIENT_IP\":\""+ clientIp+"\""
                if ((not yaiCommand.P1 is None) and (yaiCommand.P1.lower() == "true")):
                    address = get_mac()   
                    mac = "".join(c + ":" if i % 2 else c for i, c in enumerate(hex(address)[2:].zfill(12)))[:-1]                 
                    content += ", \"MAC\":\"%s\"" % mac         
                content += "}"
                
        
        yaiResult.content = content
        yaiResult.status = resultStr
        yaiResult.propagate = propagate
        return yaiResult