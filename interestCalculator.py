import os

"""
Interest Calculator
Version 1.1
By Richard Romick

Program to calculate interest in loans

changelog:
V1.2: implemented future value calculator.  Created menu loop.  Added clear screen.
      also cleaned up main menu error code

V1.1: implemented interest calculations with monthly additions.  To support this, a main menu is added.
      interest calculations w/ monthly additions on loans math is not verified

V1.0: implemented annualCompoundInterest function.  It calculates interst at the most basic level
"""
def futureValueCalculator():
        """
        This function calculates how much principle you need to reach a certain goal
        Parameters: none
        Returns: none

        P = A / ( 1 + r/n ) ^ nt.
        A = the future value of the investment/loan, including interest
        P = the principal investment amount (the initial deposit or loan amount)
        r = the annual interest rate (decimal)
        n = the number of times that interest is compounded per year
        t = the number of years the money is invested or borrowed for 
        """
        
        #step 1: receive user input
        finished = False                                                         #control variable for loops

        while (not finished):                                                    #loop to receive principle
                goal = float(raw_input("Enter goal:"))                           #receive goal as raw_input, convert to float
                if goal < 0:                                                     #if goal is not positive
                        print ("Enter a positive number")                        #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop
        
        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive interest rate
                interestRate = float(raw_input("Enter interest rate (0-100):"))  #receive interest rate as raw_input, convert to float
                if interestRate < 0 or interestRate > 100:                       #if interest rate is not 0-100
                        print ("Enter a number between 0 and 100")               #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive annual compounds
                annualCompounds = int(raw_input("Enter number of times interest is compounded per year:"))  #receive annual compounds as raw_input, convert to int
                if annualCompounds < 1:                                          #if annualCompounds is not 1 or more (must compound at least annually)
                        print ("Enter a number greater than 1")                  #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive number of years invested/borrowed
                months = float(raw_input("Enter number of months until your goal:"))#receive months invested/borrowed as raw_input, convert to float
                if months < 0:                                                    #if months is not positive
                        print ("Enter a positive number")                        #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        #step 2: make calculations
        principal = goal / ((1 + (interestRate / 100) / annualCompounds) ** (annualCompounds * (months / 12))) #calculate the required principle

        #step 3: display results
        print ("Required principal is %s" % principal)                           #displaying the principle
        delay = raw_input("Press enter to continue")                            #input to delay program clearing the screen        
        
def annualCompoundInterestWAdditions():
        """
        This function calculates interest while adding monthly contributions
        Parameters: none
        Returns: none


        Compound interest for principal (CIFP): 
        P(1+r/n)^nt

        Future value of a series (FVOS):
        PMT * (((1 + r/n)^nt - 1) / (r/n))

        A = CIFP + FVOS

        A = the future value of the investment/loan, including interest
        P = the principal investment amount (the initial deposit or loan amount)
        PMT = the monthly payment
        r = the annual interest rate (decimal)
        n = the number of times that interest is compounded per year
        t = the number of years the money is invested or borrowed for 
        """
        
        #step 1: receive user input
        finished = False                                                         #control variable for loops

        while (not finished):                                                    #loop to receive principle
                principal = float(raw_input("Enter principal:"))                 #receive principal as raw_input, convert to float
                if principal < 0:                                                #if principal is not positive
                        print ("Enter a positive number")                        #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop
        
        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive interest rate
                interestRate = float(raw_input("Enter interest rate (0-100):"))  #receive interest rate as raw_input, convert to float
                if interestRate < 0 or interestRate > 100:                       #if interest rate is not 0-100
                        print ("Enter a number between 0 and 100")               #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive annual compounds
                annualCompounds = int(raw_input("Enter number of times interest is compounded per year:"))  #receive annual compounds as raw_input, convert to int
                if annualCompounds < 1:                                          #if annualCompounds is not 1 or more (must compound at least annually)
                        print ("Enter a number greater than 1")                  #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive number of years invested/borrowed
                months = float(raw_input("Enter number of months invested/borrowed:"))#receive months invested/borrowed as raw_input, convert to float
                if months < 0:                                                    #if months is not positive
                        print ("Enter a positive number")                        #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive number monthly additions
                monthlyAddition = float(raw_input("enter monthly addition:"))    #receive monthly addition as raw_input, convert to float
                if monthlyAddition < 0:                                          #monthly addition must be positive
                        print ("Enter a positive number")                        #error message is displayed
                else:
                        finished = True                                          #exit while loop

        finished = False                                                         #reset finished variable
        loan = False                                                             #loan is a boolean for loan vs investment
        while (not finished):                                                    #loop to receive loan vs investment
                temp = raw_input("Is this a [l]oan or [i]nvestment:")            #receive loan vs investment as raw input
                finished = True                                                  #assume input is going to be valid
                if temp == "l":                                                  #case that user enters loan
                        loan = True                                              #set loan variable to true
                elif temp == "i":                                                #case that user enters invesement
                        loan = False                                             #set loan variable to false
                else:                                                            #case that users input is invalid
                        print ("Enter \"l\" or \"i\"")                           #display an error message
                        finished = False                                         #set loop to repeat

        if loan:                                                                 #if loan
                monthlyAddition = monthlyAddition - (monthlyAddition * 2)        #change monthly addition to a negative value

        #step 2: perform calculations
        CIFP = principal * ((1 + ((interestRate / 100) / annualCompounds)) ** (annualCompounds * (months / 12)))  #Compound interest for principle calculated
        FVOS = monthlyAddition * (((1 + (interestRate / 100) / annualCompounds) ** (annualCompounds * (months / 12)) - 1) / ((interestRate / 100) / annualCompounds)) #Future value of Series calculated

        #step 3: display result
        print ("Ending balance is %s" % (CIFP + FVOS))                           #print results

        delay = raw_input("Press enter to continue")                            #input to delay program clearing the screen
        
