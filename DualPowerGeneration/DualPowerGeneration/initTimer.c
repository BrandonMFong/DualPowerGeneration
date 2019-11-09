/*
 * CFile1.c
 *
 * Created: 10/18/2019 4:59:14 PM
 *  Author: Brandon
 */ 

/* Function: initTimerA
 * Using this timer to set a sampling frequency to read RESISTORS
 * Reason:  We don't want to continuously read resistors.  Reading every 160ms.
 * Values can be changed
 */
void initTimer0A()
{
	/* OCR0A
	 * The OCR0A defines the top value for the counter, hence also its resolution (pg 98)
	 */
	OCR0A = 124; //1
	OCR0B = 248; //2
<<<<<<< HEAD
=======
	
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

void initTimer2A()
{
	/* OCR0A
	 * The OCR0A defines the top value for the counter, hence also its resolution (pg 98)
	 */
	OCR0A = 124;
>>>>>>> 4a6c084f5a6b5c29177a0b8a1488ea857acecbb7
	
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
