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

```
mi_proyecto_iot/
│
├── app.py
├── serial_a_csv.py
├── datos_potenciometro.csv
│
├── templates/
│   └── index.html
│
└── static/
    └── grafica_potenciometro.png
```

---

## Ejecución del proyecto

1. Conectar el ESP32 al computador.
2. Ejecutar el script de lectura serial:

```
python serial_a_csv.py
```

3. En otra terminal ejecutar el servidor web:

```
python app.py
```

4. Abrir el navegador en:

```
http://127.0.0.1:5000
```

---

## Resultados

El sistema permite visualizar:

- Lectura en tiempo real del potenciómetro
- Gráfica de las últimas muestras
- Tabla de datos
- Resumen estadístico (mínimo, máximo, promedio)

---

## Evidencia

![imagen1](img/imagen1.png)
![imagen2](img/imagen2.png)
![imagen3](img/imagen3.png)

---

## Autor

Proyecto realizado por: Felipe Ayala y Kevin Hurtado
