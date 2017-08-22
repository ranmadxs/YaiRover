'''
Created on 21-08-2017

@author: esanchez
'''
from roverenum import EnumCommons

class YaiContext():
    def getCommonContext(self):
        context = {'ROVER_STOP': EnumCommons.CommandsEnum.ROVER_STOP.value, 
                   'ROVER_MOVE_MANUAL_BODY' : EnumCommons.CommandsEnum.ROVER_MOVE_MANUAL_BODY.value, 
                   'LASER_ACTION' : EnumCommons.CommandsEnum.LASER_ACTION.value,
                   'SERVO_TYPE_SG90' : EnumCommons.ServoTypeEnum.SERVO_TYPE_SG90.value,
                   'ROVER_BODY_MOVE_TYPE_LEFT' : EnumCommons.RoverMoveEnum.ROVER_BODY_MOVE_TYPE_LEFT.value,
                   'ROVER_BODY_MOVE_TYPE_RIGHT' : EnumCommons.RoverMoveEnum.ROVER_BODY_MOVE_TYPE_RIGHT.value,
                   'ROVER_BODY_MOVE_TYPE_BACK' : EnumCommons.RoverMoveEnum.ROVER_BODY_MOVE_TYPE_BACK.value,
                   'ROVER_BODY_MOVE_TYPE_FORWARD' : EnumCommons.RoverMoveEnum.ROVER_BODY_MOVE_TYPE_FORWARD.value,
                   'ROVER_TYPE_2WD' : EnumCommons.RoverTypeEnum.ROVER_TYPE_2WD.value,
                   'SERVO_ACTION_CONTINUOUS' : EnumCommons.CommandsEnum.SERVO_ACTION_CONTINUOUS.value,
                   'SERVO_STOP' : EnumCommons.CommandsEnum.SERVO_STOP.value,
                   'SERVO_CLOCKWISE' : EnumCommons.ServoMovementEnum.SERVO_CLOCKWISE.value,
                   'SERVO_COUNTER_CLOCKWISE' : EnumCommons.ServoMovementEnum.SERVO_COUNTER_CLOCKWISE.value,
                   'SERVO_DIRECTION_HORIZONTAL' : EnumCommons.ServoDirectionEnum.SERVO_DIRECTION_HORIZONTAL.value,
                   'SERVO_DIRECTION_VERTICAL' : EnumCommons.ServoDirectionEnum.SERVO_DIRECTION_VERTICAL.value,
                   'SERVO_DIRECTION_ALL' : EnumCommons.ServoDirectionEnum.SERVO_DIRECTION_ALL.value,
                }
        return context
    
    