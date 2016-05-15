from Tkinter import *

class GUI():
    operaion = ""
    store = 0

    def __init__(self, main):
        self.display = Entry(main)
        self.buttonPlus = Button(main, text = "+")
        self.buttonMinus = Button(main, text = "-")
        self.buttonDivide = Button(main, text = "/")
        self.buttonMultiply = Button(main, text = "*")
        self.buttonEnter = Button(main, text = "Enter")

        self.display.grid(row = 0, columnspan = 2)
        self.buttonPlus.grid(row = 1, column = 0, sticky = "ew")
        self.buttonMinus.grid(row = 1, column = 1, sticky = "ew")
        self.buttonDivide.grid(row = 2, column = 0, sticky = "ew")
        self.buttonMultiply.grid(row = 2, column = 1, sticky = "ew")
        self.buttonEnter.grid(row = 3, columnspan = 2, sticky = "ew")

        self.buttonPlus.bind("<Button-1>", self.buttonPlusClick)
        self.buttonMinus.bind("<Button-1>", self.buttonMinusClick)
        self.buttonDivide.bind("<Button-1>", self.buttonDivideClick)
        self.buttonMultiply.bind("<Button-1>", self.buttonMultiplyClick)
        self.buttonEnter.bind("<Button-1>", self.buttonEnterClick)

    def resetButtonColors(self):
        self.buttonPlus.configure(bg = "White", fg = "Black")
        self.buttonMinus.configure(bg = "White", fg = "Black")
        self.buttonMultiply.configure(bg = "White", fg = "Black")
        self.buttonDivide.configure(bg = "White", fg = "Black")
        self.buttonEnter.configure(bg = "White", fg = "Black")

    def buttonPlusClick(self, event):
        self.resetButtonColors()
        self.buttonPlus.configure(bg = "Blue", fg = "White")
        self.operation = "+"
        self.store = float(self.display.get())
        self.display.delete(0, END)

    def buttonMinusClick(self, event):
        self.resetButtonColors()
        self.buttonMinus.configure(bg = "Blue", fg = "White")
        self.operation = "-"
        self.store = float(self.display.get())
        self.display.delete(0, END)

    def buttonMultiplyClick(self, event):
        self.resetButtonColors()
        self.buttonMultiply.configure(bg = "Blue", fg = "White")
        self.operation = "*"
        self.store = float(self.display.get())
        self.display.delete(0, END)

    def buttonDivideClick(self, event):
        #check for divide by 0 error
        self.store = float(self.display.get())
        self.resetButtonColors()
        self.buttonDivide.configure(bg = "Blue", fg = "White")
        self.operation = "/"
        self.display.delete(0, END)
            
    def buttonEnterClick(self, event):
        self.resetButtonColors()
        if self.operation == "+":
            result = self.store + float(self.display.get())
            self.display.delete(0, END)
            self.display.insert(0, str(result))
        if self.operation == "-":
            result = self.store - float(self.display.get())
            self.display.delete(0, END)
            self.display.insert(0, str(result))
        if self.operation == "/":
            #if float(self.display.get()) == 0:
                #m = Message(mainWindow, text = "Mathematical error")
                #m.pack()
            #else:
            result = self.store / float(self.display.get())
            self.display.delete(0, END)
            self.display.insert(0, str(result))
        if self.operation == "*":
            result = self.store * float(self.display.get())
            self.display.delete(0, END)
            self.display.insert(0, str(result))
        self.operation = ""
        
            
mainWindow = Tk()
Interface = GUI(mainWindow)
Interface.resetButtonColors()
mainWindow.mainloop()
