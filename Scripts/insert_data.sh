# This script is to only interact with the dualpower_DataCenter db 
# The purpose of this script is to read the .csv file that was sent and insert into the database
# refer to /DualPowerGeneration/MaxPowerTracker/example_file.csv for the column descriptions

# Important references:
# http://lubos.rendek.org/import-data-from-csv-file-to-mysql-with-bash-script/
# https://hoststud.com/resources/how-to-execute-mysql-queries-from-command-line-bash-shell.136/
# https://www.cyberciti.biz/faq/unix-linux-bash-read-comma-separated-cvsfile/

# credentials
username="dualpower_BrandonMFong"
password="dualpower27182"
database="dualpower_DataCenter"
Archive_dir="archive/"
FTP_dir="B:/SOURCES/Repos/DualPowerGeneration/FTP"; # Testing locally
#FTP_dir="/home/dualpower/public_ftp/incoming/FTP"; # On server

pushd FTP_dir
        while [ $(find . -maxdepth 1 -type f|wc -l) -gt 0 ]; # keeps reading files in dir until there are not more files in dir
        do
                # Testing if archive existss
                if [ -d $dir ] # TODO figure out error
                then
                        echo "$dir Exists/n";
                else
                        mkdir archive;
                        echo "$dir does not exist.../nMade directory./n";
                fi

                echo "Removing empty files";
                rm $(find -empty); # Removes all files that are empty, this actually throws an error on the cmd line

                current_working_file=$(find . -maxdepth 1  -type f | head -1);  # filters out the dir and filters files
                echo "Currently reading file: $current_working_file";

                echo "Executing insert query";
                while IFS=,  read -r Client_ID DateTime Max_Power_for_Wind Max_Power_for_Solar
                do
                        # Query string
                        query="set @Solar_ID = (select Solar_ID from client as cl join device_client as dc on cl.ID = dc.Client_ID join device as dev on dev.ID = dc.Device_ID where cl.ID = $Client_ID); set @Wind_ID = (select Solar_ID from client as cl join device_client as dc on cl.ID = dc.Client_ID join device as dev on dev.ID = dc.Device_ID where cl.ID = $Client_ID); insert into solar (ID,Time,Power) values (@Solar_ID, '$DateTime', $Max_Power_for_Solar); insert into wind (ID,Time,Power) values (@Wind_ID, '$DateTime', $Max_Power_for_Wind);";
                        mysql -u$username -p$password -D$database -e$query # this is how you access the mysql terminal
                # This should be a FIFO procedure for the files coming into the server
                done < $current_working_file #| mysql -u$username -p$password -D$database # might not need this mysql command
                echo "Finished while loop for the insert query.";

                mv $current_working_file $dir;
                echo "Moved $current_working_file to $dir";
        done 
popd