# Engineer: Brandon Fong
#
#This script is to only interact with the dualpower_DataCenter db 
# The purpose of this script is to read the .csv file that was sent and insert into the database
# refer to /DualPowerGeneration/MaxPowerTracker/example_file.csv for the column descriptions

# Local Test Notes:
# I cannot connect to the mysql server with the socket in my.cnf, what the freeaaaaaak
# look for /etc/mysql/my.cnf

# Important references:
# http://lubos.rendek.org/import-data-from-csv-file-to-mysql-with-bash-script/
# https://hoststud.com/resources/how-to-execute-mysql-queries-from-command-line-bash-shell.136/
# https://www.cyberciti.biz/faq/unix-linux-bash-read-comma-separated-cvsfile/

set -e
# awk '/delay/ {print}' MaxPower.xml
### VARIABLES ### 
# credentials
username=$(awk -F '[<>]' '/UsernameForDatabase/{print $3}' ../Config/EarthWindFire/Scripts.xml)
password=$(awk -F '[<>]' '/PasswordForDatabase/{print $3}' ../Config/EarthWindFire/Scripts.xml)
database=$(awk -F '[<>]' '/DatabaseToInjectFTPDataInto/{print $3}' ../Config/EarthWindFire/Scripts.xml)
Archive_dir="archive/"
FTP_dir=$(awk -F '[<>]' '/FTP_Folder/{print $3}' ../Config/EarthWindFire/Scripts.xml)
DelayVar=$(awk -F '[<>]' '/SecondsToWaitToReadFolder/{print $3}' ../Config/EarthWindFire/Scripts.xml); # Delays for 5 seconds
cl=$(awk -F '[<>]' '/tablecl/{print $3}' ../Config/EarthWindFire/Scripts.xml); # Delays for 5 seconds
dc=$(awk -F '[<>]' '/tabledc/{print $3}' ../Config/EarthWindFire/Scripts.xml); # Delays for 5 seconds
dev=$(awk -F '[<>]' '/tabledev/{print $3}' ../Config/EarthWindFire/Scripts.xml); # Delays for 5 seconds
sol=$(awk -F '[<>]' '/tablesol/{print $3}' ../Config/EarthWindFire/Scripts.xml); # Delays for 5 seconds
win=$(awk -F '[<>]' '/tablewin/{print $3}' ../Config/EarthWindFire/Scripts.xml); # Delays for 5 seconds

### MAIN ###
pushd $FTP_dir
        if [ $(pwd) != $FTP_dir ];
        then 
                echo "Failure to pushd to location $FTP_dir.  Exitting script."
                exit;
        fi

        while true 
        do 
                if [ $(find . -maxdepth 1 -type f|wc -l) -gt 0 ]; # keeps reading files in dir until there are not more files in dir
                then
                        # Testing if archive existss
                        if ! [ -d $Archive_dir ] # TODO figure out error
                        then
                                mkdir $Archive_dir;
                                echo "$Archive_dir does not exist...Made directory.";
                        fi

                        if [ $(find . -empty -type f | wc -l) -gt 0 ] # checks for empty files
                        then
                                echo "Removing empty files";
                                rm $(find -empty -type f); # Removes all files that are empty, this actually throws an error on the cmd line
                        fi

                        current_working_file=$(find . -maxdepth 1  -type f | head -1);  # filters out the dir and filters files
                        echo "Currently reading file: $current_working_file";

                        echo "Executing insert query";
                        while IFS=,  read -r Client_ID DateTime Max_Power_for_Wind Max_Power_for_Solar
                        do
                                # Query string
                                # This accesses the db correctly but it now says that client does not exist in the directory
                                # echo "Date time variable";
                                # echo $DateTime;
                                querystring="set @Solar_ID = (select Solar_ID from $cl as cl join $dc as dc";
                                querystring+=" on cl.ID = dc.Client_ID join $dev as dev on dev.ID = dc.Device_ID where cl.ID = $Client_ID);";
                                querystring+=" set @Wind_ID = (select Wind_ID from $cl as cl join $dc as dc";
                                querystring+=" on cl.ID = dc.Client_ID join $dev as dev on dev.ID = dc.Device_ID where cl.ID = $Client_ID);";
                                querystring+=" insert into $sol (ID,Time,Power) values (@Solar_ID, '$DateTime', $Max_Power_for_Solar);";
                                querystring+=" insert into $win (ID,Time,Power) values (@Wind_ID, '$DateTime', $Max_Power_for_Wind);";
                                echo -n "${querystring}";
                        
                        # This should be a FIFO procedure for the files coming into the server
                        done < $current_working_file | mysql -u$username -p$password -D$database # might not need this mysql command
                        echo "Finished while loop for the insert query.";

                        mv $current_working_file $Archive_dir;
                        echo "Moved $current_working_file to $Archive_dir";
                else
                        echo "Waiting for more files...";
                        sleep $DelayVar;
                fi
        done
popd