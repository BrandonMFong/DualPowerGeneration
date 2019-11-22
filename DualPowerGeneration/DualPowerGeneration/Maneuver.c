/*
 * Maneuver.c
 *
 * Created: 11/3/2019 9:32:36 AM
 *  Author: Brandon
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "Param_Const_GLVar.h"

void movePanelTo(int direction, double resA, double resB, double * drive_motor_factor)
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

