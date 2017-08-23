'''
Created on 23-08-2017

@author: esanchez
'''
import netifaces
from model.vo import YaiNetwork

class YaiNetworkSvc():
    
    def getIps(self):
        networks = []
        for interface in netifaces.interfaces():
            addrs = netifaces.ifaddresses(interface)
            try:
                yaiNetwork = YaiNetwork(addrs[netifaces.AF_INET][0])
                
                macStr = addrs[netifaces.AF_LINK][0]['addr']
                yaiNetwork.mac = macStr
                if len(macStr) > 1:
                    networks.append(yaiNetwork)
                #print addrs[netifaces.AF_INET][0]
                #print addrs[netifaces.AF_LINK][0]
        
            except KeyError:
                pass
            
        return networks