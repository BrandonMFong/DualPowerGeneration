#Credits http://powershell.one/tricks/input-devices/detect-key-press
function Test-KeyPress
{
    param
    (
        [Parameter(Mandatory)]
        [ConsoleKey]
        $Key,

        [System.ConsoleModifiers]
        $ModifierKey = 0
    )
    if ([Console]::KeyAvailable)
    {
        $pressedKey = [Console]::ReadKey($true)

        $isPressedKey = $key -eq $pressedKey.Key
        if ($isPressedKey)
        {
            return ($pressedKey.Modifiers -eq $ModifierKey);
        }
        else
        {
            return $false
        }
    }
}

function CheckFTPExitCode
{
    Param($GetFromNokita,$PutToDPG)
    Write-Host "`n`n";
    if (($GetFromNokita -eq 0) -and ($PutToDPG -eq 0))
    {
        Write-Host "Redirect Successful" -ForegroundColor Green;
    }
    elseif(($GetFromNokita -eq 1) -and ($PutToDPG -eq 0))
    {
        Write-Host "Error getting files from Nokita" -ForegroundColor Red;
        Write-Host "Success putting files to DPG" -ForegroundColor Green;
    }
    elseif(($GetFromNokita -eq 0) -and ($PutToDPG -eq 1))
    {
        Write-Host "Success getting files from Nokita" -ForegroundColor Green;
        Write-Host "Error putting files to DPG" -ForegroundColor Red;
    }
    else
    {
        Write-Host "Error in both transfers" -BackgroundColor Yellow -ForegroundColor Red;
    }
    Write-Host "`n`n";
}