#!/usr/bin/env python
# encoding: utf-8
"""
eepromWriteCalc.py

Creates EEPROM Codes for (probably all) Gigaset Phones.

The interface was deactivated in Version 02214, don't update if you need this.

"""

import sys
import os

#target address (16 bits)
TARGET_ADDR = 5183 
#mask to change only certain bits (8 bits)
BIT_MASK = 255
#new value (8 bits)
VALUE = 0


#default settings for current IP base stations
EEPROM_VERSION = 159
KEY = 50074 #C39A



def main():
    print "menu -> einstellungen -> basis -> 94762001"
    print eepromCode(TARGET_ADDR, BIT_MASK, VALUE)
    

def eepromCode(addr, bit_mask, value, version=EEPROM_VERSION, key=KEY):
    """
    creates an EEPROM code for a specific Gigaset phone.
    addr: address of the byte to change
    bit_mask: set to 255 if you want to replace all bits
    value: new value, 1 byte
    version: EEPROM version, listed in web interface
    key: seems to be the same for all IP base stations
    btw. the "encryption" scheme is useless, the person who designed it should be fired.
    """
    def checksum(array):
        """
        calculates the checksum
        reconstructed from assembler code
        should be rewritten...
        """
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
        
    a = [version,addr,((value%(1<<8)) << 8)| bit_mask%(1<<8)]
    c = checksum(a)
    a[0] = a[0] | c << 8
    
    a[0] = a[0] ^ key 
    a[1] = a[1] ^ a[0]
    a[2] = a[2] ^ a[1]
    
    return " ".join(["%05d"%(n) for n in a])
    


if __name__ == '__main__':
    main()

