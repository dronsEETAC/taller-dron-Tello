import pygame
import time

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
        time.sleep(0.1)  # Pequeña pausa para no saturar la consola

except KeyboardInterrupt:
    print("\nPrograma terminado por el usuario.")

finally:
    joystick.quit()
    pygame.quit()