def annualCompoundInterest():
        """
        This function calculates interest at the most basic level
        Parameters: none
        Returns: none
        
        #forumula
        A = P (1 + r/n) ^ nt
        
        A = the future value of the investment/loan, including interest
        P = the principal investment amount (the initial deposit or loan amount)
        r = the annual interest rate (decimal)
        n = the number of times that interest is compounded per year
        t = the number of years the money is invested or borrowed for 
        """

        #step 1: receive user input
        finished = False                                                         #control variable for loops

        while (not finished):                                                    #loop to receive principle
                principal = float(raw_input("Enter principal:"))                 #receive principal as raw_input, convert to float
                if principal < 0:                                                #if principal is not positive
                        print ("Enter a positive number")                        #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop
        
        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive interest rate
                interestRate = float(raw_input("Enter interest rate (0-100):"))  #receive interest rate as raw_input, convert to float
                if interestRate < 0 or interestRate > 100:                       #if interest rate is not 0-100
                        print ("Enter a number between 0 and 100")               #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive annual compounds
                annualCompounds = int(raw_input("Enter number of times interest is compounded per year:"))  #receive annual compounds as raw_input, convert to int
                if annualCompounds < 1:                                          #if annualCompounds is not 1 or more (must compound at least annually)
                        print ("Enter a number greater than 1")                  #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        finished = False                                                         #reset finished variable
        while (not finished):                                                    #loop to receive number of years invested/borrowed
                months = float(raw_input("Enter number of months invested/borrowed:"))#receive months invested/borrowed as raw_input, convert to float
                if months < 0:                                                    #if months is not positive
                        print ("Enter a positive number")                        #error message is displayed
                else:                                                            #case that input is valid
                        finished = True                                          #exit while loop

        #step 2: calculate interest
        result = principal * ((1 + ((interestRate / 100) / annualCompounds)) ** (annualCompounds * (months / 12)))  #interest is calculated

        #step 3: display results
        print ("Resulting account balance is:   %s" % result)                   #display resulting balance
        print ("Accrued interest is:            %s" % (result - principal))     #display interest

        delay = raw_input("Press enter to continue")                            #input to delay program clearing the screen

        
quitting = False                                                                #variable will exit program when true
error = False                                                                   #variable will be true if the user just made an error

while not quitting:                                                             #only quitters quit
        os.system('cls' if os.name == "nt" else 'clear')                        #clear the screen
        print ("Interest Calculator")                                           #display intro and main menu
        print ("By Richard Romick")
        print ("Version 1.1\n")
        print ("Main Menu:")
        print ("1 - Simple interest calculations")
        print ("2 - Interest calculations w/ Monthly Additions")
        print ("3 - Future value calculator")
        print ("0 - quit program")

        if error:                                                               #case that the user made an error their last choice
                print ("That is not a valid command")                           #dislay an error message

        choice = int(raw_input("Choice:"))                                      #user chooses a menu option in raw_input converted to int
        
        if choice == 1:                                                         #case that user wants simple interest calculations
                annualCompoundInterest()                                        #start annualCompoundInterest function
        elif choice == 2:                                                       #case that user wants interest calculation with additions
                annualCompoundInterestWAdditions()                              #start annualCompoundsInterestWAdditions function
        elif choice == 3:                                                       #case that user wants future value calculator
                futureValueCalculator()                                         #start future value calculator
        elif choice == 0:                                                       #case that the user wants to quit
                quitting = True                                                 #set quitting to true so program loop exits
        else:                                                                   #case that user makes invalid choice
                error = True                                                    #the user made an error, we are going to display a message
