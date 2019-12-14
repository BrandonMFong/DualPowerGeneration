#This is script that connects to our server with winscp and transfers files
& "C:\Program Files (x86)\WinSCP\winscp.com" `
  /command `
    "open sftp://dualpower@146.244.101.140/ -hostkey=`"`"ssh-ed25519 256 4o8fu3NLGOw4DARK0HJLAm5iu6LYt9o0sRFvu+eNF2M=`"`" -privatekey=`"`"B:\COLLEGE\19_20\Fall_19\CompE_496A\SSH\BrandonMFong.ppk`"`" -passphrase=`"`"819295224bfWANG/`"`"" `
    "lcd B:\COLLEGE\19_20\Fall_19\CompE_496A" `
    "cd /home/dualpower/public_ftp/incoming" `
    "put -transfer=automatic FTP" `
    "exit"

$winscpResult = $LastExitCode
if ($winscpResult -eq 0)
{
  Write-Host "Let's get itttttttt" #success
}
else
{
  Write-Host "Bruh" #Failed
}
