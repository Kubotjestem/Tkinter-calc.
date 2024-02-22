from tkinter import *

root = Tk()
root.geometry('215x400')
root.title("Calculator")
root.resizable(False, False)

def on_enter(e):
    e.widget.config(bg="gray")

def on_leave(e):
    e.widget.after(100, lambda: e.widget.config(bg="SystemButtonFace"))

button_frame = Frame(root)
button_frame.pack(side=BOTTOM)

expression = StringVar()
expression.set("")

def press(num):
    global expression
    expression.set(expression.get() + str(num))

def equalpress():
    try:
        global expression
        total = str(eval(expression.get()))
        expression.set(total)
    except:
        expression.set("Error")

def clear():
    global expression
    expression.set("")


btn_clear = Button(button_frame, text='C', bd='5', width=5, height=3, command=clear)
btn_plus = Button(button_frame, text='+', bd='5', width=5, height=3, command=lambda: press('+'))
btn_minus = Button(button_frame, text='-', bd='5', width=5, height=3, command=lambda: press('-'))
btn_multiply = Button(button_frame, text='*', bd='5', width=5, height=3, command=lambda: press('*'))
btn_divide = Button(button_frame, text='/', bd='5', width=5, height=3, command=lambda: press('/'))
btn_equal = Button(button_frame, text='=', bd='5', width=5, height=3, command=equalpress)
btn_dot = Button(button_frame, text='.', bd='5', width=5, height=3, command=lambda: press('.'))
btn0 = Button(button_frame, text='0', bd='5', width=5, height=3, command=lambda: press(0))
btn1 = Button(button_frame, text='1', bd='5', width=5, height=3, command=lambda: press(1))
btn2 = Button(button_frame, text='2', bd='5', width=5, height=3, command=lambda: press(2))
btn3 = Button(button_frame, text='3', bd='5', width=5, height=3, command=lambda: press(3))
btn4 = Button(button_frame, text='4', bd='5', width=5, height=3, command=lambda: press(4))
btn5 = Button(button_frame, text='5', bd='5', width=5, height=3, command=lambda: press(5))
btn6 = Button(button_frame, text='6', bd='5', width=5, height=3, command=lambda: press(6))
btn7 = Button(button_frame, text='7', bd='5', width=5, height=3, command=lambda: press(7))
btn8 = Button(button_frame, text='8', bd='5', width=5, height=3, command=lambda: press(8))
btn9 = Button(button_frame, text='9', bd='5', width=5, height=3, command=lambda: press(9))
btnNull = Button(button_frame, text='', bd='5', width=5, height=3,)
btnNull2 = Button(button_frame, text='', bd='5', width=5, height=3,)
btnNull3 = Button(button_frame, text='', bd='5', width=5, height=3,)

btn_clear.grid(row=0, column=0, padx=1, pady=1)
btn_divide.grid(row=0, column=1, padx=1, pady=1)
btn_multiply.grid(row=0, column=2, padx=1, pady=1)
btn_minus.grid(row=0, column=3, padx=1, pady=1)
btn7.grid(row=1, column=0, padx=1, pady=1)
btn8.grid(row=1, column=1, padx=1, pady=1)
btn9.grid(row=1, column=2, padx=1, pady=1)
btn_plus.grid(row=1, column=3, padx=1, pady=1)
btn4.grid(row=2, column=0, padx=1, pady=1)
btn5.grid(row=2, column=1, padx=1, pady=1)
btn6.grid(row=2, column=2, padx=1, pady=1)
btn_equal.grid(row=2, column=3, padx=1, pady=1)
btn1.grid(row=3, column=0, padx=1, pady=1)
btn2.grid(row=3, column=1, padx=1, pady=1)
btn3.grid(row=3, column=2, padx=1, pady=1)
btn0.grid(row=3, column=3, padx=1, pady=1)
btn_dot.grid(row=4, column=0, padx=1, pady=1)
btnNull.grid(row=4, column=1, padx=1, pady=1)
btnNull2.grid(row=4, column=2, padx=1, pady=1)
btnNull3.grid(row=4, column=3, padx=1, pady=1)



for btn in (btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn0, btn_plus, btn_minus, btn_multiply,
            btn_divide, btn_equal, btn_clear, btn_dot, btnNull2, btnNull3, btnNull):
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)



entry = Entry(root, textvariable=expression, font=('arial', 20, 'bold'), bd=20, insertwidth=4, width=10, justify='right')
entry.pack(side=TOP, pady=10)

root.mainloop()
