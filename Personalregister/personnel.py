from tkinter import *
from ui import *
from typing import Union
from collections import OrderedDict
import json


class Staff:

    def __init__(self, staff_type: str, entries: list, fields: list):
        self.staff_type = staff_type
        self.entries = entries
        self.fields = fields
        self.attributes = OrderedDict()
        self.root = None
        self.frame = None
        self.warn_label = None

    def create_fields(self, entries: list) -> list:
        fields = list()
        # create a new InputField for every entry
        for input in entries:
            fields.append(InputField(input[0], input[1].__name__))
        return fields

    def display(self, root: Frame, row: int, column: int,
                padx: Union[int, tuple] = 0,
                pady: Union[int, tuple] = 0):
        """
        Display the frame and its fields on the root window.

        Parameters:
        root: The parent widget of the frame.
        row: The row index of the grid where the frame is placed.
        column: The column index of the grid where the frame is placed.
        padding: Padding of the object on x and y, for specific pading make a tuple: (x up, x down), (y left, y right)
        """
        self.root = root

        # create new frame
        self.frame = LabelFrame(root, text=self.staff_type)
        self.frame.grid(row=row, column=column, padx=padx, pady=pady)

        # display every field
        for index, field in enumerate(self.fields):
            field.display(self.frame, index)

        # create button to register staff member
        button = Button(self.frame, text="Registrera",
                        command=lambda: [self.store_data(), update_display()])
        button.grid(row=len(self.fields)+2, column=0, columnspan=2, pady=5)

    def store_data(self):
        # validate the data type
        for i, field in enumerate(self.fields):
            input_val = field.get_v()

            # try to convert to other (correct) data type
            try:
                input_val = float(input_val)
                if input_val % 1 == 0:
                    input_val = int(input_val)
            except ValueError:
                pass

            # compare to entry list
            if type(input_val) == self.entries[i][1]:
                self.attributes[field.text] = input_val
            # if data does not match, create warning label
            else:
                if self.warn_label is None:
                    self.warn_label = Label(
                        self.frame, text="wrong data type")
                    self.warn_label.grid(
                        row=len(self.fields)+1, column=0, columnspan=2)
                return

        # remove warning label if data valid
        if self.warn_label is not None:
            self.warn_label.destroy()
            self.warn_label = None

        # create attributes and assign corresponding values
        self.attributes['Typ'] = self.staff_type
        self.attributes['Lön'] = self.calculate_salary()
        self.attributes.move_to_end('Lön')

        # read and dump data to json file
        with open('Personalregister/database.json', 'r+') as file:
            # check if file is empty
            try:
                staff = json.load(file)
            except json.JSONDecodeError:
                staff = list()
                print("error loading file")

            staff.append(self.attributes)

            # write data to json file
            file.seek(0)
            json.dump(staff, file, indent=3)

    def calculate_salary(self) -> float:
        # make this function exclusive to children of this class
        raise NotImplementedError


class Salesman(Staff):

    def __init__(self):
        self.staff_type = 'Säljare'
        self.entries = [['Namn', str], [
            'Provision', float], ['Försäljning', int]]
        self.fields = self.create_fields(self.entries)
        super().__init__(self.staff_type, self.entries, self.fields)

    def calculate_salary(self) -> float:
        provision = self.attributes['Provision']
        sales = self.attributes['Försäljning']
        salary = round(sales * provision, 2)
        return salary


class Consultant(Staff):

    def __init__(self):
        self.staff_type = 'Konsult'
        self.entries = [['Namn', str], ['Timlön', int], ['Timmar', int]]
        self.fields = self.create_fields(self.entries)
        super().__init__(self.staff_type, self.entries, self.fields)

    def calculate_salary(self) -> float:
        pay = self.attributes['Timlön']
        hours = self.attributes['Timmar']
        salary = round(pay * hours, 2)
        return salary


class Clerk(Staff):

    def __init__(self):
        self.staff_type = 'Kontorist'
        self.entries = [['Namn', str], ['Lön', int]]
        self.fields = self.create_fields(self.entries)
        super().__init__(self.staff_type, self.entries, self.fields)

    def calculate_salary(self) -> float:
        salary = self.attributes['Lön']
        return salary


