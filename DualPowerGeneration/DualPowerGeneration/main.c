/*
 * DualPowerGeneration.c
 *
 * Created: 10/11/2019 5:07:09 PM
 * Author : Brandon Fong        <- Joseph Was here :3
 * 
 *
 * Date last modified: 
 */ 
//We want four resistors but lets first get the logic down for two
//Using res0, res1 (i.e. photoresistor 1 and 2)
//We are assuming the axis of rotation is one fixed motion
//Consider:  frequency to sample.  the amount we sample affects power efficiency
//Joseph's diagram is on google drive

#define F_CPU 16000000UL  // this is the clock frequency of the board
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#define SUNRISE_ANGLE = 0
#define SUNSET_ANGLE = 180
#define WEST = 0
#define EAST = 1
#define NORTH = 2
#define SOUTH = 3

/*** GLOBAL VARIABLES ***/ 
// Joseph, moving your variables as global - Brandon
// All are init to 0 by default
double currentAngle = SUNRISE_ANGLE;   // Do something with this later

double motorFactor_or_whatever;

double res0;    //West Resistor
double res1;    //East Resistor

double res2;    // North      <- in case we do 360
double res3;    // South


/*** PROTOTYPES ***/
//void SolarMovement(double res0, double res1, double res2, double res3, double * drive_motor_factor);
void movePanel(int direction, double resA, double resB, double * drive_motor_factor);
void initTimerA();
void adc_init();
uint16_t adc_read(uint8_t ch);

int main(void)
{
	//Initialize
	initTimerA(); // Initializing timer A 
	sei();
	
    while (1) 
    {
		// Read values from resistors and assign them to  res variables here
			// TODO resistor reading here
			// Done by interrupt function ISR (TIMER0_COMPA_vect)
		
		// Do something with motorFactor variable here
		    //TODO motor factor 
		
		if(res0 > res1) movePanelTo(WEST, res0, res1, &motorFactor_or_whatever);
		
		if(res1 > res0) movePanelTo(EAST, res1, res0, &motorFactor_or_whatever);
		
    }
}


void movePanelTo(int direction, double resA, double resB, double * drive_motor_factor)
{
	if(direction == WEST) &drive_motor_factor = 1;       // position 1 moving west
		
	else if(direction == EAST) &drive_motor_factor = -1; // position -1 moving east
	
	else &drive_motor_factor = 0;
}

// void SolarMovement(double res0, double res1, double res2, double res3, double * drive_motor_factor)
// {	
// 	if(res0 < res1)
// 	{
// 		&drive_motor_factor = 1; // position 1 moving west
// 	}
// 	else if (res1 > res0)
// 	{
// 		&drive_motor_factor = -1; // position -1 moving east
// 	}
// 	else &drive_motor_factor = 0;
// 	
// }

/* Function: initTimerA
 * Using this timer to set a sampling frequency to read resistors
 * Reason:  We don't want to continuously read resistors.  Reading every 160ms.
 * Values can be changed
 */
void initTimerA()
{
	/* OCR0A
	 * The OCR0A defines the top value for the counter, hence also its resolution (pg 98)
	 */
	OCR0A = 124;
	
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
	 */
	TIMSK0 |= 1<<OCIE0A;
}

// Interrupt for Timer 0 comparing to OCR0A
ISR (TIMER0_COMPA_vect) 
{
	//
}

void adc_init() {
	// AREF = AVcc
	ADMUX = (1<<REFS0);
	// ADC Enable and pre-scaler of 128
	// 16000000/128 = 125000
	//104 us per conversion
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
}

uint16_t adc_read(uint8_t ch) {
	// select the corresponding channel 0~7
	// ANDingwith ’7? will always keep the value of ‘ch’ between 0 and 7
	ch&= 0b00000111;// AND operation with 7
	ADMUX = (ADMUX & 0xF8)|ch; // clears the bottom 3 bits before ORing
	// start single conversion
	// write ’1? to ADSC
	ADCSRA |= (1<<ADSC);
	// wait for conversion to complete
	// ADSC becomes ’0? again
	// till then, run loop continuously
	while(ADCSRA & (1<<ADSC));
	// ADC is predefined to hold the 10-bit conversion value
	return (ADC);
}



