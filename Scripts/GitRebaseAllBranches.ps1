# Script to rebase all branches against master

Push-Location ($PSScriptRoot| Split-Path -Parent )
    $GitBranches = [System.Collections.ArrayList]::new(); 
    Get-ChildItem .\.git\refs\heads\ -r |
        Where-Object{$_.Mode -eq "-a----"} |
            ForEach-Object{$GitBranches.Add($_.FullName);}

    $i = 0;
    $BaseDirToRemove = $GitBranches[$i];
    while ($true)
    {
        # when we reach heads
        if (($BaseDirToRemove | Split-Path -Leaf) -eq "heads"){break;}
        # when we pass heads
        elseif(($BaseDirToRemove.Equals(($BaseDirToRemove | Split-Path -Qualifier))) -and ($i -ne $GitBranches.Count))
        {
            # Skip to next item on the list
            $i++;
            $BaseDirToRemove = $GitBranches[$i];
        }
        $BaseDirToRemove | Split-Path -Parent |ForEach-Object{$BaseDirToRemove = $_;}
    }

    for ($i = 0; $i -lt $GitBranches.Count; $i++)
    {
        
    }


Pop-Location