
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
	res1 = adc_read(CHANNEL_RESISTOR_1);
	
	if(res0 > res1) movePanelTo(WEST, res0, res1, &motorFactor_or_whatever);
	else if(res1 > res0) movePanelTo(EAST, res1, res0, &motorFactor_or_whatever);
	// Implement your values in Maneuver.c
}

ISR (TIMER0_COMPB_vect)
{
	res2 = adc_read(CHANNEL_RESISTOR_2);
	res3 = adc_read(CHANNEL_RESISTOR_3);
	
	if(res2 > res3) movePanelTo(NORTH, res2, res3, &motorFactor_or_whatever);
	else if(res3 > res2) movePanelTo(SOUTH, res3, res2, &motorFactor_or_whatever);

	// Read Resistor 0 values
}

/* Interrupt for Timer 0 comparing to OCR0A
 * This is the function that will read the resistor values
 * Reading the resistor values require an Analog to Digital Converter 
 * Refer to ADConverter.c
 */
ISR (TIMER0_COMPB_vect)
{
	// Read Resistor 1 values
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
ISR(ADC_vect)
{
	/* ADC
	 * ADC holds the value at the anolog value
	 */
	uint16_t AD = ADC;
}















