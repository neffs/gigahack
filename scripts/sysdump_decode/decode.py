#!/usr/bin/python
# -*- coding: utf-8 -*-
#key is in every firmware file
#search for sysdump.jsp
#it starts with ' and ends with J
#save the key in file named key


BLOCK_SIZE = 32

from Crypto.Cipher import AES



def main():
    filename = "in"
    keyfilename = "key"
    targetfilename = "out"
    f = open(keyfilename, "rb")
    key = f.readline()
    f.close()
    cipher = AES.new(key, AES.MODE_ECB)
    f = open(filename, "rb")
    ciphertext = f.read()
    f.close()
    
    f = open(targetfilename, "wb")
    msg = cipher.decrypt(ciphertext)
    f.write(msg)
    f.close()
	
	
if __name__ == '__main__':
    main()
