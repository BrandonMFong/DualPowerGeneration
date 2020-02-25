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
#define R0 0    //Left
#define R1 1	//Top
#define R2 2	//Right
#define R3 3	//Bottom

#include <avr/io.h>
#include <util/delay.h>
#include <avr/interrupt.h>
#include <stdio.h>

//UART for displaying the values from the photoresistors *Test Purposes Only*
void uart_Init();
void uart_Transmit(char data[]);

//To convert values from ADC to string for the UART
void convertToString(uint16_t value, char word[]);
char getChar(int  digit);

void adc_Init();
uint16_t adc_read(uint8_t channel);
void dac_Init();


//Moving functions
void beginReading(); //Read voltage values from the 4 voltage dividers
void moveLinearActuator(uint16_t v1, uint16_t v2);
void moveTheOtherMotorWhoseNameIDontKnow(uint16_t v1, uint16_t v2);


char value[6];

int main(void)
{
	//Init
	
	DDRB |= (1 << DDRB5);  //Set portB 5 as output LED
	DDRB &= ~(1<<DDRB7);   //Set portB 7 as input
	DDRC &= ~(1<<DDRC0);
	
	uart_Init();
	adc_Init();
	
	sei();
	while (1) {
		if(!(PINB & (1<<PINB7))) // PINB7 is low (Button has been pressed)
		{
			while(!(PINB & (1<<PINB7)));
			
			PINB |= (1<<PINB5); //toggle LED
		}
	}
}

void beginReading(){
	//Photoresistor channels
	uint16_t v0;
	uint16_t v1;
	uint16_t v2;
	uint16_t v3;
	
	v0 = adc_read(R0);
	v1 = adc_read(R1);
	v2 = adc_read(R2);
	v3 = adc_read(R3);
	
	moveLinearActuator(v0, v2);
	//moveTheOtherMotorWhoseNameIDontKnow(v1,v3);
	
	//We done ;)
}

void moveLinearActuator(uint16_t v1, uint16_t v2){
	
	//Work in progress
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
}

void uart_Init(){
	UBRR0H = (BAUDRATE>>8);				 //shift register to the right by 8 bits
	UBRR0L = BAUDRATE;					 //set baud rate
	UCSR0B |= (1<<TXEN0) | (1<<RXEN0);   //enable receiver and transmitter
	UCSR0C |= (1<<UCSZ00) | (1<<UCSZ01); //8 bit data format
}

void convertToString(uint16_t value, char word[])
{
	double number = value;
	int divisionCount = 0;
	int digit;
	
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

