# Monitoreo de Potenciómetro con ESP32 y Python

## Descripción del proyecto

Este proyecto consiste en la lectura de un potenciómetro usando un ESP32, el envío de los datos al computador mediante comunicación serial, su almacenamiento en un archivo CSV con Python y su visualización en una página web usando Flask.

El sistema integra conceptos de electrónica, programación y desarrollo web.

---

## Tecnologías utilizadas

- ESP32 (Arduino IDE)
- Python 3
- Flask
- Pandas
- Matplotlib
- PySerial
- HTML

---

## Funcionamiento del sistema

1. El potenciómetro genera una señal analógica.
2. El ESP32 la convierte a un valor digital (0 - 4095).
3. Los datos se envían por puerto serial al computador.
4. Python recibe los datos y los guarda en un archivo CSV.
5. Flask lee el CSV, genera una gráfica y muestra los datos en una página web.
6. El navegador muestra los resultados en tiempo real.

---

## Estructura del proyecto
