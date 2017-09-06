'''
Created on 21-08-2017

@author: esanchez
'''
from roverenum.EnumCommons import ServoDirectionEnum, CommandsEnum, RoverMoveEnum, ServoTypeEnum, RoverTypeEnum, ServoMovementEnum
from roverenum.EnumCommunicator import JoystickEnum

class YaiContext():
    def getCommonContext(self):
        context = {'ROVER_STOP': CommandsEnum.ROVER_STOP.value, 
                   'ROVER_MOVE_MANUAL_BODY' : CommandsEnum.ROVER_MOVE_MANUAL_BODY.value, 
                   'LASER_ACTION' : CommandsEnum.LASER_ACTION.value,
                   'SERVO_TYPE_SG90' : ServoTypeEnum.SERVO_TYPE_SG90.value,
                   'ROVER_BODY_MOVE_TYPE_LEFT' : RoverMoveEnum.ROVER_BODY_MOVE_TYPE_LEFT.value,
                   'ROVER_BODY_MOVE_TYPE_RIGHT' : RoverMoveEnum.ROVER_BODY_MOVE_TYPE_RIGHT.value,
                   'ROVER_BODY_MOVE_TYPE_BACK' : RoverMoveEnum.ROVER_BODY_MOVE_TYPE_BACK.value,
                   'ROVER_BODY_MOVE_TYPE_FORWARD' : RoverMoveEnum.ROVER_BODY_MOVE_TYPE_FORWARD.value,
                   'ROVER_TYPE_2WD' : RoverTypeEnum.ROVER_TYPE_2WD.value,
                   'SERVO_ACTION_CONTINUOUS' : CommandsEnum.SERVO_ACTION_CONTINUOUS.value,
                   'SERVO_STOP' : CommandsEnum.SERVO_STOP.value,
                   'SERVO_CLOCKWISE' : ServoMovementEnum.SERVO_CLOCKWISE.value,
                   'SERVO_COUNTER_CLOCKWISE' : ServoMovementEnum.SERVO_COUNTER_CLOCKWISE.value,
                   'SERVO_DIRECTION_HORIZONTAL' : ServoDirectionEnum.SERVO_DIRECTION_HORIZONTAL.value,
                   'SERVO_DIRECTION_VERTICAL' : ServoDirectionEnum.SERVO_DIRECTION_VERTICAL.value,
                   'SERVO_DIRECTION_ALL' : ServoDirectionEnum.SERVO_DIRECTION_ALL.value,
                   'TYPE_MOTOR' : JoystickEnum.TYPE_MOTOR.value,
                   'TYPE_SERVO' : JoystickEnum.TYPE_SERVO.value,
                }
        return context
    
    