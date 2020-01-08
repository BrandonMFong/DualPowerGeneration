/*
 * Maneuver.c
 *
 * Created: 11/3/2019 9:32:36 AM
 *  Author: Joseph Morga, Brandon Fong, Ahmad AlSarhan
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "Param_Const_GLVar.h"

void movePanelTo(int direction, double resA, double resB, double * drive_motor_factor)// the drive_motor_factor can probably be an int to save mem footprint?
{
	while (resA > resB)
	{
		//Move 1 degree to the given direction
		switch(direction)
		{
			case WEST: {*drive_motor_factor = 1; break;}
			case EAST: {*drive_motor_factor = -1; break;}
			case NORTH: {*drive_motor_factor = 1; break;}
			case SOUTH: {*drive_motor_factor = -1; break;}
			default: {*drive_motor_factor = 0; break;}
		}
	}
}

// Right now we want to use two motors
void moveJoint(bool is_x_axis, double * drive_motor_factor)
{
	if(is_x_axis)
	{
		dac_write_digital(*drive_motor_factor);
	}
	else
	{
		dac_write_digital(*drive_motor_factor);
	}
}

