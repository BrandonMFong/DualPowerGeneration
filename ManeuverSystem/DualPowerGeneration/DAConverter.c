/*
 * CFile1.c
 *
 * Created: 10/20/2019 4:32:46 PM
 *  Author: Joseph Morga, Brandon Fong, Ahmad AlSarhan
 */ 

/*** OUTPUT ***/

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "Param_Const_GLVar.h"

/*
 * Not really a DAC
 * Just making an output pin here
 */
void dac_init()
{
	// Joint 1 = x, Joint 2 = y
	DDRB |= JOINT_1_init_X|JOINT_2_init_Y; // this connects to OC1A, refer to text (I think 119)
}

/*
 * This is for the motor where we just need to apply a digital input
 *
 * TODO finish this logic
 * setting PORTB to value is wrong because value is not the correct binary value if value is negative
 * figure out how to decode Joseph's drivefactor logic to the correct analog output
 * Might need to add more parameters
 */
void dac_write_digital(bool is_x_actuator, double value)
{
	if(is_x_actuator)
	{
		if(value == 1) //forward
		{
			PORTB &= JOINT_1_move_X;
		}
		else //reverse
		{
			PORTB &= JOINT_1_move_X; // How do you establish a reverse?
		}
	}
	else
	{
		if(value == 1) //forward
		{
			PORTB &= JOINT_2_move_Y;
		}
		else //reverse
		{
			PORTB &= JOINT_2_move_Y;// How do you establish a reverse?
		}
	}
}
// TODO 
// If I make a pulse width here, I would put its own timer sequence her
// But what if an interrupt is called?
// Does a linear actuator need an analog signal?
void dac_write_analog()
{
	// TODO figure out pulse width modulation
}
