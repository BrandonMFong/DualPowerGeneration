Import-Module $($PSScriptRoot + "\Modules\Redirect.psm1");
[xml]$ScriptsXML = Get-Content $($PSScriptRoot + '\..\Config\EarthWindFire\Scripts.xml');
[System.Object[]]$RedirectJson = Get-Content -Raw -Path $($PSScriptRoot + "\..\Config\EarthWindFire\Redirect.json") | ConvertFrom-Json 

[bool]$key = $false;

Write-Host "Entering script.  Press Q to exit program`n`n" -ForegroundColor Green;
while(!$key)
{
    # FTP Get
    & "C:\\Program Files (x86)\\WinSCP\\winscp.com" `
    /log="B:\FTP_Get.log" /ini=nul `
    /command `
        "open $($RedirectJson.Redirect.Get.Site) -hostkey=`"`"$($RedirectJson.Redirect.Get.HostKey)`"`"" `
        "cd $($RedirectJson.Redirect.Get.CD)" `
        "lcd $($RedirectJson.Redirect.Get.LCD)" `
        "get Outbound" `
        "exit"
    $GetFromNokita = $LastExitCode
    Write-Host "`n`n";

    # FTP Put
    & "C:\\Program Files (x86)\\WinSCP\\winscp.com" `
    /log="B:\FTP_Put.log" /ini=nul `
    /command `
        "open $($RedirectJson.Redirect.Put.Site) -hostkey=`"`"$($RedirectJson.Redirect.Put.HostKey)`"`" -privatekey=`"`"$($RedirectJson.Redirect.Put.PrivateKey)`"`" -passphrase=`"`"$($RedirectJson.Redirect.Put.PassPhrase)`"`"" `
        "lcd $($RedirectJson.Redirect.Put.LCD)" `
        "cd $($RedirectJson.Redirect.Put.CD)" `
        "put Outbound" `
        "exit"


    $PutToDPG = $LastExitCode

    # Checks FTP exit code
    CheckFTPExitCode -GetFromNokita $GetFromNokita -PutToDPG $PutToDPG

    # Archive
    Write-Host "Archiving files" -ForegroundColor Cyan;
    if(!(Test-Path $ScriptsXML.Scripts.Redirect.ArchivePath))
    {
        mkdir $ScriptsXML.Scripts.Redirect.ArchivePath;
    }

    try 
    {
        Move-Item $($ScriptsXML.Scripts.Redirect.Path + "\*.*") $ScriptsXML.Scripts.Redirect.ArchivePath -ea stop;
    }
    catch [System.IO.IOException]
    {
        Write-Warning "File already exists"
    }
    finally 
    {
        Write-Host `n;
        Remove-Item $($ScriptsXML.Scripts.Redirect.Path + "\*.*") -Verbose;
        Write-Host `n;
    }

    # Zips if there are more than 10 files in the archive directory
    if((Get-ChildItem $ScriptsXML.Scripts.Redirect.ArchivePath|Measure-Object).Count -gt 10)
    {
        [string]$ArchiveName = $ScriptsXML.Scripts.Redirect.ArchivePath + "\Archive";
        Compress-Archive $($ScriptsXML.Scripts.Redirect.ArchivePath + "\*" + $ScriptsXML.Scripts.Redirect.FileExt) $ArchiveName -Update;
        Remove-Item $($ScriptsXML.Scripts.Redirect.ArchivePath + "\*" + $ScriptsXML.Scripts.Redirect.FileExt);
    }

    # Sleep
    start-sleep($ScriptsXML.Scripts.Redirect.NoFTPSleep);
    
    $key = Test-KeyPress -Key Q; # test key
}