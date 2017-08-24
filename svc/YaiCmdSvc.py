'''
Created on 22-08-2017

@author: instala
'''
import time
from lib.logger import logger as log
from model.vo import YaiCommand, YaiResult
from roverenum import EnumCommons, EnumCommunicator
from svc.YaiCommunicatorSvc import I2c
from utils.exception import YaiRoverException
from svc.NetworkSvc import YaiNetworkSvc

class YaiCommandSvc():
    
    yaiCommunicator = I2c()
    yaiNetworkSvc = YaiNetworkSvc()
    
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
        responseCommand = None
        
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
                yaiResult.type = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_RESULT.value
                log.debug("ejecutando get IP")
                resultStr = EnumCommons.StatusEnum.STATUS_OK.value;
                clientIp = self.yaiNetworkSvc.getIps()
                content = "["
                content += ",". join(str(e) for e in clientIp)     
                content += "]"
                
            if (command == EnumCommons.CommandsEnum.OBSTACLE_READER.value):
                resultStr = EnumCommons.StatusEnum.STATUS_OK.value
                propagate = True
                yaiCommand.address = EnumCommunicator.I2CEnum.I2C_CLIENT_YAI_MOTOR.value
                yaiResult = self.propagateCommand(yaiCommand)               

            #Comandos que se propagan con delay
            if ((command == EnumCommons.CommandsEnum.SERVO_STOP.value) 
                or (command == EnumCommons.CommandsEnum.SERVO_ACTION_CONTINUOUS.value)
                or (command == EnumCommons.CommandsEnum.SERVO_ACTION_ANGLE.value)):
                resultStr = EnumCommons.StatusEnum.STATUS_OK.value
                propagate = True
                tiempoStop = int(yaiCommand.p2)

                yaiCommand.address = EnumCommunicator.I2CEnum.I2C_CLIENT_YAI_SERVO.value
                time.sleep(tiempoStop)
                log.debug("antes de propagar YaiServo")
                yaiResult = self.propagateCommand(yaiCommand)
                log.debug("antes de propagar YaiServo")        

            if ((command == EnumCommons.CommandsEnum.LASER_ACTION.value) 
                or (command == EnumCommons.CommandsEnum.ROVER_STOP.value)
                or (command == EnumCommons.CommandsEnum.ROVER_MOVE_MANUAL_BODY.value)):
                resultStr = EnumCommons.StatusEnum.STATUS_OK.value
                propagate = True
                tiempoStop = int(yaiCommand.P2)

                yaiCommand.address = EnumCommunicator.I2CEnum.I2C_CLIENT_YAI_MOTOR.value
                time.sleep(tiempoStop)
                log.debug("antes de propagar YaiMotor")
                yaiResult = self.propagateCommand(yaiCommand)
                log.debug("despues de propagar YaiMotor")                                                    
                
        if propagate :
            content = "{\"propagate\": \"%s\"}" % yaiCommand.type
        
        yaiResult.content = content
        yaiResult.status = resultStr
        yaiResult.propagate = propagate
        return yaiResult

    def resToObject(self, yaiResult = None, msg = None):
        log.info(msg)
        msg = msg.replace("#", "")
        log.info(msg)
        resMsgArray = msg.split(",")
        log.info(resMsgArray)
        yaiResult.message = msg
        yaiResult.type = resMsgArray[0]
        countR = 0     
        for r in resMsgArray:
            if countR > 0:
                setattr(yaiResult, "R%d"%countR, r)
            countR = countR + 1                                        
        log.info(msg)   
        return yaiResult

    def propagateCommand(self, yaiCommand):
        response = None
        yaiResult = YaiResult()
        yaiResult.status = EnumCommons.StatusEnum.STATUS_NOK.value
        if (yaiCommand.type == EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_SERIAL.value):
            log.info("SERIAL >> ");
            yaiResult.status = EnumCommons.StatusEnum.STATUS_OK.value
            yaiResult.message = yaiCommand.message
            yaiResult.type = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_RESULT.value
            raise YaiRoverException("propagateCommand SERIAL not implemented yet")
        
        if (yaiCommand.type == EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_I2C.value):
            log.info("I2C >> ");
            yaiResult.status = EnumCommons.StatusEnum.STATUS_OK.value
            responseCommand = self.yaiCommunicator.sendCommand(yaiCommand.message, yaiCommand.address)
            yaiResult = self.resToObject(responseCommand, yaiResult)
            log.info("Saliendo de I2c XDDD")
                    
        return yaiResult