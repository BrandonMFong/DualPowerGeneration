/*
 * CFile1.c
 *
 * Created: 10/18/2019 5:00:41 PM
 *  Author: Joseph Morga, Brandon Fong, Ahmad AlSarhan
 */ 

/*** INPUT ***/

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "Param_Const_GLVar.h"

void adc_init() {
	/* ADMUX
	 * REFS0 = using Vcc as reference voltage
	 */
	ADMUX = (1<<REFS0);
	
	/* ADCSRA
	 * ADEN = enables the analog to digital converter
	 * ADIE = Interrupt enabled
	 * ADPS[2:0] = Pre-Scalars
	 * Subject to change
	 */
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1 << ADIE)|(1<<ADPS1)|(1<<ADPS0);
	
	/* ADCSRB
	 * Since we are reading when timer 0 finishes counting to A, we are reading at the same time
	 */
	ADCSRB = (1<<ADTS1)|(1<<ADTS0);
}

uint16_t adc_read(uint8_t adcChannels) {
	
	/* adcChannels
	 * There are only 8 channels right now on the Atmega 328 board for ADC
	 * log2(8) = 3, only need to represent these channels with 3 bits.  Reason why we & with 0b00000111
	 * adcChannels can be chose from functions
	 * We must determine which channels we are using to read the resistors
	 * Since we are using 4, when need to call this function 4 times
	 */
	adcChannels &= 0b00000111;
	
	/* ADMUX
	 * This sets the channels we use
	 * We & 0xF8 to clear the bottom three to disregard our last channel read
	 * TODO figure out if you can call this function 4 times, or should we multiplex the.  
	 * Because can you use ADMUX in 4 different instantiations? 
	 * There is only one ADMUX
	 * Multiplex means we read 1 resistor at a time
	 * E.G. 400us after reading resistor x we read resister x+1
	 */
	ADMUX = (ADMUX & 0xF8)|adcChannels;
	
	/* ADSC
	 * This tells the processor to start converting A to D
	 */
	ADCSRA |= (1<<ADSC);
	
	// while ADSC is 1, keep looping.  When ADSC = 0, get out of loop
	while(ADCSRA & (1<<ADSC));
	
	return (ADC);
}