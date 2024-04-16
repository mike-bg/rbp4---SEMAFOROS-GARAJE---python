import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO en modo BOARD
GPIO.setmode(GPIO.BOARD)
pin_number = 12  # Por ejemplo, para usar el pin físico 12 de la Raspberry Pi
GPIO.setup(pin_number, GPIO.IN)  # Configura el pin como entrada

try:
    while True:
        # Lee el estado del pin
        estado = GPIO.input(pin_number)

        # Muestra el estado
        print("Estado del pin", pin_number, ":", estado)

        # Espera un segundo antes de volver a leer
        time.sleep(1)

except KeyboardInterrupt:
    # Limpiar los pines GPIO antes de salir si se presiona Ctrl+C
    print("\nPrograma detenido por el usuario.")
finally:
    GPIO.cleanup()
    print("Pines GPIO limpiados.")
