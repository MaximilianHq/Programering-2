from tkinter import *
import json


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


# a class for creating staff objects of different types
class Staff:
    def __init__(self, type: str, fields: list):
        self.type = type
        self.attributes = {
            'type': type
        }
        self.fields = list()
        for field in fields:
            self.fields.append(Input_Field(field))

    # displaying the staff object in a labeled frame with a button to register it
    def display(self, root, row, column):
        frame = LabelFrame(root, text=self.type)
        frame.grid(row=row, column=column, padx=0, pady=0)

        for index, field in enumerate(self.fields):
            field.display(frame, index)

        button = Button(frame, text="Registrera", command=self.get_values)
        button.grid(row=len(self.fields)+1, column=0,
                    padx=0, pady=(15, 10), columnspan=2)

    # getting the values of the input fields and appending them to a json file
    def get_values(self):
        for field in self.fields:
            self.attributes[field.text] = field.get_v()

        with open('database.json', 'a+', encoding='utf-8') as file:

            try:
                staff = json.load(file)
            except json.JSONDecodeError:
                staff = list()

            staff.append(self.attributes)

            json.dump(staff, file, indent=3)
            file.truncate()


class Salesman:

    def __init__(self):
        pass


class Consultant:

    def __init__(self):
        pass


class Clerk:

    def __init__(self):
        pass


# creating three staff objects of different types
salesman = Staff('salesman', ['Namn', 'Provision', 'Försäljning'])
consultant = Staff('consultant', ['Namn', 'Timlön', 'Arbetad tid'])
clerk = Staff('clerk', ['Namn', 'Månadslön'])

# creating a window for the gui
window = Tk()
window.title('Staffregister')
window.geometry('400x300')
window.maxsize(800, 400)

# displaying the staff objects in the window
salesman.display(window, 0, 0)
consultant.display(window, 0, 1)
clerk.display(window, 0, 2)

# starting the main loop of the window
window.mainloop()