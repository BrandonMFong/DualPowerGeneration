/*
 * DualPowerGeneration.c
 *
 * Created: 10/11/2019 5:07:09 PM
 * Author : Brandon Fong        <- Joseph Was here
 * 
 *
 * Date last modified: 
 */ 

#include <avr/io.h>

#define SUNRISE_ANGLE = 0
#define SUNSET_ANGLE = 180


//We want four resistors but lets first get the logic down for two
//Using res0, res1 (i.e. photoresistor 1 and 2)
//We are assuming the axis of rotation is one fixed motion
// TODO put Joseph's diagram on repo
// Consider:  frequency to sample.  the amount we sample affects power efficiency
void SolarMovement(double res0, double res1, double res2, double res3, double * drive_motor_factor);

int main(void)
{
    /* Replace with your application code */
    while (1) 
    {
		
		
    }
}

void SolarMovement(double res0, double res1, double res2, double res3, double * drive_motor_factor)
{	
	if(res0 < res1)
	{
		&drive_motor_factor = 1; // position 1 moving west
	}
	else if (res1 > res0)
	{
		&drive_motor_factor = -1; // position -1 moving east
	}
	else &drive_motor_factor = 0;
	
}

