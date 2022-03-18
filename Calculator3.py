from tkinter import *
import tkinter.messagebox

# ---------------------- Basic Settings -----------------------
root = Tk()
root.title('Calculator')
root.geometry('400x220')
root.resizable(width=False, height=False)
color = 'white'
number1 = IntVar(value='')
number2 = IntVar(value='')
result = IntVar()
numbers = IntVar(value='')


# ---------------------- Functions -----------------------
def num(entry):
    inputs.insert(END, entry)


def seperator(num):
    amount = []
    if num < 1000:
        amount.insert(0, str(num))
    else:
        while num > 0:
            result = num % 1000
            num //= 1000
            amount.insert(0, str(result).zfill(3))
            if num < 100 and num != 0:
                result = num % 1000
                amount.insert(0, str(result))
                break

    return ','.join(amount)


def clear():
    numbers.set('')


def calculate():
    try:
        result.set(seperator(round(eval(inputs.get()), 3)))
    except ZeroDivisionError:
        tkinter.messagebox.showerror('Zero Error', 'you can divide on zero!')
    except NameError:
        tkinter.messagebox.showerror('Value Error', 'you must use just numbers!')
    except SyntaxError:
        tkinter.messagebox.showerror('Syntax Error', 'The format you have Enter is not Correct!')


# ---------------------- Frames -----------------------
resultFrames = Frame(root, width=400, height=20, bg='gray')
resultFrames.pack(side=TOP)
operatorsFrames = Frame(root, width=400, height=400, bg='white')
operatorsFrames.pack(side=TOP)

# ---------------------- Inputs -----------------------
topLabel = Label(resultFrames, text='You Can Calculate easily')
topLabel.pack(side=TOP, pady=5)

inputs = Entry(resultFrames, textvariable=numbers, width=40)
inputs.pack(side=LEFT, padx=5, pady=5)

btn1 = Button(operatorsFrames, text='1', command=lambda: num(1), width=10)
btn1.grid(row=1, column=1, padx=5, pady=5)
btn2 = Button(operatorsFrames, text='2', command=lambda: num(2), width=10)
btn2.grid(row=1, column=2, padx=5, pady=5)
btn3 = Button(operatorsFrames, text='3', command=lambda: num(3), width=10)
btn3.grid(row=1, column=3, padx=5, pady=5)
btnPlus = Button(operatorsFrames, text='plus (+)', command=lambda: num('+'), width=15)
btnPlus.grid(row=1, column=4, padx=5, pady=5)

btn4 = Button(operatorsFrames, text='4', command=lambda: num(4), width=10)
btn4.grid(row=2, column=1, padx=5, pady=5)
btn5 = Button(operatorsFrames, text='5', command=lambda: num(5), width=10)
btn5.grid(row=2, column=2, padx=5, pady=5)
btn6 = Button(operatorsFrames, text='6', command=lambda: num(6), width=10)
btn6.grid(row=2, column=3, padx=5, pady=5)
btnMinus = Button(operatorsFrames, text='minus (-)', command=lambda: num('-'), width=15)
btnMinus.grid(row=2, column=4, padx=5, pady=5)

btn7 = Button(operatorsFrames, text='7', command=lambda: num(7), width=10)
btn7.grid(row=3, column=1, padx=5, pady=5)
btn8 = Button(operatorsFrames, text='8', command=lambda: num(8), width=10)
btn8.grid(row=3, column=2, padx=5, pady=5)
btn9 = Button(operatorsFrames, text='9', command=lambda: num(9), width=10)
btn9.grid(row=3, column=3, padx=5, pady=5)
btnMultiple = Button(operatorsFrames, text='multiple (x)', command=lambda: num('*'), width=15)
btnMultiple.grid(row=3, column=4, padx=5, pady=5)

btn_ = Button(operatorsFrames, text='CE', width=10, command=lambda: clear())
btn_.grid(row=4, column=1, padx=5, pady=5)
btn0 = Button(operatorsFrames, text='0', command=lambda: num(0), width=10)
btn0.grid(row=4, column=2, padx=5, pady=5)
btnDot = Button(operatorsFrames, text='.', command=lambda: num('.'), width=10)
btnDot.grid(row=4, column=3, padx=5, pady=5)
btnDivide = Button(operatorsFrames, text='divide (/)', command=lambda: num('/'), width=15)
btnDivide.grid(row=4, column=4, padx=5, pady=5)

finalResult = Label(resultFrames, textvariable=result)
finalResult.pack(side=RIGHT, padx=5, pady=5)
btnResult = Button(resultFrames, text='=', command=calculate)
btnResult.pack(side=RIGHT, padx=5)

root.configure(bg='grey')
root.mainloop()
