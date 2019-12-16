#include <stdio.h>

int main() 
{
	int i,total;
	//int srand[60];
	int n = 60;
	int rand[60];
		int total_rpm = 0;

		for(i = 0; i < n; i++) 
		{
			int num;
			num =  abs(rand[i] % (3600 + 1 - 0) + 0);

			total_rpm += num;
			printf("%d\n", num);
		}

		printf("Average rpm = %f\n", total_rpm/(float)n);
	}
	int torque(){
	int srand[60];
	int total_torque = 0;

	for(int c = 0; c < n; c++) {
	int num;
	num =  abs(srand[c] % (1000 + 1 - 0) + 0);

	total_torque += num;
	printf("%d\n", num);
	}

	printf("Average torque = %f\n", total_torque/(float)n);
	}


	return 0;
}
