from tkinter import *

ws = Tk()
ws.title('leap year python')
ws.geometry('400x300')

def welMsg(name):
    year = int(name_Tf.get())
    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        print("{0} is a leap year".format(year))
        Label(ws, text=str(year) + ' is a leap year').pack(pady=50)

    # not divided by 100 means not a century
    # year divided by 4 is a leap year
    elif (year % 4 == 0) and (year % 100 != 0):
        print("{0} is a leap year".format(year))
        Label(ws, text=str(year) + ' is a leap year').pack(pady=50)

    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        print("{0} is not a leap year".format(year))
        Label(ws, text=str(year) + ' is not a leap year').pack(pady=50)

Label(ws, text='Enter Year & hit enter key').pack(pady=50)
name_Tf = Entry(ws)
name_Tf.bind('<Return>',welMsg)
name_Tf.pack()

ws.mainloop()
