from tkinter import *

# a class for creating input fields in the gui
class Input_Field:
    def __init__(self, text):
        self.text = text
        self.entry = None

    # getting the value of the entry widget
    def get_v(self):
        return self.entry.get()

    # displaying the label and entry widgets in a given frame and row
    def display(self, frame, row):
        label = Label(frame, text=self.text)
        label.grid(row=row, column=0, padx=0, pady=0, sticky=W)

        entry = Entry(frame)
        entry.grid(row=row, column=1, padx=(10, 5), pady=(0, 5))
        self.entry = entry


class ListBox: 
    def __init__(self, text):
        self.text = text
        
    #displays values of every dict inside a list 
    #(by adding every eployees salary in each dictionary,
    # this code can be reused)
    
    def display(self, frame, row):
        label = Label(frame, text=0) #TODO change text to *var, sep=':'
        label.grid(row=row, column=0, padx=0, pady=0)