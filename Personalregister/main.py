from tkinter import *
import functions

#window settings
root = Tk()
root.title("Personalregister")
root.config(bg='skyblue')

#################### Main Frame ####################

width = 800
height = 300
field_width = width/4
field_height = height/5*3.5


frame_upper = Frame(root, width=width, height=height, bg='white')
frame_upper.grid(row=0, column=0, padx=5, pady=5)

frame_lower = Frame(root, width=width, height=height, bg='grey')
frame_lower.grid(row=1, column=0, padx=5, pady=5)
 
#################### Input 1 ####################

frame_input_left = Frame(frame_upper, width=field_width, height=field_height, bg='red')
frame_input_left.grid(row=0, column=0, padx=5, pady=5)

Label(frame_input_left, text='Namn').grid(row=0, column=0, padx=10, pady=20)
name = Entry(frame_input_left).grid(row=0, column=1, padx=0, pady=20)

Label(frame_input_left, text='weight').grid(row=1, column=0, padx=10, pady=20)
weight = Entry(frame_input_left).grid(row=1, column=1, padx=0, pady=20)

Label(frame_input_left, text='size').grid(row=2, column=0, padx=10, pady=20)
size = Entry(frame_input_left).grid(row=2, column=1, padx=0, pady=20)


 
#Update popup screen
root.mainloop()