class Window():

    def __init__(self, window_type: str, keys: list):
        self.window_type = window_type
        self.keys = keys
        self.items = list()
        self.list_variable = None
        self.lb = None

    def load_data(self) -> list:
        # read json file
        with open('Personalregister/database.json', 'r', encoding='utf-8') as file:
            # check if file is empty
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = list()

        return data

    def insert_items(self, list_variable: StringVar):
        # append selected keys to listvariable
        items = list()
        for item in self.items:
            temp = list()
            for key in item:
                if key in self.keys:
                    temp.append(item[key])
            items.append(temp)

        list_variable.set(items)

    def display(self, root: Frame, row: int, column: int,
                padx: Union[int, tuple] = 0,
                pady: Union[int, tuple] = 0,
                height: int = 10,
                width: int = 30):
        """
        Display the frame and its fields on the root window.

        Parameters:
        root: The parent widget of the frame.
        row: The row index of the grid where the frame is placed.
        column: The column index of the grid where the frame is placed.
        padding: Padding of the object on x and y, for specific pading make a tuple: (x up, x down), (y left, y right)
        height: Items to display
        widht: px
        """
        self.root = root
        self.items = self.load_data()

        # create new frame
        frame = Frame(root)
        frame.grid(row=row, column=column, padx=padx, pady=pady)

        # create new label
        label = Label(frame, text=f"{self.window_type}")
        label.grid(row=0, column=0)

        # CAUTION create the StringVar after creating the root window!!!!
        self.list_variable = StringVar()
        self.insert_items(self.list_variable)

        # create a scrollbar widget
        scrollbar = Scrollbar(frame)
        scrollbar.grid(row=1, column=1, sticky=N+S)

        # create listbox
        self.lb = Listbox(
            frame, listvariable=self.list_variable, height=height, width=width)
        self.lb.grid(row=1, column=0)

        # attach scrollbar to listbox
        self.lb.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.lb.yview)

    def update_listbox(self):
        self.items = self.load_data()
        self.insert_items(self.list_variable)
        self.lb.update()
        print("Listbox updated!")


class TotalSalary:

    def __init__(self):
        self.total_salary = 0
        self.output = None

    def load_data(self) -> list:
        # read json file
        with open('Personalregister/database.json', 'r', encoding='utf-8') as file:
            # check if file is empty
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

        return data

    def calculate_payroll(self):
        data = self.load_data()
        self.total_salary = f"{round(sum(person['Lön'] for person in data), 2)} SEK"

    def display(self, root: Frame, row: int, column: int,
                padx: Union[int, tuple] = 0,
                pady: Union[int, tuple] = 0):
        """
        Display the frame and its fields on the root window.

        Parameters:
        root: The parent widget of the frame.
        row: The row index of the grid where the frame is placed.
        column: The column index of the grid where the frame is placed.
        padding: Padding of the object on x and y, for specific pading make a tuple: (x up, x down), (y left, y right)
        """
        # create new frame
        frame = Frame(root)
        frame.grid(row=row, column=column, padx=padx, pady=pady)

        # create title label
        Label(frame, text="Total Lönekostnad").grid(row=0, column=0)

        # create new entry
        self.output = Entry(frame, state='disabled',
                            disabledforeground='black')
        self.output.grid(row=1, column=0)

        # create update button
        Button(frame, text="Beräkna total lönekostnad",
               command=self.update_total).grid(row=2, column=0)

    def update_total(self):
        self.calculate_payroll()
        self.output.config(state='normal')
        self.output.delete(0, 'end')
        self.output.insert(0, f"{self.total_salary}")
        self.output.config(state='disabled')


#################### MAIN ####################

# create root window
root = Tk()
root.title('Personalregister')

# create frame for content
window = Frame(root)
window.pack()


def resize_root():
    # resize root window based on the content size
    root.update()
    root.geometry('{}x{}'.format(
        window.winfo_width(), window.winfo_height()))


# call resize_root after mainloop starts
root.after(0, resize_root)

# create staff objects
salesman = Salesman()
consultant = Consultant()
clerk = Clerk()

# create personnel window
registry = Window('register', ['Namn', 'Typ'])
salaries = Window('löneutbetalningar', ['Namn', 'Typ', 'Lön'])
total = TotalSalary()

# display staff objects
salesman.display(window, 0, 0)
consultant.display(window, 0, 1)
clerk.display(window, 0, 2)

# display personnel
registry.display(window, 1, 0, 0, (30, 0))
salaries.display(window, 1, 1, 0, (30, 0))
total.display(window, 1, 2)


def update_display():
    print("Update initialized")
    registry.update_listbox()
    salaries.update_listbox()


window.mainloop()
