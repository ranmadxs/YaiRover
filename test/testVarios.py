'''
Created on 15-08-2017

@author: esanchez
'''
MAX_I2C_CONTENT = 26
YAI_COMMAND_TYPE_I2C = "I2C"


def buildI2Cpackage(command, total, part) :
    respCommand = "%s%s%s%s" % (YAI_COMMAND_TYPE_I2C, part, total, command);
    return respCommand

def sendI2CCommand(cmd):
        print cmd
        totalParts = 1;
        if (len(cmd) > MAX_I2C_CONTENT) :
            totalParts = 2;
        cmd1 = cmd[:MAX_I2C_CONTENT]
        #print cmd1
        cmd1 = buildI2Cpackage(cmd1, totalParts, 1)
        print cmd1

        if (totalParts > 1) :
            cmd2 = cmd[MAX_I2C_CONTENT:]
            #print cmd2
            cmd2 = buildI2Cpackage(cmd2, totalParts, 2)
            print cmd2
        
sendI2CCommand("SERIAL,100001,1001,0,0,10003,None,None,None")