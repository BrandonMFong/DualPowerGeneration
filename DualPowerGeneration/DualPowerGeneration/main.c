/*
 * DualPowerGeneration.c
 *
 * Created: 10/11/2019 5:07:09 PM
 * Author : Brandon Fong        <- Joseph Was here :3
 * 
 *
 * Date last modified: 
 */ 

#include <avr/io.h>

#define SUNRISE_ANGLE = 0
#define SUNSET_ANGLE = 180
#define WEST = 0
#define EAST = 1
#define NORTH = 2
#define SOUTH = 3

//We want four resistors but lets first get the logic down for two
//Using res0, res1 (i.e. photoresistor 1 and 2)
//We are assuming the axis of rotation is one fixed motion
// TODO put Joseph's diagram on repo
// Consider:  frequency to sample.  the amount we sample affects power efficiency

//void SolarMovement(double res0, double res1, double res2, double res3, double * drive_motor_factor);

void movePanel(int direction, double resA, double resB, double * drive_motor_factor);

int main(void)
{
	//Initialize
	double currentAngle = SUNRISE_ANGLE;   // Do something with this later
	
	double motorFactor_or_whatever;
	
	double res0;    //West Resistor
	double res1;    //East Resistor
	
	double res2;    // North      <- in case we do 360
	double res3;    // South
	
    /* Replace with your application code */
    while (1) 
    {
		// Read values from resistors and assign them to  res variables here
			//TODO resistor reading here
			
		// Do something with motorFactor variable here
		    //TODO motor factor
		
		if(res0 > res1) movePanelTo(WEST, res0, res1, &motorFactor_or_whatever);
		
		if(res1 > res0) movePanelTo(EAST, res1, res0, &motorFactor_or_whatever);
		
    }
}

void movePanelTo(int direction, double resA, double resB, double * drive_motor_factor)
{
	if(direction == WEST) &drive_motor_factor = 1;       // position 1 moving west
		
	else if(direction == EAST) &drive_motor_factor = -1; // position -1 moving east
	
	else else &drive_motor_factor = 0;
}

// void SolarMovement(double res0, double res1, double res2, double res3, double * drive_motor_factor)
// {	
// 	if(res0 < res1)
// 	{
// 		&drive_motor_factor = 1; // position 1 moving west
// 	}
// 	else if (res1 > res0)
// 	{
// 		&drive_motor_factor = -1; // position -1 moving east
// 	}
// 	else &drive_motor_factor = 0;
// 	
// }

