#! /usr/bin/python

import os
from pyfiglet import Figlet

def fetch(pkg) :
    cmd = f"dir /b %SystemRoot%\servicing\Packages\*{pkg}*.mum >{pkg}.txt"
    os.system(f'cmd /c {cmd}')
    return True

def download(pkg) :
    to_download = open(f"{pkg}.txt", "r")
    to_download_line = to_download.readlines()
    q = len(to_download_line)
    l = 1
    os.system(f'dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\{to_download_line[0]}"')
    print( f'0 / {q}')
    os.system(f'dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\{to_download_line[1]}"')
    print(f'1 / {q}')
    try :
        while l < q :
            l += 1
            os.system(f'dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\{to_download_line[l]}"')
            print(f'{l} / {q}')
    except IndexError :
        print("all the packages have been added")
    return True

cf = Figlet(font="slant")
c = cf.renderText("""WIN  10 
Features Enabler""")
print(c)
print("the available options are below:")
print("""1- "Docker" To install required features for Docker Desktop
2- Or enter the feature you want to enable e.g: containers """)
user_input = str(input("Enter your desired option: "))

if user_input == "Docker" :
    fetch("Hyper-V")
    download("Hyper-V")
    fetch("containers")
    download("containers")
    print("Now restart your PC")
    print("and then change the EditionID subkey in the registry located at 'Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion' from core to 'Professional'")
else :
    fetch(user_input)
    download(user_input)