'''
Created on 21-08-2017

@author: instala
'''

from enum import Enum

class RoverTypeEnum(Enum):
    ROVER_TYPE_2WD                      =       "1001"

class ServoTypeEnum(Enum):
    SERVO_TYPE_SG90                     =       "2001"

class ObstacleTypeEnum(Enum):
    OBSTACLE_HC_SR04                    =       "3001"

class RoverMoveEnum(Enum):
    ROVER_BODY_MOVE_TYPE_LEFT           =       "10001"
    ROVER_BODY_MOVE_TYPE_RIGHT          =       "10002"
    ROVER_BODY_MOVE_TYPE_FORWARD        =       "10003"
    ROVER_BODY_MOVE_TYPE_BACK           =       "10004"
    
class ServoDirectionEnum(Enum):
    SERVO_DIRECTION_HORIZONTAL          =       "20001"
    SERVO_DIRECTION_VERTICAL            =       "20002"
    SERVO_DIRECTION_ALL                 =       "20003"
    
class ObstacleDirectionEnum(Enum):
    OBSTACLE_SENSOR_FRONT               =       "30001"
    
class ServoMovementEnum(Enum):
    SERVO_CLOCKWISE                     =       "21001"     #Horario
    SERVO_COUNTER_CLOCKWISE             =       "21002"     #Antihorario

class CommandsEnum(Enum):
    ROVER_MOVE_MANUAL_BODY              =       "100001"
    ROVER_STOP                          =       "100002"
    YAI_SERIAL_CMD_GET_IP               =       "100003"
    LASER_ACTION                        =       "100004"
    YAI_GET_CURRENT_LOG                 =       "100005"
    SERVO_ACTION_CONTINUOUS             =       "200001"
    SERVO_ACTION_ANGLE                  =       "200002"
    SERVO_STOP                          =       "200003"
    OBSTACLE_READER                     =       "300001"
    GET_SNAPSHOT                        =       "400001"
    
class LogEnum(Enum):
    YAI_LOG_FOLDER                      =       "/logs"

class YaiCommandTypeEnum(Enum):
    YAI_COMMAND_TYPE_SERIAL             =       "SERIAL"
    YAI_COMMAND_TYPE_SPI                =       "SPI"
    YAI_COMMAND_TYPE_WIFI               =       "WIFI"
    YAI_COMMAND_TYPE_RESULT             =       "RESULT"
    YAI_COMMAND_TYPE_NONE               =       "NONE"
    YAI_COMMAND_TYPE_I2C                =       "I2C"
    
class StatusEnum(Enum):
    STATUS_OK                           =       "OK"
    STATUS_NOK                          =       "NOK"

    