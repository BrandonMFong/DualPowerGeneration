/*
 * CFile1.c
 *
 * Created: 10/18/2019 4:59:14 PM
 *  Author: Brandon
 */ 

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include "Param_Const_GLVar.h"

// Link: https://sites.google.com/site/qeewiki/books/avr-guide/timers-on-the-atmega328

/* Function: initTimerA
 * Using this timer to set a sampling frequency to read RESISTORS
 * Reason:  We don't want to continuously read resistors.  Reading every 160ms.
 * Values can be changed
 */
void initTimer0()
{
	/* OCR0A
	 * The OCR0A defines the top value for the counter, hence also its resolution (pg 98)
	 */
	OCR0A = 124; //1
	OCR0B = 248; //2
	
	/* TCCR0A
	 * Setting mode to CTC (Clear Timer on Compare)
	 * Comparing to OCR0A	
	 */
	TCCR0A |= 1<<WGM01; 
	
	/* TCCR0B
	 * Incrementing timer at a frequency = F_CPU / 256 = 62.5 kHz
	 * CSO[2:0] = 3'b100;
	 */
	TCCR0B |= 1<<CS02;
	
	/* TIMSK0
	 * Setting Timer A interrupt flag to True
	 * Setting Timer B interrupt flag to True
	 */
	TIMSK0 |= (1<<OCIE0A)|(1<<OCIE0B);
}

// refer to page 131 in data sheet
// Don't edit this
void initTimer1()
{
	// Note the WGM1n = 15 means fast pwm compare on ocr1a
	//TCCR1A – Timer/Counter1 Control Register A
	TCCR1A |= (1<<COM1A1)|(1<<COM1A0)|(1<<WGM10)|(1<<WGM11);
	
	// TCCR1B – Timer/Counter1 Control Register B
	// Not going to prescale
	TCCR1B |= (1<<WGM12)|(1<<WGM13);
	
	/* TODO config timer registers */
	//// TCCR1C – Timer/Counter1 Control Register C
	//TCCR1C = 0;
	//
	//// TCNT1H and TCNT1L – Timer/Counter1
	//TCNT1 = 0;
	//
	////OCR1AH and OCR1AL – Output Compare Register 1 A
	//OCR1A =0;
	//
	//// OCR1BH and OCR1BL – Output Compare Register 1 B
	//OCR1B = 0;
	//
	//// ICR1H and ICR1L – Input Capture Register 1
	//ICR1H = 0;
	//
	//// TIMSK1 – Timer/Counter1 Interrupt Mask Register
	//TIMSK1 = 0;
	//
	//// TIFR1 – Timer/Counter1 Interrupt Flag Register
	//TIFR1 = 0;
}
void initTimer2()
{
	/* OCR0A
	 * The OCR0A defines the top value for the counter, hence also its resolution (pg 98)
	 */
	OCR2A = 124;
	
	/* TCCR0A
	 * Setting mode to CTC (Clear Timer on Compare)
	 * Comparing to OCR0A
	 */
	TCCR2A |= 1<<WGM21; 
	
	/* TCCR0B
	 * Incrementing timer at a frequency = F_CPU / 256 = 62.5 kHz
	 * CSO[2:0] = 3'b100;
	 */
	TCCR2B |= 1<<CS22;
	
	/* TIMSK0
	 * Setting Timer A interrupt flag to True
	 */
	TIMSK2 |= 1<<OCIE2A;
}
