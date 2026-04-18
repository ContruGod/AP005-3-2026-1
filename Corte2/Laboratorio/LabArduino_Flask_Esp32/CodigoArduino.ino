String cmd = "";

int leds[] = {2,3,4,5,6,7,8,9,10,11};

void setup() {
  Serial.begin(115200);

  randomSeed(micros());

  for (int i = 0; i < 10; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {

  if (Serial.available()) {
    cmd = Serial.readStringUntil('\n');
    cmd.trim();

    Serial.println(cmd);

    if (cmd == "ENCENDER") encender();
    else if (cmd == "APAGAR") apagar();
    else if (cmd == "BARRIDO_LUMINICO") barrido();
    else if (cmd == "ESTROBOSCOPICO") estroboscopico();
    else if (cmd == "EFECTO_RESPIRACION") respiracion();
    else if (cmd == "ONDA_LUMINICA") onda();
    else if (cmd == "MODO_RANDOM") randomMode();
    else if (cmd == "SEMAFORO") semaforo();
  }
}

// ---------------- FUNCIONES ----------------

void encender() {
  for (int i = 0; i < 10; i++) digitalWrite(leds[i], HIGH);
}

void apagar() {
  for (int i = 0; i < 10; i++) digitalWrite(leds[i], LOW);
}

void barrido() {
  for (int i = 0; i < 10; i++) {
    digitalWrite(leds[i], HIGH);
    delay(80);
    digitalWrite(leds[i], LOW);
  }

  for (int i = 10; i >= 0; i--) {
    digitalWrite(leds[i], HIGH);
    delay(80);
    digitalWrite(leds[i], LOW);
  }
}

void estroboscopico() {
  for (int i = 0; i < 10; i++) digitalWrite(leds[i], HIGH);
  delay(80);
  for (int i = 0; i < 10; i++) digitalWrite(leds[i], LOW);
  delay(80);
}

void respiracion() {

  for (int b = 0; b <= 1; b++) {
    for (int i = 0; i < 10; i++) {
      digitalWrite(leds[i], HIGH);
    }
    delay(300);

    for (int i = 0; i < 10; i++) {
      digitalWrite(leds[i], LOW);
    }
    delay(300);
}


  for (int b = 255; b >= 0; b -= 5) {
    for (int i = 0; i < 10; i++) analogWrite(leds[i], b);
    delay(10);
  }
}

void onda() {
  for (int i = 0; i < 10; i++) {
    digitalWrite(leds[i], HIGH);
    delay(50);
  }

  for (int i = 0; i < 10; i++) {
    digitalWrite(leds[i], LOW);
    delay(50);
  }
}

void randomMode() {
  for (int i = 0; i < 10; i++) {
    digitalWrite(leds[i], random(0, 2));
  }

  delay(150);

  for (int i = 0; i < 10; i++) {
    digitalWrite(leds[i], LOW);
  }

  delay(100);
}
void semaforo() {

  // ---------------- ROJO ----------------
  for (int i = 11; i >= 7; i--) {
    digitalWrite(i, HIGH);
  }
  delay(2000);

  for (int i = 11; i >= 7; i--) {
    digitalWrite(i, LOW);
  }

  // ---------------- AMARILLO ----------------
  for (int i = 6; i >= 5; i--) {
    digitalWrite(i, HIGH);
  }
  delay(1000);

  for (int i = 6; i >= 5; i--) {
    digitalWrite(i, LOW);
  }

  // ---------------- VERDE ----------------
  for (int i = 4; i >= 2; i--) {
    digitalWrite(i, HIGH);
  }
  delay(2000);

  for (int i = 4; i >= 2; i--) {
    digitalWrite(i, LOW);
  }
}