/*
 * Param_Const_GLVar.h
 *
 * Created: 11/3/2019 8:21:35 AM
 *  Author: Brandon
 */ 


#ifndef GLOBAL_VARIABLES_H_
#define GLOBAL_VARIABLES_H_

/*** CONSTANTS ***/
#define F_CPU 16000000UL  // this is the clock frequency of the board
#define SUNRISE_ANGLE  0
#define SUNSET_ANGLE  180
#define WEST  0
#define EAST  1
#define NORTH  2
#define SOUTH  3

#define CHANNEL_RESISTOR_0  0
#define CHANNEL_RESISTOR_1  1
#define CHANNEL_RESISTOR_2  2
#define CHANNEL_RESISTOR_3  3

/*** GLOBAL VARIABLES ***/
double currentAngle = SUNRISE_ANGLE;   // default possition of the panel

double motorFactor_or_whatever = 0.00;

double res0;    //West Resistor
double res1;    //East Resistor

double res2;    // North      <- in case we do 360
double res3;    // South

int speed; // value I am using for the pulse width


/*** PROTOTYPES ***/
//void SolarMovement(double res0, double res1, double res2, double res3, double * drive_motor_factor);
void movePanelTo(int direction, double resA, double resB, double * drive_motor_factor);
void initTimer0A();
void movePanel(int direction, double resA, double resB, double * drive_motor_factor);
void initTimer0();
void initTimer1();
void initTimer2();
void adc_init();
uint16_t adc_read(uint8_t ch);
void dac_init();

#endif /* GLOBAL_VARIABLES_H_ */