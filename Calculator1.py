from tkinter import *
import tkinter.messagebox

# ---------------------- Basic Settings -----------------------
root = Tk()
root.title('Calculator')
root.geometry('400x200')
root.resizable(width=False, height=False)
color = 'white'
result = IntVar()
number1 = IntVar()
number2 = IntVar()


# ---------------------- Functions -----------------------
def errormsg(msg):
    if msg == 'error':
        tkinter.messagebox.showerror('Value Error', 'you must use just numbers!')
    elif msg == 'zeroError':
        tkinter.messagebox.showerror('Zero Error', 'you can divide on zero!')


def plus():
    try:
        result.set(number1.get() + number2.get())
    except:
        errormsg('error')


def minus():
    try:
        result.set(number1.get() - number2.get())
    except:
        errormsg('error')


def multiple():
    try:
        result.set(number1.get() * number2.get())
    except:
        errormsg('error')


def power():
    try:
        result.set(number1.get() ** number2.get())
    except:
        errormsg('error')


def divide():
    try:
        if float(number1.get()) and number2.get() != 0:
            result.set(number1.get() / number2.get())
        elif number2.get() == 0:
            errormsg('zeroError')
    except:
        errormsg('error')


# ---------------------- Frames -----------------------
firstFrame = Frame(root, width=400, height=50)
firstFrame.pack(side=TOP)
secondFrame = Frame(root, width=400, height=50)
secondFrame.pack(side=TOP)
thirdFrame = Frame(root, width=400, height=50)
thirdFrame.pack(side=TOP)
fourthFrame = Frame(root, width=400, height=50)
fourthFrame.pack(side=TOP)

# ---------------------- Inputs -----------------------
topLabel = Label(firstFrame, text='You Can Calculate easily')
topLabel.pack(side=TOP, pady=5)

num1 = Label(firstFrame, text='Number 1 : ')
num1.pack(side=LEFT)
num2 = Label(secondFrame, text='Number 2 : ')
num2.pack(side=LEFT)

input1 = Entry(firstFrame, textvariable=number1)
input1.pack(side=LEFT, padx=5, pady=5)
input2 = Entry(secondFrame, textvariable=number2)
input2.pack(side=LEFT, padx=5, pady=5)

btnPlus = Button(thirdFrame, text='plus (+)', command=lambda: plus())
btnPlus.pack(side=LEFT, padx=5, pady=5)

btnMinus = Button(thirdFrame, text='minus (-)', command=lambda: minus())
btnMinus.pack(side=LEFT, padx=5, pady=5)

btnMultiple = Button(thirdFrame, text='multiple (x)', command=lambda: multiple())
btnMultiple.pack(side=LEFT, padx=5, pady=5)

btnDivide = Button(thirdFrame, text='divide (/)', command=lambda: divide())
btnDivide.pack(side=LEFT, padx=5, pady=5)

btnPower = Button(thirdFrame, text='Power (^n)', command=lambda: power())
btnPower.pack(side=LEFT, padx=5, pady=5)

resultLabel = Label(fourthFrame, text='The Answer is : ')
resultLabel.pack(side=LEFT)
finalResult = Label(fourthFrame, textvariable=result)
finalResult.pack(side=LEFT)

root.mainloop()
