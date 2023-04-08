#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define ENC_A 14
#define ENC_B 16
#define BUT1 13
#define BUT2 12
#define SDA 5
#define SCL 4
#define BAT A0
#define BAT_CH 0

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

int stepEnc1 = 0;
int stepEnc2 = 0;
int lenght = 0;
int error_mes = 0;
float lenght_factor = 1.9;

IRAM_ATTR void int1()
{
  stepEnc1++;
  if (digitalRead(ENC_B) != 1) stepEnc2++;
  else stepEnc2--;
  if (stepEnc1!=abs(stepEnc2)) error_mes=1;
  lenght=stepEnc1/lenght_factor;
}

void setup()
{
  Serial.begin(9600);
  Wire.begin(SDA, SCL);
  if (!display.begin(SSD1306_SWITCHCAPVCC, 0x3C))
  {
    Serial.println(F("SSD1306 allocation failed"));
    for (;;)
      ;
  }
  pinMode(ENC_A, INPUT);
  pinMode(ENC_B, INPUT);
  pinMode(BUT1, INPUT);
  pinMode(BUT2, INPUT);
  pinMode(BAT_CH, INPUT);
  attachInterrupt(digitalPinToInterrupt(ENC_A), int1, RISING);

  display.setTextColor(WHITE);
  display.clearDisplay();
}

void loop()
{
  if (digitalRead(BUT1) == 1)
  {
    stepEnc1 = 0;
    stepEnc2 = 0;
    error_mes = 0;
  }
  

  display.clearDisplay();

  display.setCursor(10, 10);
  display.printf("Enc1 - %d ", stepEnc1);

  if (error_mes==0)
  {
  display.setCursor(10, 20);
  display.printf("Length - %d cm", lenght);
  }
  else if (error_mes==1)
  {
  display.setCursor(10, 20);
  display.printf("Length - Error!");
  }

  display.setCursor(10, 30);
  display.printf("Enc2 - %d ", stepEnc2);

  display.setCursor(10, 40);
  display.printf("Bat - %d", analogRead(BAT));

  display.setCursor(10, 50);
  display.printf("Uptime - %d s", int(millis() / 1000));

  display.display();
}
