from flask import Flask
import serial
import time

app = Flask(__name__)

time.sleep(2)

arduino = serial.Serial('COM4', 115200, timeout=1)

@app.route("/cmd/<comando>")
def cmd(comando):
    try:
        print("Recibido:", comando)
        arduino.write((comando + "\n").encode())
        return "OK"
    except Exception as e:
        print("ERROR:", e)
        return "ERROR"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)