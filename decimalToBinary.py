import os

os.system("clear") #clear the screen

valid = False
decimal = 0
binary = ""
exponent = 0

#receive input
while not valid:
    valid = True
    try:
        decimal = int(input("Enter you decimal integer:")) #receive input
    except TypeError:
        print ("You did not enter a valid integer")
        valid = False
    except NameError:
        print ("You did not enter a valid integer")
        valid = False


#begin computing the binary number
while decimal > 1:
    if decimal % 2 == 0:
        binary = "0" + binary
    else:
        binary = "1" + binary
    decimal = decimal / 2

    
if decimal == 0:
    binary = "0" + binary
else:
    binary = "1" + binary
    
        
#print the binary
print ("Your binary result is:" + binary)

    
