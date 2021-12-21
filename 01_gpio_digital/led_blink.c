/*#include <wiringPi.h>
#define LED_PIN 4
int main (void)
{
  //wiringPiSetup () ;
  wiringPiSetupGpio () ;
  pinMode (LED_PIN, OUTPUT) ;
  for (int i=0; i<5; i++)
  {
    digitalWrite (LED_PIN, HIGH) ; delay (1000) ;
    digitalWrite (LED_PIN,  LOW) ; delay (1000) ;
  }
  return 0 ;
}*/

#include <wiringPi.h>
#define LED_R 4
#define LED_Y 25
#define LED_G 24
int main(void){
  wiringPiSetupGpio();
  pinMode (LED_R, OUTPUT);
  pinMode (LED_Y, OUTPUT);
  pinMode (LED_G, OUTPUT);

  digitalWrite(LED_R, HIGH); delay(2000);
  digitalWrite(LED_R, LOW);
  digitalWrite(LED_Y, HIGH); delay(2000);
  digitalWrite(LED_Y, LOW);
  digitalWrite(LED_G, HIGH); delay(2000);
  digitalWrite(LED_G, LOW);

  return 0;
}
