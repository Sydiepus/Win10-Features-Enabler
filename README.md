# Win10-Features-Enabler
This script will enable windows 10 PRO features on the Home edition.  
The purpose of this project is to make the installation of Docker Desktop on Windows 10 Home possible.
# How to use
## Instalation
- Clone the repository
```
git clone https://github.com/Sydiepus/Win10-Features-Enabler.git
```
- Install the requirements
```
cd Win10-Features-Enabler
pip install -r requirements.txt
```
**Administrator privileges are needed**
- Open Run application using the shortcut below
```
windowsKey + R
powershell
ctrl + shitKey + enter
select yes (if promted)
```
You should now have an Administrator powershell
- go to the script path e.g: 'C:\Users\user'
```
cd C:\Users\user
py winFE.py
```
**After you have enabled the features required for docker desktop and changed the values in the registry you can proceed in the installation**
