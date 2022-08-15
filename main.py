import tkinter as tk
from tkinter import *  # all commands from tkinter

ws = tk.Tk()  # create canvas
ws.title('leap year python')  # title

canvas1 = tk.Canvas(ws, width=400, height=300)
canvas1.pack()

name_Tf = tk.Entry(ws)  # create entry
name_Tf.bind('<Return>', (lambda event: leap_year()))  # function is called when enter is pressed
canvas1.create_window(200, 140, window=name_Tf)

instructions = tk.Label(ws, text='Enter Number & hit enter key')  # instructions for user
canvas1.create_window(200, 110, window=instructions)


ws.btn = tk.Button(ws, text='Enter', bd='5', command=(lambda: leap_year()))
canvas1.create_window(200, 180, window=ws.btn)

def create_canvas():
    canvas1.delete("all")
    instructions = tk.Label(ws, text='Enter Number & hit enter key')  # instructions for user
    canvas1.create_window(200, 110, window=instructions)
    ws.btn = tk.Button(ws, text='Enter', bd='5', command=(lambda: leap_year()))
    canvas1.create_window(200, 180, window=ws.btn)
    canvas1.create_window(200, 140, window=name_Tf)

def create_entry():
    name_Tf = tk.Entry(ws)  # create entry
    name_Tf.bind('<Return>', (lambda event: leap_year()))  # function is called when enter is pressed

def clear_text():
   name_Tf.delete(0, END)

def leap_year():
    create_canvas()
    year = int(name_Tf.get())

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))
        result = tk.Label(ws, text=str(year) + ' is a leap year')

    # not divided by 100 means not a century
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))
        result = tk.Label(ws, text=str(year) + ' is a leap year')

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print("{0} is not a leap year".format(year))
        result = tk.Label(ws, text=str(year) + ' is not a leap year')
    canvas1.create_window(200, 210, window=result)
    create_entry()
    clear_text()


ws.mainloop()  # show window
