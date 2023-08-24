from microbit import pin0
	
#Alias vergeben
s = pin0.read_analog()

while True:
    print("Lautstärke:",s)
