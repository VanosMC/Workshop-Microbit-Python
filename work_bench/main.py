from microbit   import pin0, pin1, pin2, pin8, sleep, statistics

while True:
    # Werte messen mit Analog Sound Sensor
    s = pin0.read_analog()
    sleep(60)
    print(s)

    # Generiere eine Liste mit Werte der letzte Minute
    myList = #Liste generieren, aber wie?

    # Mittelwert dieser Werte berechnen
    mean = statistics.mean(myList)
    print("Mittelwert =" + str(mean))    

    # pins alle ausschalten
    pin1.write_digital(0)
    pin2.write_digital(0)
    pin8.write_digital(0)

    # schlussfolgerung Mittelwert
    if s < 50:
        pin1.write_digital(1)

    elif s >= 500  and s < 150:
        pin2.write_digital(1)

    else:
        pin8.write_digital(1)

