
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  // put your setup code here, to run once:

}

void loop() {
  if (Serial.available() > 0){
    char command = Serial.read();
    if (command == '1'){
      digitalWrite(2,HIGH);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
    }
    else if (command == '2'){
      digitalWrite(3,HIGH);
      digitalWrite(2,LOW);
      digitalWrite(4,LOW);
    }
    else if (command == '3'){
      digitalWrite(4,HIGH);
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
    }
    else if (command == '0'){
      digitalWrite(2,LOW);
      digitalWrite(3,LOW);
      digitalWrite(4,LOW);
    }
  }

  // put your main code here, to run repeatedly:

}
