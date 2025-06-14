import pygame
import time
from djitellopy import Tello


def cambiarEscala( value):
    """
    Convierte valor del eje (-1 a 1) a rango RC (-100 a 100)
    """
    if value < 0:
        value = -value
        return int(-value * value * value * value * 100)
    else:
        return int(value * value * value * value * 100)

tello = Tello()
tello.connect()
print('BATERIA: ',tello.get_battery())


# Inicializar pygame y el módulo de joystick
pygame.init()
pygame.joystick.init()

# Verificar si hay joysticks conectados
print ("Numero de joystics :", pygame.joystick.get_count())
if pygame.joystick.get_count() == 0:
    print("No hay joysticks conectados.")
    pygame.quit()
    exit()

# Obtener el primer joystick
joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Joystick detectado: {joystick.get_name()}")
volando = False
try:
    while True:
        # Procesar eventos de pygame (necesario para actualizar el estado del joystick)
        pygame.event.pump()

        # Leer valores de los ejes
        axes = [joystick.get_axis(i) for i in range(joystick.get_numaxes())]
        print("Ejes:", ["{:.2f}".format(a) for a in axes])

        # Leer estado de botones
        buttons = [joystick.get_button(i) for i in range(joystick.get_numbuttons())]
        print("Botones:", buttons)

        # Leer hats (crucetas digitales)
        hats = [joystick.get_hat(i) for i in range(joystick.get_numhats())]
        print("Hats:", hats)

        print("-" * 40)

        if buttons[8] == 1:
            tello.takeoff()
            volando = True
        elif buttons[9] == 1:
            tello.land()

        elif volando:
            lr = cambiarEscala(axes[3])  # RC1
            fb = cambiarEscala(-axes[2])  # RC2
            ud = cambiarEscala(-axes[1])  # RC3
            yaw = cambiarEscala(axes[0])  # RC4

            tello.send_rc_control(lr, fb, ud, yaw)



        time.sleep(0.1)  # Pequeña pausa para no saturar la consola

except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")

finally:
    joystick.quit()
    pygame.quit()
