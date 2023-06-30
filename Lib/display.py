from djitellopy import Tello
import time


tello = Tello()
tello.connect()
print('BATERIA: ',tello.get_battery())

tello.send_control_command('EXT led 255 0 0')
time.sleep(5)
tello.send_control_command('EXT led 0 255 0')
time.sleep(5)
tello.send_control_command('EXT led 0 0 255')
time.sleep(5)
tello.send_control_command("EXT mled g 000000000rr00rr0rrrrrrrrrrrrrrrr0rrrrrr000rrrr00000rr00000000000")
time.sleep(5)
tello.send_control_command("EXT mled g 000bb00000bb00000bb00000bbbbbbbbbbbbbbbb0bb0000000bb0000000bb000")
time.sleep(5)
tello.send_control_command("EXT mled l r 2.5 HOLA")
time.sleep(5)
tello.send_control_command("EXT mled u g 2.5 0000b00bbb0b0b000b00b00000bb0000000b0000bbb00bbb000b0b0b0b00b0b0")
time.sleep(5)
tello.send_control_command('EXT mled s p I')
time.sleep(5)
