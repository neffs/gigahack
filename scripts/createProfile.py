#!/usr/bin/env python
# encoding: utf-8
"""
createProfile.py

creates a provider profile for gigaset phones


"""

import sys
import os


FILE = "d_tonline_de.bin"
HEADER = {0: "2402102240",0x40:FILE}
KEY_VALUE = {"S_INFO_SERVICE_URL": "http://info.gigaset.net/info/menu.jsp",
"I_WEB_LABELING": 0}



def int_to_chr(val):
    """docstring for int_to_chr"""
    out = ""
    for i in (24, 16, 8, 0):
        t = (val >> i)%256
        out += chr(t)
    return out

def encodeField(value, header_type=False):
    t = type(value)
    if (t==type(True)):
        #boolean
        h = 3
        value=chr(value)
    elif (t==type(1)):
        h = 4
        value=int_to_chr(value)
    elif (t==type({'a':1}) or t==type((1,2)) or t==type([3,4])):
        a,b = value
        h=1
        value = encodeField(a,2)
        value += encodeField(b)
    elif (t==type("a")):
        h = 5
        value = str(value+'\x00')
    else:
        raise Exception("value not recognized")
    if (header_type!=False):
        out = chr(header_type)
    else:
        out = chr(h)
    out += chr(len(value))
    out += value
    return out


def main():
    f = open(FILE,"wb") 
    for k,v in HEADER.items():
        f.write(encodeField(v,k))
    for a in KEY_VALUE.items():
        f.write(encodeField(a))
    f.close()


if __name__ == '__main__':
    main()

