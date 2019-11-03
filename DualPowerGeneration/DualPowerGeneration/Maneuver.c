/*
 * Maneuver.c
 *
 * Created: 11/3/2019 9:32:36 AM
 *  Author: Brandon
 */ 
void movePanelTo(int direction, double resA, double resB, double * drive_motor_factor)
{
	if(direction == WEST) &drive_motor_factor = 1;       // position 1 moving west
	
	else if(direction == EAST) &drive_motor_factor = -1; // position -1 moving east
	
	else &drive_motor_factor = 0;
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

if(res0 > res1) movePanelTo(WEST, res0, res1, &motorFactor_or_whatever);

if(res1 > res0) movePanelTo(EAST, res1, res0, &motorFactor_or_whatever);