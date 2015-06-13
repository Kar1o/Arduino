int led1 = 2;
int led2 = 3;
int led3 = 4;
int led4 = 5;

void setup() {
  
  Serial.begin(9600);
  
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
}

void loop() {
  
  if(Serial.available() > 0){
   int inByte = Serial.read();
   Serial.println(inByte);
   switch (inByte) {
     case '0':
       digitalWrite(led1, LOW);
       digitalWrite(led2, LOW);
       digitalWrite(led3, LOW);
       digitalWrite(led4, LOW);
       break;
     case '1':
       digitalWrite(led1, HIGH);
       digitalWrite(led2, HIGH);
       digitalWrite(led3, HIGH);
       digitalWrite(led4, HIGH);
       break;
     case '2':
       digitalWrite(led1, HIGH);
       break;
     case '3':
       digitalWrite(led2, HIGH);
       break;
     case '4':
       digitalWrite(led3, HIGH);
       break;
     case '5':
       digitalWrite(led4, HIGH);
       break;
     case '11':
       digitalWrite(led1, LOW);
       break;
     case '12':
       digitalWrite(led2, LOW);
       break;
     case '13':
       digitalWrite(led3, LOW);
       break;
     case '14':
       digitalWrite(led4, LOW);
       break;
   }
  }
  delay(350); 
}
