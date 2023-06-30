from djitellopy import Tello
import time

tello = Tello()
tello.connect()
print('BATERIA: ',tello.get_battery())

tello.takeoff()
tello.move_left(50)
tello.move_up(50)
tello.rotate_clockwise(90)
tello.move_forward(50)
tello.land()