from tkinter import *
import time

clock = Tk()
clock.title("Digital Clock")
clock.geometry("440x150")
clock.resizable(0, 0)

text_font= ("Boulder", 50, 'bold')
foreground= "#2e2d2e"
border_width = 25

l = Label(clock, font=text_font, fg=foreground, bd=border_width)
l.grid(row=0, column=0)

def digital_clock():
   current_time = time.strftime("%I:%M:%S %p")
   l.config(text=current_time)
   l.after(200, digital_clock)

digital_clock()
clock.mainloop()