# This script is to only interact with the dualpower_DataCenter db 
# The purpose of this script is to read the .csv file that was sent and insert into the database

# Important references:
# http://lubos.rendek.org/import-data-from-csv-file-to-mysql-with-bash-script/

# credentials
username="dualpower_BrandonMFong"
password="dualpower27182"
database="dualpower_DataCenter"

mysql -u$username -p$password -D$database # this is how you access the mysql terminal


IFS=,
while read column1 column2 column3
      do
        echo "INSERT INTO cost (column1,column2,column3) VALUES ('$column1', '$column2', '$column3');"

done < input.csv | mysql -u myusername -p mypassword mydata;