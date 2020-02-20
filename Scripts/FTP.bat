@echo off
echo.
rem This allows the script to run on any machine in any directory
set GitRepoPath=%~dp0
rem -9 strips the \Scripts\ from the string
set GitRepoPath=%GitRepoPath:~0,-9% 
set FTPPath=%GitRepoPath:~0, -1%\FTP
echo "The path to DualPowerGeneration gitrepo:"
echo %GitRepoPath%
echo.
echo "The path to local FTP output folder:"
echo %FTPPath%
echo.


rem The following is a command inputted for the winscp to send everything from our FTP folder to the server
"C:\Program Files (x86)\WinSCP\winscp.com" ^
  /command ^
    "open sftp://dualpower@146.244.101.140/ -hostkey=""ssh-ed25519 256 4o8fu3NLGOw4DARK0HJLAm5iu6LYt9o0sRFvu+eNF2M="" -privatekey=""B:\COLLEGE\19_20\Fall_19\CompE_496A\SSH\BrandonMFong.ppk"" -passphrase=""819295224bfWANG/""" ^
    "lcd %GitRepoPath%" ^
    "cd /home/dualpower/public_ftp/incoming" ^
    "put FTP/Outbound" ^
    "exit"
rem TODO 'put' only .csv files in the current directory
set WINSCP_RESULT=%ERRORLEVEL%
if %WINSCP_RESULT% equ 0 (
  rem successful ftp
  echo Let's get itttttttt
) else (
  rem failed ftp
  echo Bruh 
  dir 
)

echo.
exit /b %WINSCP_RESULT%