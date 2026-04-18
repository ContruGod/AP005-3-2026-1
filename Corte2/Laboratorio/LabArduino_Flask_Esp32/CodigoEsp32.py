import machine
import network
import socket
import urequests
import time

print("Reiniciando ESP32...")
time.sleep(1)

# ---------------- WIFI ----------------
ssid = "Familia Martinez"
password = "Mv79285324**"

pc_ip = "http://192.168.1.7:5000"

# ---------------- IP FIJA ----------------
ip = "192.168.1.50"
gateway = "192.168.1.7"
subnet = "255.255.255.0"
dns = "8.8.8.8"

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.ifconfig((ip, subnet, gateway, dns))
wifi.connect(ssid, password)

while not wifi.isconnected():
    time.sleep(0.2)

print("Conectado ESP32")
print("IP fija:", wifi.ifconfig()[0])

# ---------------- SERVER ----------------
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

# ---------------- PC SEND ----------------
def send_to_pc(cmd):
    try:
        print("ENVIANDO AL PC:", cmd)
        r = urequests.get(pc_ip + "/cmd/" + cmd)
        print("RESPUESTA:", r.text)
        r.close()
    except Exception as e:
        print("ERROR PC:", e)

# ---------------- HTML ----------------
html = """\
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ESP32 Control LED</title>

<style>
body {
    margin: 0;
    font-family: Arial;
    background: #0b1220;
    color: white;
    text-align: center;
}

h1 { color: #38bdf8; }

.card {
    background: #111827;
    margin: 20px auto;
    padding: 20px;
    width: 90%;
    max-width: 500px;
    border-radius: 20px;
}

button {
    padding: 12px;
    margin: 8px;
    width: 45%;
    border: none;
    border-radius: 10px;
    font-weight: bold;
    cursor: pointer;
}

.on { background: #22c55e; }
.off { background: #ef4444; }

.m1 { background: #3b82f6; }
.m2 { background: #a855f7; }
.m3 { background: #f59e0b; }
.m4 { background: #14b8a6; }
.m5 { background: #ef4444; }
</style>
</head>

<body>

<h1>Control de LEDs ESP32</h1>

<div class="card">

<a href="/encender"><button class="on">ENCENDER</button></a>
<a href="/apagar"><button class="off">APAGAR</button></a>

<a href="/barrido"><button class="m1">BARRIDO</button></a>
<a href="/estroboscopico"><button class="m2">ESTROBOSCÓPICO</button></a>

<a href="/respiracion"><button class="m3">RESPIRACIÓN</button></a>
<a href="/onda"><button class="m4">ONDA</button></a>

<a href="/random"><button class="m6">RANDOM</button></a>
<a href="/semaforo"><button class="m3">SEMÁFORO</button></a>

</div>

</body>
</html>
"""

# ---------------- LOOP ----------------
while True:
    cl, addr = s.accept()

    # ✔ SOLO LA PRIMERA LINEA HTTP (FIX IMPORTANTE)
    request = cl.recv(1024).decode().split("\r\n")[0]

    print("REQUEST:", request)

    # ---------------- IGNORAR FAVICON ----------------
    if "favicon.ico" in request:
        cl.close()
        continue

    # ---------------- COMANDOS LIMPIOS ----------------
    if "GET /encender " in request:
        send_to_pc("ENCENDER")

    elif "GET /apagar " in request:
        send_to_pc("APAGAR")

    elif "GET /barrido " in request:
        send_to_pc("BARRIDO_LUMINICO")

    elif "GET /estroboscopico " in request:
        send_to_pc("ESTROBOSCOPICO")

    elif "GET /respiracion " in request:
        send_to_pc("EFECTO_RESPIRACION")

    elif "GET /onda " in request:
        send_to_pc("ONDA_LUMINICA")

    elif "GET /random " in request:
        send_to_pc("MODO_RANDOM")
    elif "GET /semaforo " in request:
        send_to_pc("SEMAFORO")

    # ---------------- RESPUESTA WEB ----------------
    cl.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
    cl.send(html)
    cl.close()