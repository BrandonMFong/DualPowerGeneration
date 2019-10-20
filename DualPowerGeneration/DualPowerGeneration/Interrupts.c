/*
 * CFile1.c
 *
 * Created: 10/18/2019 5:01:30 PM
 *  Author: Brandon
 */ 

/* Interrupt for Timer 0 comparing to OCR0A
 * This is the function that will read the resistor values
 * Reading the resistor values require an Analog to Digital Converter 
 * Refer to ADConverter.c
 */
ISR (TIMER0_COMPA_vect)
{
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
 */
ISR(ADC_vect)
{
	/* ADC
	 * ADC holds the value at the anolog value
	 */
	uint16_t AD = ADC;
}