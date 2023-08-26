from microbit   import pin0, pin1, pin2, pin8, sleep, statistics

geradeAcceptable = 100
nichtAcceptable = 200

while True:
    # Werte messen mit Analog Sound Sensor
    s = pin0.read_analog()
    sleep(600)
    print(s)

    # Generiere eine Liste mit Werte der letzte Minute 100 Messungen
    myList = #Liste generieren, aber wie?

    # Mittelwert dieser Werte berechnen
    mean = statistics.mean(myList)
    print("Mittelwert =" + str(mean))    

    # pins alle ausschalten
    pin1.write_digital(0)
    pin2.write_digital(0)
    pin8.write_digital(0)

    # schlussfolgerung Mittelwert
    if mean < geradeAcceptable
        pin1.write_digital(1)

    elif mean > nichtAcceptable
        pin8.write_digital(1)

    else:
        pin2.write_digital(1)

