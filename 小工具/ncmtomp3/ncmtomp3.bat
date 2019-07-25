@echo off&&setlocal enabledelayedexpansion

for %%i in (*.ncm) do (
call  ncmdump-windows-amd64.exe "%%i"
)
endlocal 