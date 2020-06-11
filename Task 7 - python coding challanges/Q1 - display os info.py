#!/usr/bin/env python


import os 
import platform
def checkos():
    '''Checks the current OS systems, versions and gives you the current working directory'''
    print(platform.system())
    print(platform.release())
    print(platform.version())
    print(platform.machine())
    print(os.getcwd())


if __name__ == "__main__":
    checkos()
