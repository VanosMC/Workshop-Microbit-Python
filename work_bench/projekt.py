
from microbit import pin0, pin2, pin8, pin9, sleep



while True:
    s = pin0.read_analog()
    print(s)

    if s >= 250:
        pin9.write_digital(1)
        
    elif s >= 100  and s < 250:
        pin8.write_digital(1)

    else:
        pin2.write_digital(1)
    pin2.write_digital(0)
    pin8.write_digital(0)
    pin9.write_digital(0)
    sleep(1000)
