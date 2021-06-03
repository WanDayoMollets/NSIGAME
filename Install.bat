@echo off


:start
cls

set python_ver=36

cd C:\
cd Program Files/Python
py -m pip install pygame --user
py -m pip install requests --user

pause
exit