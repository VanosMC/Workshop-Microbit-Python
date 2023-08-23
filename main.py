# mein Projekt

from microbit import pin0, pin1, pin2, pin3, sleep

#Alias vergeben
s = pin0.read_analog()

while True:
    print(s)

    if s >= 6000:
        pin3.write_digital(1)
        
    elif s >= 4000 and s < 6000:
        pin2.write_digital(1)

    else:
        pin1.write_digital(1)
    pin1.write_digital(0)
    pin2.write_digital(0)
    pin3.write_digital(0)
    sleep(1000)
