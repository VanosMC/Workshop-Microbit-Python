from microbit   import pin0, pin1, pin2, pin8, sleep

# Bedingungen
keinWert = 10
ok = 300
nichtok = 400

while True:
    # Werte messen mit Analog Sound Sensor
    s = pin0.read_analog()
    sleep(100)
    print(s)

    # pins alle ausschalten, damit keine doppelt Besetzung entsteht.
    pin1.write_digital(0)
    pin2.write_digital(0)
    pin8.write_digital(0)

    # Wenn keine Werte gemessen sind die Pins ausgeschalten.   
    if s <= keinWert:
        pin1.write_digital(0)
        pin2.write_digital(0)
        pin8.write_digital(0)

    # Wenn einen Wert rauskommt.
    elif s < ok and s > keinWert:
        pin1.write_digital(1)
        sleep(1000)

    elif s > nichtok:
        pin8.write_digital(1)
        sleep(1000)
    
    elif s > ok and s < nichtok:
        pin2.write_digital(1)
        sleep(1000)
      
    
        