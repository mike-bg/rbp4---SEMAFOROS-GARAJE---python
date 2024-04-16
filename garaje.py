import RPi.GPIO as GPIO
import time
from datetime import datetime

#cambio git no se refleja


# Configuración de los pines GPIO en modo BOARD
GPIO.setmode(GPIO.BOARD)
pin_number = 12  # Por ejemplo, para usar el pin físico 12 de la Raspberry Pi
GPIO.setup(pin_number, GPIO.IN)  # Configura el pin como entrada

try:
    while True:
        # Lee el estado del pin
        estado = GPIO.input(pin_number)

        # Obtiene la hora actual con segundos
        hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Muestra el estado del pin junto con la hora
        print(f"{hora_actual} - Estado del pin {pin_number}: {estado}")

        # Espera medio segundo antes de volver a leer
        time.sleep(0.5)

except KeyboardInterrupt:
    # Limpiar los pines GPIO antes de salir si se presiona Ctrl+C
    print("\nPrograma detenido por el usuario.")
finally:
    GPIO.cleanup()
    print("Pines GPIO limpiados.")

