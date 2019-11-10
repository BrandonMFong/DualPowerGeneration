 // calculate torque and angular velocity of the wind turbine
 // take the average of the values to get the average power
 // use equation P = torque* rpm*pi/30.
 // torque in N/m and angular velocity in revolutions per minute
#include <stdio.h>

int main() {
   int i,total;
   //int srand[60];
   int n = 60;
int rand[60];
int srand[60];
   total = 0;

   for(i = 0; i < n; i++) {
       int num;
       num =  abs(rand[i] % (2000 + 1 - 0) + 0);

     total += num;
      printf("%d\n", num);
   }

   printf("Average rpm = %f\n", total/(float)n);
   int total_1 = 0;
     for(int c = 0; c < n; c++) {
       int num;
       num =  abs(srand[c] % (500 + 1 - 0) + 0);

     total_1 += num;

      printf("%d\n", num);
   }

  int pie = 3.14159265;
    printf("Average torque = %f\n", total_1/(float)n);
    printf("Average power for a minute = %f", total/(float)n*total_1/(float)n*pie/30);

   return 0;
}
