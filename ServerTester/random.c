#include <stdio.h>

int main() {
   int i,total;
   //int srand[60];
   int n = 60;
int rand[60];
   total = 0;

   for(i = 0; i < n; i++) {
       int num;
       num =  abs(rand[i] % (3600 + 1 - 0) + 0);

     total += num;
      printf("%d\n", num);
   }

   printf("Average = %f\n", total/(float)n);
   return 0;
}
