@echo off
setlocal
set /a count=0

for %%f in (*.txt) do (
    set /a count+=1
)

title Liczba plikow tekstowych: %count%
pause