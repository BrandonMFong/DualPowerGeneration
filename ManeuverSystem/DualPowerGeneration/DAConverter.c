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
//void dac_write_digital(bool is_x_actuator, double value)
//{
	//if(is_x_actuator)
	//{
		//if(value == 1) //forward
		//{
			//PORTB &= JOINT_1_move_X;
		//}
		//else //reverse
		//{
			//PORTB &= JOINT_1_move_X; // How do you establish a reverse?
		//}
	//}
	//else
	//{
		//if(value == 1) //forward
		//{
			//PORTB &= JOINT_2_move_Y;
		//}
		//else //reverse
		//{
			//PORTB &= JOINT_2_move_Y;// How do you establish a reverse?
		//}
	//}
//}

// Right now we want to use two motors or actuators 
void dac_write_digital(int axis, double * drive_motor_factor)
{
	switch(axis)
	case is_X_AXIS_0_1: 
	{
		switch(*drive_motor_factor)
		case 1: //forward
		{
			PORTB &= JOINT_1_move_X;
			break;
		}
		case -1: //reverse
		{
			PORTB &= JOINT_1_move_X; // How do you establish a reverse?
			break;
		}
		default: {PORTB &= JOINT_1_dont_move_X|JOINT_2_dont_move_Y;break;}
	}
	case is_Y_AXIS_2_3: 
	{
		switch(*drive_motor_factor)
		case 1: //forward
		{
			PORTB &= JOINT_2_move_Y;
		}
		case -1: //reverse
		{
			PORTB &= JOINT_2_move_Y;// How do you establish a reverse?
		}
		default: {PORTB &= JOINT_1_dont_move_X|JOINT_2_dont_move_Y;break;}
	}
	default: {PORTB &= JOINT_1_dont_move_X|JOINT_2_dont_move_Y;break;}
}
// TODO 
// If I make a pulse width here, I would put its own timer sequence here
// But what if an interrupt is called?
// Does a linear actuator need an analog signal?
/*
 * This might stay in this function until resistors are the same
 * is that safe?
 */
void dac_write_analog(int channelA, int channelB, int axis, double * drive_motor_factor)
{
	// TODO put reverse mode and distinguish the joint movements.  Might have to put another case
	int msec = 10000;
	uint16_t resA = adc_read(channelA);
	uint16_t resB = adc_read(channelB);
	switch(axis)
	{
		case is_X_AXIS_0_1: 
		{
			if (resA > resB)
			{
				do
				{
					resA = adc_read(channelA);
					resB = adc_read(channelB);
					_delay_ms(msec);
					PORTB &= JOINT_1_move_X;
				} while (resA > (resB/2));
				
				do
				{
					resA = adc_read(channelA);
					resB = adc_read(channelB);
					_delay_ms(msec);
					PORTB &= JOINT_1_move_X;
				} while (resA > resB/2);
			}
			else
			{
				do
				{
					resA = adc_read(channelA);
					resB = adc_read(channelB);
					_delay_ms(msec);
					PORTB &= JOINT_1_move_X;
				} while (resB > (resA/2));
				
				do
				{
					resA = adc_read(channelA);
					resB = adc_read(channelB);
					_delay_ms(msec);
					PORTB &= JOINT_1_move_X;
				} while (resB > resA);
			}
	}
		case is_Y_AXIS_2_3:
		{
			if (resA > resB)
			{
				do
				{
					resA = adc_read(channelA);
					resB = adc_read(channelB);
					_delay_ms(msec);
					PORTB &= JOINT_2_move_Y;
				} while (resA > (resB/2));
			
				do
				{
					resA = adc_read(channelA);
					resB = adc_read(channelB);
					_delay_ms(msec);
					PORTB &= JOINT_2_move_Y;
				} while (resA > resB/2);
			}
			else
			{
				do
				{
					resA = adc_read(channelA);
					resB = adc_read(channelB);
					_delay_ms(msec);
					PORTB &= JOINT_2_move_Y;
				} while (resB > (resA/2));
			
				do
				{
					resA = adc_read(channelA);
					resB = adc_read(channelB);
					_delay_ms(msec);
					PORTB &= JOINT_2_move_Y;
				} while (resB > resA);
			}
		}
	}
}
