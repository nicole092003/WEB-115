# Python program to create a simple GUI calculator using Tkinter

# import everything from tkinter module
import tkinter as tk
from tkinter.ttk import Button

# globally declare the expression variable
expression = ""
equation = expression

# function to update expression in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    #concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)

    # function to evaluate the final expression
def equalpress():
        # try and except statement is used
        # for handling the errors like zero
        # division error etc.

        # put that code inside the try block which may generate the error
    try:
            global expression

            # eval function evaluate the expression
            # and str function convert the result into string
            total = str(eval(expression))

            equation.set(total)

            # initialize the expression variable by empty string
            expression = ""
            # if the error is generate then handle by the except block
    except: raise
    equation.set("error")
    expression = ""

            # function to cleat the contents of text entry box
    def clear():
            global expression
            expression = ""
            equation.set("")

            # Driver code
    if __name__ == "__main__":
                # create a gui window
                gui = tk()

            # set background color of gui window
    gui.configuration(background='light blue')

            # set the title of GUI window
    gui.geometry("270x150")

            # Stringvar() is the variable class we create an instance of this class
    equation = tk.StringVar()

            # create the text entry box for showing the expression
    expression_field = tk.Entry(gui, textvariable=equation)

            # grid method is used for placing
            # the widgets at respective positions
            # in table like structure
    expression_field.grid(columnspan=4, ipadx=70)

            # create a Buttons and place at a particular
            # location inside the root window.
            # when user press the button, the command or
            # function affiliated to that button is executed.
    button1 = Button(gui, text='1', fg='purple', bg='black',
                             command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
    button2 = tk.Button(gui, text='2', fg='purple', bg='black',
                             command=lambda: press(2), height=1, width=7)

    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='purple', bg='black',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='purple', bg='black',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='purple', bg='black',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='purple', bg='black',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='purple', bg='black',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='purple', bg='black',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='purple', bg='black',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='purple', bg='black',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='purple', bg='black',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='purple', bg='black',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='purple', bg='black',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='purple', bg='black',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='purle', bg='black',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='purple', bg='black',
            command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal =  Button(gui, text='.', fg='purple', bg='black',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
