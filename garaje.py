import RPi.GPIO as GPIO
import time

# Configurar el modo de los pines (BCM o BOARD)
GPIO.setmode(GPIO.BCM)

# Definir el pin GPIO (por ejemplo, GPIO17)
relay_pin = 17

# Configurar el pin como salida
GPIO.setup(relay_pin, GPIO.OUT)

# Función para encender el relé
def relay_on():
    GPIO.output(relay_pin, GPIO.HIGH)  # HIGH para activar el relé

# Función para apagar el relé
def relay_off():
    GPIO.output(relay_pin, GPIO.LOW)  # LOW para desactivar el relé

try:
    while True:
        relay_on()
        time.sleep(2)  # Relé encendido por 2 segundos
        relay_off()
        time.sleep(2)  # Relé apagado por 2 segundos
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
