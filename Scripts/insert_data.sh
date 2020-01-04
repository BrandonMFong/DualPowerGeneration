# This script is to only interact with the dualpower_DataCenter db 
# The purpose of this script is to read the .csv file that was sent and insert into the database
# refer to \DualPowerGeneration\MaxPowerTracker\example_file.csv for the column descriptions

# Important references:
# http://lubos.rendek.org/import-data-from-csv-file-to-mysql-with-bash-script/

# credentials
username="dualpower_BrandonMFong"
password="dualpower27182"
database="dualpower_DataCenter"

pushd /home/dualpower/public_ftp/incoming/FTP
        while [ $(find . -maxdepth 1 -type f|wc -l) -gt 0 ]; # keeps reading files in dir until there are not more files in dir
        do
                # Testing if archive exists
                dir=archive/
                # if [ -d "$dir" ]
                # then
                #         echo "$dir Exists\n";
                # else
                #         mkdir archive;
                #         echo "$dir does not exist...\nMade directory.\n";
                # fi
                # above does not seem to work
                # it's fine if I made the directory myself, but if we are serving many different clients with different
                # servers then it would be ideal to have these lines of code to work
                # atm, not the priority

                echo "Removing empty files\n";
                rm $(find -empty); # Removes all files that are empty

                current_working_file=$(find . -maxdepth 1  -type f | head -1);  # filters out the dir and filters files
                echo "Currently reading file: $current_working_file\n\n";

                # Time and Power is in the file, but ID is not
                # I need to query the db to obtain the ID for the solar from the org_id provided in the .csv file
                IFS=, # IFS is a way to say we are reading a comma delimited file
                # This while loop reads the current file and works on inserting the data
                echo "Executing insert query";
                while read Client_ID DateTime Max_Power_for_Wind Max_Power_for_Solar
                do
                        # Query string
                        echo 
                        "
                                set @Solar_ID = -- Get's id for the solar table
                                        (
                                        select Solar_ID
                                                from client cl 
                                                join device_client dc 
                                                        on cl.ID = dc.Client_ID
                                                join device dev 
                                                        on dev.ID = dc.Device_ID
                                                where cl.ID = $Client_ID
                                        );
                                set @Wind_ID = -- Get's id for the wind table
                                        (
                                        select Solar_ID
                                                from client cl 
                                                join device_client dc 
                                                        on cl.ID = dc.Client_ID
                                                join device dev 
                                                        on dev.ID = dc.Device_ID
                                                where cl.ID = $Client_ID
                                        );

                                insert into solar (ID,Time,Power) 
                                values (@Solar_ID, '$DateTime', $Max_Power_for_Solar);
                                
                                insert into wind (ID,Time,Power) 
                                values (@Wind_ID, '$DateTime', $Max_Power_for_Wind);
                        ";
                # This should be a FIFO procedure
                done < $current_working_file | mysql -u$username -p$password -D$database # this is how you access the mysql terminal
                echo "Finished while loop for the insert query.";

                mv $current_working_file $dir;
                echo "Moved $current_working_file to $dir";
        done 
popd