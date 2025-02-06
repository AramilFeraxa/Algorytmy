@echo off
if "%~2"=="" (
    echo Uzycie: skrypt.bat "wyraz1" "wyraz2"
    exit /b
)

set "wyraz1=%~1"
set "wyraz2=%~2"
set "plik=test.txt"

if not exist "%plik%" (
    echo Plik %plik% nie istnieje!
    exit /b
)

(for /f "usebackq delims=" %%l in ("%plik%") do (
    set "linia=%%l"
    setlocal enabledelayedexpansion
    echo !linia:%wyraz1%=%wyraz2%!
    endlocal
)) > temp.txt
move /y temp.txt "%plik%"
echo Zamieniono "%wyraz1%" na "%wyraz2%" w pliku %plik%.
pause