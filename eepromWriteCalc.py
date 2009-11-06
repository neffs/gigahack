#!/usr/bin/env python
# encoding: utf-8
"""
untitled.py

Created by David Kreitschmann on 2009-10-04.
Copyright (c) 2009 . All rights reserved.
"""

import sys
import os

TARGET_ADDR = 5183
CLEAR_BITS = 255
#bits die gesetzt werden sollen müssen vorher gecleart werden
SET_BITS = 0
EEPROM_VERSION = 159
KEY = 50074 #C39A



def main():
    print "menu -> einstellungen -> basis -> 94762001"
    print eepromCode(TARGET_ADDR, CLEAR_BITS, SET_BITS, EEPROM_VERSION, KEY)
    

def eepromCode(addr, clear, set, version, key):
    """docstring for calcEepromString"""
    def checksum(array):
        """docstring for get_data_byte"""
        data = 0
        for i in range(1,6):
            word = array[i/2]
            if (i%2==0):
                word = word >> 8
            data += word
            data = data % (1<<8)
            data *= 3
            data = data % (1<<8)
        return data
        
    a = [version,addr,((set%(1<<8)) << 8)| clear%(1<<8)]
    c = checksum(a)
    a[0] = a[0] | c << 8
    
    a[0] = a[0] ^ key 
    a[1] = a[1] ^ a[0]
    a[2] = a[2] ^ a[1]
    
    return " ".join(["%05d"%(n) for n in a])
    #return a
    


if __name__ == '__main__':
    main()

