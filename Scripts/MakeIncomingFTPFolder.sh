# Remotely creating correct FTP folders

set -e

pushd ~/
    mkdir public_ftp;
    cd public_ftp;
    mkdir incoming;
    cd incoming;
    mkdir FTP;
    cd FTP; 
    path=$(pwd);
popd

echo "FTP created in $path";