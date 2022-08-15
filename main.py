import tkinter as tk # gui
from tkinter import *  # all commands from tkinter

ws = tk.Tk()  # create canvas
ws.title('leap year python')  # title

canvas1 = tk.Canvas(ws, width=400, height=300) # canvas height and width
canvas1.pack() # create canvas

name_Tf = tk.Entry(ws)  # create entry
name_Tf.bind('<Return>', (lambda event: leap_year()))  # function is called when enter is pressed
canvas1.create_window(200, 140, window=name_Tf) # show entry in canvas

instructions = tk.Label(ws, text='Enter Number & hit enter key')  # instructions for user
canvas1.create_window(200, 110, window=instructions) # show instructions in canvas


ws.btn = tk.Button(ws, text='Enter', bd='5', command=(lambda: leap_year())) # button that runs leap_year
canvas1.create_window(200, 180, window=ws.btn) # show button

def create_canvas(): # define function
    canvas1.delete("all") # delete everything in canvas
    # recreate everything EXCEPT entry
    instructions = tk.Label(ws, text='Enter Number & hit enter key')  # instructions for user
    canvas1.create_window(200, 110, window=instructions) 
    ws.btn = tk.Button(ws, text='Enter', bd='5', command=(lambda: leap_year()))
    canvas1.create_window(200, 180, window=ws.btn)
    canvas1.create_window(200, 140, window=name_Tf)

def create_entry(): # define function
    name_Tf = tk.Entry(ws)  # create entry
    name_Tf.bind('<Return>', (lambda event: leap_year()))  # function is called when enter is pressed

def clear_text(): # define function
   name_Tf.delete(0, END) # deletes entry from first symbol to end

def leap_year(): # define function
    create_canvas() # calls function
    year = int(name_Tf.get()) # tturn entry value into int

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0): # fits criteria for leap year
        result = tk.Label(ws, text=str(year) + ' is a leap year') # result label

    # not divided by 100 means not a century
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0): # fits other criteria for leap year
        result = tk.Label(ws, text=str(year) + ' is a leap year') # result label

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else: # does not fit criteria for leap year at all
        result = tk.Label(ws, text=str(year) + ' is not a leap year') # result label
    canvas1.create_window(200, 210, window=result) # show result label in canvas
    create_entry() # creates new entry
    clear_text() # clears entry text


ws.mainloop()  # show window
