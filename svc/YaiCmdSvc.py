#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 22-08-2017

@author: instala
'''
import time
from lib.logger import logger as log
from model.vo import YaiCommand, YaiResult
from roverenum import EnumCommons, EnumCommunicator
from svc.YaiCommunicatorSvc import I2c, YaiSerial
from utils.exception import YaiRoverException
from svc.NetworkSvc import YaiNetworkSvc

class YaiCommandSvc():
    
    i2cSvc = I2c()
    yaiSerialSvc = YaiSerial()
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
        
        log.info("Execute Command")
        propagate = False;
        content = "Command not found";
        resultStr = EnumCommons.StatusEnum.STATUS_NOK.value;
        responseCommand = None
        
        yaiResult = YaiResult()
         
        if(yaiCommand.execute):
            #self.yaiCommunicator.sendCommand("I2C,100001,1001,0,0,10002,None,None,None", I2c.CLIENT_ADDR_YAI_MOTOR)            
            command = yaiCommand.COMMAND
            
            log.info("cmd::" + command)
            
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
                if (not yaiCommand.P2 is None) and (yaiCommand.P2.isnumeric()):
                    tiempoStop = int(yaiCommand.P2)
                    time.sleep(tiempoStop)

                yaiCommand.address = EnumCommunicator.I2CEnum.I2C_CLIENT_YAI_SERVO.value                
                log.debug("antes de propagar YaiMotor")
                yaiResult = self.propagateCommand(yaiCommand)
                log.debug("despues de propagar YaiMotor")        

            if ((command == EnumCommons.CommandsEnum.LASER_ACTION.value) 
                or (command == EnumCommons.CommandsEnum.ROVER_STOP.value)
                or (command == EnumCommons.CommandsEnum.ROVER_MOVE_MANUAL_BODY.value)):
                resultStr = EnumCommons.StatusEnum.STATUS_OK.value
                propagate = True
                if (not yaiCommand.P2 is None) and (yaiCommand.P2.isnumeric()):
                    tiempoStop = int(yaiCommand.P2)
                    time.sleep(tiempoStop)

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

    def propagateCommand(self, yaiCommand):
        response = None
        yaiResult = YaiResult()
        yaiResult.status = EnumCommons.StatusEnum.STATUS_NOK.value
        if (yaiCommand.type == EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_SERIAL.value):
            log.debug("SERIAL >> Propagate");
            yaiResult.status = EnumCommons.StatusEnum.STATUS_OK.value
            yaiResult.message = yaiCommand.message
            yaiResult.type = EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_RESULT.value
            responseCommand = self.yaiSerialSvc.sendCommand(yaiCommand.message, yaiCommand.serialPort)
            yaiResult.__resToObject__(responseCommand)
        
        if (yaiCommand.type == EnumCommons.YaiCommandTypeEnum.YAI_COMMAND_TYPE_I2C.value):
            log.debug("I2C >> Propagate");
            yaiResult.status = EnumCommons.StatusEnum.STATUS_OK.value
            responseCommand = self.i2cSvc.sendCommand(yaiCommand.message, yaiCommand.address)
            yaiResult.__resToObject__(responseCommand)
                    
        return yaiResult