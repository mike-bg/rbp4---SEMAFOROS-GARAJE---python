import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO
RELAY_PIN_1 = 23
RELAY_PIN_2 = 24
IR_SENSOR_PIN = 17

# Configuración de la librería RPi.GPIO
GPIO.setmode(GPIO.BCM)  # Usamos la numeración BCM
GPIO.setup(RELAY_PIN_1, GPIO.OUT)  # Configuramos el pin 23 como salida
GPIO.setup(RELAY_PIN_2, GPIO.OUT)  # Configuramos el pin 24 como salida
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)  # Configuramos el pin 17 como entrada

try:
    while True:
        # Leer el estado del sensor de infrarrojos
        ir_state = GPIO.input(IR_SENSOR_PIN)
        if ir_state == GPIO.HIGH:
            print("Objeto detectado")
        else:
            print("No se detecta objeto")

        time.sleep(.5)

        # Activar los relés
        #GPIO.output(RELAY_PIN_1, GPIO.HIGH)
        #GPIO.output(RELAY_PIN_2, GPIO.HIGH)
        #print("Relés activados")
        #time.sleep(1)  # Espera 1 segundo

        # Desactivar los relés
        #GPIO.output(RELAY_PIN_1, GPIO.LOW)
        #GPIO.output(RELAY_PIN_2, GPIO.LOW)
        #print("Relés desactivados")
        #time.sleep(1)  # Espera 1 segundo

except KeyboardInterrupt:
    # Limpiar los GPIO en caso de interrupción
    GPIO.cleanup()
    print("Programa terminado")

finally:
    # Limpiar los GPIO al final del programa
    GPIO.cleanup()
