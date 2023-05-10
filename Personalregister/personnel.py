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
            self.fields.append(Input_Field(input[0]))

    # displaying the staff object in a labeled frame with a button to register it
    def display(self, root, row, column):
        self.root = root
        
        self.frame = LabelFrame(root, text=self.type)
        self.frame.grid(row=row, column=column, padx=0, pady=0)

        for index, field in enumerate(self.fields):
            field.display(self.frame, index)

        button = Button(self.frame, text="Registrera", command=self.store_data)
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
                    self.warn_label.grid(row=4, column=0, columnspan=2)  # Adjust the column span as needed
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
            
    def display_data(self, root, row, column, text):
        #create labelframe
        label_frame = LabelFrame(root, text=text)
        label_frame.grid(row=row, column=column, padx=0, pady=0)
        
        button = Button(label_frame, text="Registrera", command=self.store_data)
        button.grid(row=len(self.fields)+1, column=0,
                    padx=0, pady=(15, 10), columnspan=2)
    
    
class Window():
    
    def __init__(self, type:str, keys:list):
        self.type = type
        self.keys = keys
        self.items = self.load_items()
        self.show_salary = False
        
    def load_items(self) -> list:
        with open('Personalregister/database.json', 'r', encoding='utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = list()

        return data
    
    def insert_items(self) -> Variable:
        values = []
        for item in self.items:
            temp = []
            for key in item:
                if key in self.keys:
                    temp.append(item[key])
            values.append(temp)

        return Variable(value=values)
            
    def display(self, root, row, column):
        self.root = root
        
        lb = Listbox(root, listvariable=self.insert_items())
        lb.grid(row=row, column=column)


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


"""class Consultant(Staff):

    def __init__(self):
        super().__init__()
        self.type = 'Konsult'
        self.entries.extend([['Pay', int], ['Hours', int]])
        self.gen_entries()


class Clerk(Staff):

    def __init__(self):
        super().__init__()
        self.type = 'Kontorist'
        self.entries.extend([['Wage', int]])
        self.gen_entries()"""