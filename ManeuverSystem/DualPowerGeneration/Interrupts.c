
/*
 * CFile1.c
 *
 * Created: 10/18/2019 5:01:30 PM
 *  Author: Joseph Morga, Brandon Fong, Ahmad AlSarhan
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "Param_Const_GLVar.h"


double motorFactor_or_whatever = 0.00;

// Might need to change the data type for these res[0 - 3] cuz adc_read() returns uint16_t
double res0;    //West Resistor
double res1;    //East Resistor

double res2;    // North      <- in case we do 360
double res3;    // South

/* Interrupt for Timer 0 comparing to OCR0A
 * This is the function that will read the resistor values
 * Reading the resistor values require an Analog to Digital Converter 
 * Refer to ADConverter.c
 *
 * Let resistor 0 and 1 be the x-axis 
 * Let resistor 2 and 3 be the y-axis
 */

// Joseph below is how I put the adc values from the resistors into your variables.  
// Good job on using the adc_read() twice in one timer interrupt.  Honestly didn't think of that -Brandon
ISR (TIMER0_COMPA_vect)
{
	res0 = adc_read(CHANNEL_RESISTOR_0);
	res1 = adc_read(CHANNEL_RESISTOR_1);
	
	if(res0 > res1) movePanelTo(WEST, res0, res1, &motorFactor_or_whatever);
	else if(res1 > res0) movePanelTo(EAST, res1, res0, &motorFactor_or_whatever);
	
	/* Call the output function to turn on the motor */
	dac_write_digital(is_X_AXIS_0_1 ,&motorFactor_or_whatever);
}

ISR (TIMER0_COMPB_vect)
{
	res2 = adc_read(CHANNEL_RESISTOR_2);
	res3 = adc_read(CHANNEL_RESISTOR_3);
	
	if(res2 > res3) movePanelTo(NORTH, res2, res3, &motorFactor_or_whatever);
	else if(res3 > res2) movePanelTo(SOUTH, res3, res2, &motorFactor_or_whatever);
	
	/* Call the output function to turn on the motor */
	dac_write_digital(is_Y_AXIS_2_3, &motorFactor_or_whatever);
}

/* Interrupt for ADC Converter
 * Tells us when we can get the value from the adc reg
 * NOTE: might not need this if I'm reading from the timer vector
 */
ISR(ADC_vect)
{
	/* ADC
	 * ADC holds the value at the anolog value
	 */
	uint16_t AD = ADC;
}















