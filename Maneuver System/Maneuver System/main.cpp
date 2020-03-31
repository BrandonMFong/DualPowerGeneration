/*
 * Maneuver System.cpp
 *
 * Created: 2/18/2020 3:25:51 PM
 * Author : Joseph Morga
 */ 

#define F_CPU 16000000UL  //16MHz
#define BAUD 9600
#define BAUDRATE ((F_CPU)/(BAUD*16UL)-1)

//Photoresistors 0 -> 3
#define R0 0    //Top
#define R1 1	//Bottom
#define R2 2	//Left
#define R3 3	//Right

#define frequency 10

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>

//UART for displaying the values from the photoresistors *Test Purposes Only*
void uart_Init();
void uart_Transmit(char data[]);

//To convert values from ADC to string for the UART
void convertToString(int16_t value, char word[]);
char getChar(int  digit);

void adc_Init();
uint16_t adc_read(uint8_t channel);
void dac_Init();


//Moving functions
void startManeuvering(); //Read voltage values from the 4 voltage dividers
void moveLinearActuator();
void moveStepperMotor();

char value[7];

int main(void)
{
	//Init
	
	DDRB |= (1 << DDRB5);  //Set portB 5 as output LED
	
	DDRD |= (1 << DDD2) | (1 << DDD3) | (1 << DDD4)| (1 << DDD5);
	
	DDRB &= ~(1<<DDRB7);   //Set portB 7 as input
	
	DDRC &= ~((1<<DDRC0) | (1 << DDRC1) | (1 << DDRC2) | (1 << DDRC3));
	
	PORTD |= (1 << PORTD3) | (1 << PORTD2);

	uart_Init();
	adc_Init();
	
	sei();
	while (1) {
		if(!(PINB & (1<<PINB7))) // PINB7 is low (Button has been pressed)
		{
			while(!(PINB & (1<<PINB7)));
			
			startManeuvering();
			
		}
	}
}

void startManeuvering(){
	
	PINB |= (1<<PINB5); //toggle LED
	
	moveStepperMotor();
	//moveLinearActuator();
	
	PINB |= (1<<PINB5); //toggle LED
	//We done ;)
}

void moveLinearActuator(){
	
	int16_t v0;
	int16_t v1;
	int16_t difference;
	
	v0 = adc_read(R0);              //Read voltage value v0
	
	convertToString(v0, value);     //Used to convert the value into
	uart_Transmit(value);			//a string and to display it
	
	v1 = adc_read(R1);				//Read voltage value v1
	convertToString(v1, value);
	uart_Transmit(value);
	
	difference = v0 - v1;           //Take difference
	
	convertToString(difference, value);
	uart_Transmit(value);
	
	if(difference > 50) PORTD &= ~(1 << PORTD3);       //Send signal to start retracting
	else if(difference < -50) PORTD &= ~(1 << PORTD2); //Send signal to start expanding
	
	while(difference < -50 || difference > 50){//True while the difference is outside the [-50, 50] range
		v0 = adc_read(R0);
		v1 = adc_read(R1);			//Continue reading voltage values and take difference
		difference = v0 - v1;
	}
	
	PORTD |= (1 << PORTD3) | (1 << PORTD2);  //Cut the power of the linear actuator
}

void dac_Init()
{
	DDRB |= (1<<DDB0)|(1<<DDB1);
}




uint16_t adc_read(uint8_t channel){
	
	channel &= 0b00000111;
	
	ADMUX = (ADMUX & 0xF8) | channel;
	
	ADCSRA |= (1<<ADSC);
	
	while(ADCSRA & (1<<ADSC));
	
	return ADC;
}

void adc_Init(){
	//select Vcc and select ADC1 as input
	ADMUX = (1<<REFS0); 
	
	ADCSRA = (1<<ADEN) | (1<<ADPS2) | (1<<ADPS1) | (1<<ADPS0);
}

void uart_Transmit(char data[]){
	for(int i = 0; i < 6; i++){
		while(!(UCSR0A & (1<<UDRE0)));      //wait for register to be free
		UDR0 = data[i];
	}
	
	while(!(UCSR0A & (1<<UDRE0))); 
	UDR0 = ' ';
	
	for(int i = 0; i < 6; i++) value[i] = ' ';
}

void uart_Init(){
	UBRR0H = (BAUDRATE>>8);				 //shift register to the right by 8 bits
	UBRR0L = BAUDRATE;					 //set baud rate
	UCSR0B |= (1<<TXEN0) | (1<<RXEN0);   //enable receiver and transmitter
	UCSR0C |= (1<<UCSZ00) | (1<<UCSZ01); //8 bit data format
}

void convertToString(int16_t voltage, char word[])
{
	double number = voltage;
	int divisionCount = 0;
	int digit;
	
	if(number < 0) number *= -1;
	
	while(number >= 1){
		 number = number / 10;
		 divisionCount++;
	}
	for(int i = 0; i < divisionCount && i < 6; i++){
		
		number = number * 10;
		digit = (int)number;
		number = number - digit;
		word[i] = getChar(digit);
	}
	
	word[6] = '\0';
}

char getChar(int digit){
	
	switch(digit)
	{
		case 1: return '1';
		case 2: return '2';
		case 3: return '3';
		case 4: return '4';
		case 5: return '5';
		case 6: return '6';
		case 7: return '7';
		case 8: return '8';
		case 9: return '9';
		default: return '0';
	}
}

