'''
Created on 22-08-2017

@author: esanchez
'''
import socket
from uuid import getnode as get_mac
import uuid

hdr="\xff"*6
mac=uuid.getnode()
txt="%012X"%mac
as_b=[int("".join(x),16) for x in map(None,*(txt[::2],txt[1::2]))]
as_s="".join(chr(b) for b in as_b)
out=hdr+as_s

print out

def get_mac2():
  mac_num = hex(uuid.getnode()).replace('0x', '').upper()
  mac = '-'.join(mac_num[i : i + 2] for i in range(0, 11, 2))
  return mac

print get_mac2()

clientIp = socket.gethostbyname(socket.gethostname())
print clientIp

address = get_mac()
h = iter(hex(address)[2:].zfill(12))
strH = ":".join(i + next(h) for i in h)
print strH


h = hex(address)[2:].zfill(12)
strH = ":".join(i + j for i, j in zip(h[::2], h[1::2]))
print strH
'''
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

ip = get_ip_address('eth0')  # '192.168.0.110'
print ip
'''

import netifaces

ifaces = netifaces.interfaces()
print ifaces


for interface in netifaces.interfaces():
    addrs = netifaces.ifaddresses(interface)
    try:
        print addrs[netifaces.AF_INET][0]
        print addrs[netifaces.AF_LINK][0]
        
    except KeyError:
        pass
    #addr = netifaces.ifaddresses(interface)[netifaces.AF_INET]
    #addr = networkDevice[netifaces][0]['addr']
    #print addr
    #print addrs

print netifaces.AF_LINK
print netifaces.AF_INET
print netifaces.ifaddresses('{53DB9CCE-4728-41E8-ADC4-F6634F394D25}')
#ip = netifaces.ifaddresses('{53DB9CCE-4728-41E8-ADC4-F6634F394D25}')[netifaces.AF_INET][0]['addr']
#print ip

