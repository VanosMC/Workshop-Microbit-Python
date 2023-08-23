from microbit import pin1, pin2, pin5, sleep

while True:
    pin1.write_digital(1)
    sleep(2000)
    pin1.write_digital(0)
    for x in range(3):
        pin2.write_digital(1)
        sleep(500)
        pin2.write_digital(0)
        sleep(500)
    pin5.write_digital(1)
    sleep(2000)
    pin5.write_digital(0)