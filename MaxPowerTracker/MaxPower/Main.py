# Python, there is no main.  It's like a script.  Just like powershell

from random import random # for the random function

n = 60;
total_rpm = 0;

#TODO how to do a for loop to iterate an integer
for i in n:
    num = abs(random() % (3600 + 1 - 0) + 0);
    total_rpm += num;
    print("Num variable: " + num);

print("Total RPM: " + total_rpm);