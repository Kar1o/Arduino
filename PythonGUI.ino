#include <RelayBoard.h> //Inclui a biblioteca RelayBoard.h

#define data    6 //Define a palavra data como 6 para o pino D6 ser utilizado como o pino do DATA
#define strobe  3 //Define a palavra strobe como 4 para o pino D4 ser utilizado como o pino do STROBE
#define clock   2 //Define a palavra clock como 2 para o pino D2 ser utilizado como o pino do CLOCK
#define numberboards 2 //Define a palavra numberboards como 2, onde é definido quantas RelayBoard há no circuito

RelayBoard relay(data, strobe, clock, numberboards);

void setup() {
  
  Serial.begin(9600);
}

void loop() {
  
  if(Serial.available() > 0){
   int inByte = Serial.read();
   Serial.println(inByte);
   switch (inByte) {
     case '0':
       relay.set(0,0,1);
       relay.set(0,1,1);
       relay.set(0,2,1);
       relay.set(0,3,1);
       relay.set(0,4,1);
       relay.set(0,5,1);
       relay.set(0,6,1);
       relay.set(0,7,1);
       break;
       
     case '1':
       relay.set(0,0,0);
       relay.set(0,1,0);
       relay.set(0,2,0);
       relay.set(0,3,0);
       relay.set(0,4,0);
       relay.set(0,5,0);
       relay.set(0,6,0);
       relay.set(0,7,0);
       break;
       
     case '2':
       relay.set(0,0,1);
       break;
       
     case '3':
       relay.set(0,1,1);
       break;
       
     case '4':
       relay.set(0,2,1);
       break;
       
     case '5':
       relay.set(0,3,1);
       break;
       
     case '6':
       relay.set(0,4,1);
       break;
       
     case '7':
       relay.set(0,5,1);
       break;
       
     case '8':
       relay.set(0,6,1);
       break;
       
     case '9':
       relay.set(0,7,1);
       break;
       
   }
  }
  delay(500); 
}
