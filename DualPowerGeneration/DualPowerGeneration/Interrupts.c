/*
 * CFile1.c
 *
 * Created: 10/18/2019 5:01:30 PM
 *  Author: Brandon
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "Param_Const_GLVar.h"

/* Interrupt for Timer 0 comparing to OCR0A
 * This is the function that will read the resistor values
 * Reading the resistor values require an Analog to Digital Converter 
 * Refer to ADConverter.c
 */

// Joseph below is how I put the adc values from the resistors into your variables.  
ISR (TIMER0_COMPA_vect)
{
	res0 = adc_read(CHANNEL_RESISTOR_0);
	// Call your function here Joseph to move the solar panel
	// Implement your values in Maneuver.c
}

ISR (TIMER0_COMPB_vect)
{
	res1 = adc_read(CHANNEL_RESISTOR_1);
	// Call function
}

ISR (TIMER2_COMPA_vect)
{
	res2 = adc_read(CHANNEL_RESISTOR_2);
	// Call function
}

ISR (TIMER2_COMPB_vect)
{
	res3 = adc_read(CHANNEL_RESISTOR_3);
	// Call function
}

/* Interrupt for ADC Converter
 * Tells us when we can get the value from the adc reg
 * NOTE: might not need this if I'm reading from the timer vector
 */
//ISR(ADC_vect)
//{
	///* ADC
	 //* ADC holds the value at the anolog value
	 //*/
	//uint16_t AD = ADC;
//}

