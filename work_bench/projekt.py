
from microbit import pin0, pin2, pin8, pin9, sleep

geradeAcceptable = 100
nichtAcceptable = 200

  # Generiere eine Liste mit Werte der letzte Minute 100 Messungen
MeasuringPeriod = 60000

myList = []
while True
    # Werte erzeugen und in einer Liste eingeben
    s = pin0.read_analog()
    print(s)
    myList.append(s)
        
    # Mittelwert dieser Liste berechnen
    mean = statistics.mean(myList)
    print("Mittelwert =" + str(mean))    
