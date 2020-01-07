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

/* Problem: 
 * Link: https://www.edn.com/design/integrated-circuit-design/4312523/Create-a-DAC-from-a-microcontroller-s-ADC
 * Link: https://tutorial.cytron.io/2012/06/22/pid-for-embedded-design/
 * The atmega does not have a DAC output port.  
 * There has been some practices about making a DAC from an ADC
 * PID (proportional-integral-derivative) algorithm
 *
 * Update: This might just be an output pin for a digital value
 */

/*
 * Not really a DAC
 * Just making an output pin here
 */
void dac_init()
{
	DDRB |= JOINT_1_init|JOINT_2_init; // this connects to OC1A, refer to text (I think 119)
}

/*
 * This is for the motor where we just need to apply a digital input
 *
 * TODO finish this logic
 * setting PORTB to value is wrong because value is not the correct binary value if value is negative
 * figure out how to decode Joseph's drivefactor logic to the correct analog output
 * Might need to add more parameters
 */
void dac_write_digital(bool x_motor, bool y_motor, double value)
{
	if(x_motor)
	{
		PORTB &= value;
	}
	else if(y_motor)
	{
		PORTB &= value;
	}
	else
}

void dac_write_analog()
{
	// TODO figure out pulse width modulation
}
