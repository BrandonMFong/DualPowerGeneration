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
#define SUNRISE_ANGLE = 0
#define SUNSET_ANGLE = 180
#define WEST = 0
#define EAST = 1
#define NORTH = 2
#define SOUTH = 3

#define CHANNEL_RESISTOR_0 = 0
#define CHANNEL_RESISTOR_1 = 1
#define CHANNEL_RESISTOR_2 = 2
#define CHANNEL_RESISTOR_3 = 3

/*** GLOBAL VARIABLES ***/
double currentAngle = SUNRISE_ANGLE;   // Do something with this later

double motorFactor_or_whatever;

double res0;    //West Resistor
double res1;    //East Resistor

double res2;    // North      <- in case we do 360
double res3;    // South


/*** PROTOTYPES ***/
//void SolarMovement(double res0, double res1, double res2, double res3, double * drive_motor_factor);
void movePanel(int direction, double resA, double resB, double * drive_motor_factor);
void initTimer0A();
void adc_init();
uint16_t adc_read(uint8_t ch);

#endif /* GLOBAL_VARIABLES_H_ */