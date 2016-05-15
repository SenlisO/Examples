import os

os.system("clear") #clear the screen

binary = raw_input("Enter your binary number:") #receive input

result = 0
stringTemp = ""
temp = 0
valid = True
for num in range(0, len(binary)):  #iterate from 1 to len string+1
    stringTemp = binary[(-1 * (num + 1))] #retrieves the binary value at current position (looping right to left)
    if stringTemp != "0" and stringTemp != "1": #if the result is not a binary value
        print ("You did not enter a binary value") #display an error
        valid = False #prevent the result from showing
        break #and stop the loop
    
    temp = int(stringTemp) #convert the string binary value to an integer

    result = result + (temp * (2 ** num)) #this converts the 1 or 0 to the appropriate binary number for its position
    #in other words, binary 1 in the third position will be converted to decimal 4

if valid: #make sure the user entered a valid binary number before printing the results
    print ("Your decimal number is:" + str(result)) #print the result
    
