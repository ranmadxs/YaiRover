'''
Created on 23-08-2017

@author: esanchez
'''

from model.vo import YaiResult

strRes = "RESULT,OK,RIGH##################"

yaiResult = YaiResult()
yaiResult.__resToObject__(strRes)
print yaiResult.__str__()