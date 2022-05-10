from tkinter import *
from tkmacosx import Button
import tkinter.font as font

from Calculate import Check


def main():
    global equation
    equation = ""

    # Add number to the equation
    def click(number):
        global equation
        if equation == "":
            e.delete(0, END)
        equation = equation + str(number)
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))
        print(f"equation is {equation}")

    # Clear calculator screen
    def clear():
        e.delete(0, END)
        global equation
        equation = ""

    # Add a sign to the equation
    def button_sign(sign):
        global equation
        if equation == "":
            e.delete(0, END)
        equation = equation + str(sign)
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(sign))
        print(f"equation is {equation}")

    # Calculate given equation
    def send():
        global equation
        e.delete(0, END)
        output = Check(equation)
        equation = ""
        print(output)
        e.insert(0, output)

    # Creating the root
    root = Tk()
    root.title("My Calculator")
    root['background'] = "black"

    # Defining calculator size and placement
    app_width = 425
    app_height = 680
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    # Fonts
    myFont = font.Font(family='Helvetica', size=15, weight='bold')
    bigFont = font.Font(family='Helvetica', size=26, weight='bold')

    # Creating the entry box
    e = Entry(root, width=30, border=0, fg='white', bg='black', highlightcolor="black")
    e.grid(row=0, column=0, columnspan=40, ipady=30)
    e['font'] = bigFont

    # Number buttons
    button_1 = Button(root, text='1', padx=5, pady=40, command=lambda: click(1), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_2 = Button(root, text='2', padx=5, pady=40, command=lambda: click(2), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_3 = Button(root, text='3', padx=5, pady=40, command=lambda: click(3), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_4 = Button(root, text='4', padx=5, pady=40, command=lambda: click(4), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_5 = Button(root, text='5', padx=5, pady=40, command=lambda: click(5), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_6 = Button(root, text='6', padx=5, pady=40, command=lambda: click(6), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_7 = Button(root, text='7', padx=5, pady=40, command=lambda: click(7), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_8 = Button(root, text='8', padx=5, pady=40, command=lambda: click(8), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_9 = Button(root, text='9', padx=5, pady=40, command=lambda: click(9), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)
    button_0 = Button(root, text='0', padx=55, pady=40, command=lambda: click(0), fg='white', bg='#535150',
                      activebackground='#5C5B57', borderless=1)

    # Calculate buttons
    button_divide = Button(root, text='÷', padx=5, pady=40, command=lambda: button_sign('÷'), fg='white', bg='#cc7700',
                           activebackground='#e68600', borderless=1)
    button_multiply = Button(root, text='X', padx=5, pady=40, command=lambda: button_sign('x'), fg='white',
                             bg='#cc7700', activebackground='#e68600', borderless=1)
    button_minus = Button(root, text='-', padx=5, pady=40, command=lambda: button_sign('-'), fg='white', bg='#cc7700',
                          activebackground='#e68600', borderless=1)
    button_plus = Button(root, text='+', padx=5, pady=40, command=lambda: button_sign('+'), fg='white', bg='#cc7700',
                         activebackground='#e68600', borderless=1)
    button_open = Button(root, text='(', padx=5, pady=40, command=lambda: button_sign('('), fg='white', bg='#cc7700',
                         activebackground='#e68600', borderless=1)
    button_close = Button(root, text=')', padx=5, pady=40, command=lambda: button_sign(')'), fg='white', bg='#cc7700',
                          activebackground='#e68600', borderless=1)
    button_point = Button(root, text='.', padx=5, pady=40, command=lambda: button_sign('.'), fg='white', bg='#7D7D7D',
                          activebackground='#AAAAAA', borderless=1)
    button_reset = Button(root, text='AC', padx=5, pady=40, command=lambda: clear(), fg='white', bg='#7D7D7D',
                          activebackground='#AAAAAA', borderless=1)
    button_equals = Button(root, text='=', padx=5, pady=40, command=lambda: send(), fg='white', bg='#cc7700',
                           activebackground='#e68600', borderless=1)

    # Applying fonts
    button_1['font'] = myFont
    button_2['font'] = myFont
    button_3['font'] = myFont
    button_4['font'] = myFont
    button_5['font'] = myFont
    button_6['font'] = myFont
    button_7['font'] = myFont
    button_8['font'] = myFont
    button_9['font'] = myFont
    button_0['font'] = myFont
    button_divide['font'] = myFont
    button_multiply['font'] = myFont
    button_minus['font'] = myFont
    button_plus['font'] = myFont
    button_equals['font'] = myFont
    button_open['font'] = myFont
    button_close['font'] = myFont
    button_reset['font'] = myFont
    button_point['font'] = myFont

    # 1st row positioning
    button_reset.grid(row=1, column=0)
    button_open.grid(row=1, column=1)
    button_close.grid(row=1, column=2)
    button_divide.grid(row=1, column=3)

    # 2nd row positioning
    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)
    button_multiply.grid(row=2, column=3)

    # 3rd row positioning
    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    button_minus.grid(row=3, column=3)

    # 4th row positioning
    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)
    button_plus.grid(row=4, column=3)

    # 5th row positioning
    button_0.grid(row=5, column=0, columnspan=2)
    button_point.grid(row=5, column=2)
    button_equals.grid(row=5, column=3)

    # Run
    root.mainloop()


if __name__ == '__main__':
    main()
