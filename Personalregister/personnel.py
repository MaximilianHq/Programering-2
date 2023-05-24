from tkinter import*
from ui import*
import json

# a class for creating staff objects of different types
class Staff:
    def __init__(self):
        self.type = ''
        self.entries = [['Namn', str]]
        self.fields = list()
        self.attributes = dict()
        self.root = None
        self.frame = None
        self.warn_label = None
        
    #create entries
    def make_entries(self):
        for input in self.entries:
            self.fields.append(InputField(input[0]))

    # displaying the staff object in a labeled frame with a button to register it
    def display(self, root, row, column):
        self.root = root
        
        self.frame = LabelFrame(root, text=self.type)
        self.frame.grid(row=row, column=column, padx=0, pady=0)

        for index, field in enumerate(self.fields):
            field.display(self.frame, index)

        button = Button(self.frame, text="Registrera", command=lambda : [self.store_data(), update_display()])
        button.grid(row=len(self.fields)+2, column=0,
                    padx=0, pady=(15, 10), columnspan=2)
               

    # getting the values of the input fields and appending them to a json file
    def store_data(self):
        #validate data
        for i, field in enumerate(self.fields):
            val = field.get_v()
            
            #try to convert to other data type
            try:
                val = float(val)
                if val % 1 == 0:
                    val = int(val)
            except ValueError:
                pass
            
            #validate data type
            if type(val) == self.entries[i][1]:
                self.attributes[field.text] = val
            else:
                if self.warn_label is None:  # Create the warning label only if it doesn't exist
                    self.warn_label = Label(self.frame, text='wrong data type')
                    self.warn_label.grid(row=len(self.fields)+1, column=0, columnspan=2)  # Adjust the column span as needed
                return
        else:
            # Remove the warning label if it exists
            if self.warn_label is not None:
                self.warn_label.destroy()
                self.warn_label = None
            
        self.attributes['Typ'] = self.type

        self.attributes['Lön'] = self.calculate_salary()

        with open('Personalregister/database.json', 'r+') as file:

            try:
                staff = json.load(file)
            except json.JSONDecodeError:
                staff = list()
                print("error loading file")

            staff.append(self.attributes)

            file.seek(0)
            json.dump(staff, file, indent=3)


class Salesman(Staff):

    def __init__(self):
        super().__init__()
        self.type = 'Säljare'
        self.entries.extend([['Provision', float], ['Försäljning', int]])
        self.make_entries()

    def calculate_salary(self) -> float:
        provision = self.attributes['Provision']
        sales = self.attributes['Försäljning']
        salary = round(sales * provision, 2)
        return salary


class Consultant(Staff):

    def __init__(self):
        super().__init__()
        self.type = 'Konsult'
        self.entries.extend([['Pay', int], ['Hours', int]])
        self.make_entries()
        
    def calculate_salary(self) -> float:
        pay = self.attributes['Timlön']
        hours = self.attributes['Timmar']
        salary = round(pay * hours, 2)
        return salary


class Clerk(Staff):

    def __init__(self):
        super().__init__()
        self.type = 'Kontorist'
        self.entries.extend([['Lön', int]])
        self.make_entries()
        
    def calculate_salary(self) -> float:
        salary = self.attributes['Lön']
        return salary
    
    
class Window():
    def __init__(self, type:str, keys:list):
        self.type = type
        self.keys = keys
        self.items = self.load_items()
        self.list_variable = None  # Initialize the StringVar as None
        self.lb = None

    def load_items(self) -> list:
        with open('Personalregister/database.json', 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = list()

        return data

    def insert_items(self):
        values = []
        for item in self.items:
            temp = []
            for key in item:
                if key in self.keys:
                    temp.append(item[key])
            values.append(temp)

        self.list_variable.set(values)  # Update the value of the StringVar

    def display(self, root, row, column):
        self.root = root

        self.list_variable = StringVar()  # Create the StringVar after creating the root window

        self.insert_items()

        self.lb = Listbox(root, listvariable=self.list_variable)
        self.lb.grid(row=row, column=column)

    def update_items(self):
        self.items = self.load_items()
        self.insert_items()
        self.lb.update()
        print("Listbox updated!")
        
        
class TotalSalary:
    
    def __init__(self):
        self.total_salary = 0
        self.output = None
    
    def load_items(self) -> list:
        with open('Personalregister/database.json', 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = list()

        return data
    
    def calculate_total(self):
        data = self.data = self.load_items()
        self.total_salary = 0
        for person in data:
            self.total_salary += person['Lön']
            
    def display(self, root, row, column):
        frame = Frame(root)
        frame.grid(row=row, column=column)
        
        label = Label(frame, text="Total Lönekostnad")
        label.grid(row=0, column=0)
        self.output = Entry(frame, state=DISABLED)
        self.output.grid(row=1, column=0)
        button = Button(frame, text="Beräkna total lönekostnad", command=self.update_total)
        button.grid(row=2, column=0)
        
    def update_total(self):
        self.calculate_total()
        self.output.config(state=NORMAL)
        self.output.delete(0, 'end')
        self.output.insert(0, f"{self.total_salary}"),
        self.output.config(state=DISABLED)
        
        
#################### MAIN ####################

# creating three staff objects of different types
salesman = Salesman()
consultant = Consultant()
clerk = Clerk()

# create windows
registry = Window('registry', ['Namn', 'Typ'])
salaries = Window('löneutbetalningar', ['Namn', 'Typ', 'Lön'])
total = TotalSalary()

# creating a window for the gui
window = Tk()
window.title('Personalregister')
window.geometry('600x400')

# displaying the staff objects in the window
salesman.display(window, 0, 0)
consultant.display(window, 0, 1)
clerk.display(window, 0, 2)

# display the staff members
registry.display(window, 1, 0)
salaries.display(window, 1, 1)
total.display(window, 1, 2)

def update_display():
    print("Update initialized")
    registry.update_items()
    salaries.update_items()

# starting the main loop of the window
window.mainloop()