 // calculate torque and angular velocity of the wind turbine
 // take the average of the values to get the average power
 // use equation P = torque* angular velocity.
 // torque in N/m and angular velocity in revolutions per minute
 #include <stdio.h>
    #include <stdlib.h>

    int main() {
        double angularvelocity(){
      int c, n;

      printf("3600 random numbers in 1 to 3600\n");

      for (c = 1; c <= 60; c++) {
        n = rand() % 3600 + 1;
        printf("%d\n", n);
      }
        }
        double torque(){
            int d, n;

      printf("random numbers in 1 to 10\n");
    int b;
      for (d = 1; d <= 10; d++) {
        n = rand() % 10 + 1;
        printf("%d\n", b);
      }
      double e;
      double average(angularvelocity, torque){
          double sum;
      sum = angularvelocity * torque;
      printf("%lf", e);
      }


      return e;
        }
      }

