@echo off
title Woolvers X Industries
chcp 65001 >nul
mode con: cols=220 lines=40

:: Основной текст
color 05
cls
timeout /t 1 >nul
echo     ██╗    ██╗ ██████╗  ██████╗ ██╗     ██╗   ██╗███████╗██████╗ ███████╗    ██╗  ██╗    ██╗███╗   ██╗██████╗ ██╗   ██╗███████╗████████╗██████╗ ██╗███████╗███████╗
timeout /t 1 >nul
color 0D
echo     ██║    ██║██╔═══██╗██╔═══██╗██║     ██║   ██║██╔════╝██╔══██╗██╔════╝    ╚██╗██╔╝    ██║████╗  ██║██╔══██╗██║   ██║██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝██╔════╝
timeout /t 1 >nul
color 09
echo     ██║ █╗ ██║██║   ██║██║   ██║██║     ██║   ██║█████╗  ██████╔╝███████╗     ╚███╔╝     ██║██╔██╗ ██║██║  ██║██║   ██║███████╗   ██║   ██████╔╝██║█████╗  ███████╗
timeout /t 1 >nul
color 0B
echo     ██║███╗██║██║   ██║██║   ██║██║     ╚██╗ ██╔╝██╔══╝  ██╔══██╗╚════██║     ██╔██╗     ██║██║╚██╗██║██║  ██║██║   ██║╚════██║   ██║   ██╔══██╗██║██╔══╝  ╚════██║
timeout /t 1 >nul
color 0A
echo     ╚███╔███╔╝╚██████╔╝╚██████╔╝███████╗ ╚████╔╝ ███████╗██║  ██║███████║    ██╔╝ ██╗    ██║██║ ╚████║██████╔╝╚██████╔╝███████║   ██║   ██║  ██║██║███████╗███████║
echo      ╚══╝╚══╝  ╚═════╝  ╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═╝    ╚═╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝
timeout /t 1 >nul
echo.
echo ===============================================================================                   Information about multitool
echo                         ███████████████████████████████████████████████████████                   Woolvers X Hack is a custom tool that automates tasks like pinging IPs, tracing routes, and scanning 
echo                         █                                                     █                   ports. It also lets users run Python scripts for security testing, like SQL injection and brute force 
echo                         █        Welcome to Woolvers X Industries Multitool   █                   attacks. The tool is designed for easy use with a simple menu interface.
echo                         █                                                     █                   
echo                         ███████████████████████████████████████████████████████                   Tips
echo ===============================================================================                   Ping an IP Address: Pings an IP to check availability. Enter IP and press Enter. Use to check server reachability.
echo                                                                                                   Trace a Route: Shows the path to a server/IP. Enter IP or domain. Use for network troubleshooting.
echo                                                                                                   Scan Ports: Scans common ports (80, 443). Enter IP. Use to check open ports on a server.
echo                                                                                                   Run Python Scripts: Runs Python security scripts. Select and run a script. Use for vulnerability testing.
echo                                                                                                   Show System Info: Displays system info. View system details. Use to check system specs.
echo.

:menu
color 0A
echo ===============================================================================                  Information about company
echo   ███████████████████████████████████████████████████████████████████████████                    "Woolvers X Industries" is a company specializing in the development of advanced hacking tools. The 
echo   █  [1] Ping an IP Address                                                 █                    company focuses on creating software that aids in cybersecurity testing, with tools for tasks such as
echo   █  [2] Trace a Route                                                      █                    network scanning, route tracing, and vulnerability assessments. Woolvers X Industries aims to 
echo   █  [3] Scan Ports                                                         █                    provide users with efficient and effective tools for security professionals and researchers.
echo   █  [4] Run Python Scripts                                                 █
echo   █  [5] Show System Info                                                   █                   
echo   █  [6] Exit                                                               █
echo   ███████████████████████████████████████████████████████████████████████████
echo ===============================================================================
echo.
echo Select an option by typing the corresponding number and pressing Enter.
echo.
set /p choice="Choose an option: "

if "%choice%"=="1" goto ping
if "%choice%"=="2" goto tracert
if "%choice%"=="3" goto scan_ports
if "%choice%"=="4" goto python_scripts
if "%choice%"=="5" goto system_info
if "%choice%"=="6" exit
goto menu

:ping
cls
color 0D
echo Enter the IP Address to ping:
set /p ip="IP: "
ping %ip%
pause
goto menu

:tracert
cls
color 0C
echo Enter the target for route tracing:
set /p target="Target: "
tracert %target%
pause
goto menu

:scan_ports
cls
color 0E
echo Enter the IP Address to scan ports:
set /p ip="IP: "
echo Scanning ports on %ip%...
powershell -Command "Test-NetConnection -ComputerName %ip% -Port 80; Test-NetConnection -ComputerName %ip% -Port 443;"
pause
goto menu

:python_scripts
cls
color 0B
echo ===============================================================================
echo   ███████████████████████████████████████████████████████████████████████████
echo   █  [1] SQL Injection Test                                                 █
echo   █  [2] Directory Brute Force                                              █
echo   █  [3] Back to Main Menu                                                  █
echo   ███████████████████████████████████████████████████████████████████████████
echo ===============================================================================
set /p pychoice="Choose a Python script: "

if "%pychoice%"=="1" python sql_injection_test.py
if "%pychoice%"=="2" python dir_bruteforce.py
if "%pychoice%"=="3" goto menu
goto python_scripts

:system_info
cls
color 0A
systeminfo
pause
goto menu