from tkinter import *


class InputField:

    def __init__(self, text: str, placeholder: str):
        self.text = text
        self.placeholder = placeholder
        self.entry = None
        self.placeholder_shown = True
        self.frame = None

    def on_entry_focus_in(self, event: Event = None):
        if self.placeholder_shown:
            self.entry.delete(0, END)
            self.entry.config(foreground='black')
            self.placeholder_shown = False

    def on_entry_focus_out(self, event: Event = None):
        if self.entry.get() == '':  # empty
            self.entry.insert(0, self.placeholder)
            self.entry.config(foreground='grey')
            self.placeholder_shown = True

    def get_v(self):
        entry_value = self.entry.get()
        # clear entries
        self.entry.delete(0, END)
        self.frame.focus_set()
        self.on_entry_focus_out()
        # return entry value
        return entry_value

    def display(self, frame: Frame, row: int):
        self.frame = frame

        # create entry label
        label = Label(frame, text=self.text)
        label.grid(row=row, column=0, sticky=W)

        # create new entry
        entry = Entry(frame, foreground='grey')
        entry.insert(0, self.placeholder)

        # bnd focus events to handle placeholder behavior
        entry.bind('<FocusIn>', self.on_entry_focus_in)
        entry.bind('<FocusOut>', self.on_entry_focus_out)

        entry.grid(row=row, column=1, padx=(10, 5), pady=(0, 5))
        self.entry = entry
