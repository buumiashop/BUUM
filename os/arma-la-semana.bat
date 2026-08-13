@echo off
REM BUUM OS - el CEO arma la semana (revisa arsenal -> 4 filtros -> semana.js)
cd /d "%~dp0\..\buumia-tienda\marketing"
"C:\Users\playg\Tools\Miniconda\python.exe" rutina_semanal.py --all >> "%~dp0\_rutina.log" 2>&1
