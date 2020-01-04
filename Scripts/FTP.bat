@echo off

set path=%~dp0
echo "The path to DualPowerGeneration gitrepo:"
echo %path:~0,-9% 

"C:\Program Files (x86)\WinSCP\winscp.com" ^
  /command ^
    "open sftp://dualpower@146.244.101.140/ -hostkey=""ssh-ed25519 256 4o8fu3NLGOw4DARK0HJLAm5iu6LYt9o0sRFvu+eNF2M="" -privatekey=""B:\COLLEGE\19_20\Fall_19\CompE_496A\SSH\BrandonMFong.ppk"" -passphrase=""819295224bfWANG/""" ^
    "lcd %path:~0,-9%" ^
    "cd /home/dualpower/public_ftp/incoming" ^
    "put FTP" ^
    "exit"

set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  echo Success
) else (
  echo Error
)

exit /b %WINSCP_RESULT%