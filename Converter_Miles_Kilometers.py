# CONVERTER Miles to kilometers and vice versa

from pickletools import int4
import re
from telnetlib import SE
import tkinter as tk
from turtle import bgcolor, clear, color

unitOptions =[
    "- - -",
    "Miles",
    "Kilometers"
]

def miles_kilometers():
    
    miles = 1
    kilometers = 1

    if var1.get() == unitOptions[2]:
        miles = (float)(inputValue.get()) * 0.621371
        result = tk.Label(window, text=round(miles, 4), fg="black", font=('Helvetica', 20), width=10)
        result.grid(row=0, column=2)
        var2.set(unitOptions[1])
        

    if var1.get() == unitOptions[1]:
        kilometers = (float)(inputValue.get()) / 0.621371
        result = tk.Label(window, text=round(kilometers, 4), fg="black", font=('Helvetica', 20), width=10)
        result.grid(row=0, column=2)
        var2.set(unitOptions[2])



#Master Widget
window = tk.Tk()
window.geometry("800x400")
window.title("Unit Converter")
window.config(background="silver")
window.resizable(False, False) #non permette di cambiare le dimensioni della finestra 


#Selected Unit
var1 = tk.StringVar(window)
var1.set(unitOptions[0])
var2 = tk.StringVar(window)
var2.set(unitOptions[0])

#First Menu'
my_menu = tk.OptionMenu(window, var1, *unitOptions)
my_menu.config(width=20,height=2, font=('Helvetica', 12))
my_menu.grid(row=1, column=0, padx=50)

#Second Menu'
my_menu2 = tk.OptionMenu(window, var2, *unitOptions)
my_menu2.config(width=20, height=2, font=('Helvetica', 12))
my_menu2.grid(row=1, column=2, padx=50)

#Convert button
button_converter = tk.Button(text="Converter", command=miles_kilometers)
button_converter.config(width=15, height=1, font=('Helvetica', 10))
button_converter.grid(column=1, row=0, padx=10, pady=100)

#Input Value
inputValue = tk.Entry(window, justify=tk.CENTER)
inputValue.grid(column=0, row=0)
inputValue.config(width=10, font=('Helvetica', 20))

#Credits
me = tk.Label(text="by Lorenzo Bernardini")
me.config(width=20, font=('Helvetica', 10), background="silver")
me.grid(row=3, column=2, sticky="SE", pady=100, padx=2)

if __name__ == "__main__":
    window.mainloop()