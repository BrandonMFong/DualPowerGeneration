/*
 * CFile1.c
 *
 * Created: 10/20/2019 4:32:46 PM
 *  Author: Brandon
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "Param_Const_GLVar.h"

/* Problem: 
 * Link: https://www.edn.com/design/integrated-circuit-design/4312523/Create-a-DAC-from-a-microcontroller-s-ADC
 * Link: https://tutorial.cytron.io/2012/06/22/pid-for-embedded-design/
 * The atmega does not have a DAC output port.  
 * There have been some practices about making a DAC from an ADC
 * PID (proportional-integral-derivative) algorithm
 */

/*
 * Not really a DAC
 * Just making an output pin here
 */
void dac_init()
{
	DDRB |= (1<<DDB1); // this connects to OC1A, refer to text (I think 119)
}