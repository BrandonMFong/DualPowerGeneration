
IFS=,
while read column1 column2 column3
      do
        echo "INSERT INTO cost (column1,column2,column3) VALUES ('$column1', '$column2', '$column3');"

done < input.csv | mysql -u myusername -p mypassword mydata;