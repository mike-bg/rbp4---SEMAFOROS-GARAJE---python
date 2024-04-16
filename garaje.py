import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO en modo BOARD
GPIO.setmode(GPIO.BOARD)
pin12 = 12  # Por ejemplo, para usar el pin físico 12 de la Raspberry Pi
GPIO.setup(pin12, GPIO.IN)  # Configura el pin como entrada

try:
    while True:
        # Lee el estado del pin
        estado = GPIO.input(pin12)

        # Muestra el estado
        print("Estado del pin", pin12, ":", estado)

        # Espera un segundo antes de volver a leer
        time.sleep(1)

except KeyboardInterrupt:
    # Limpiar los pines GPIO antes de salir si se presiona Ctrl+C
    GPIO.cleanup()
    print("\nPines GPIO limpiados.")
