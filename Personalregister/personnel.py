from ui import*
import json



# a class for creating staff objects of different types
class Staff:
    def __init__(self):
        self.type = ''
        self.entries = [['Namn', str]]
        self.fields = list()
        self.root = None
        
    #create entries
    def make_entries(self):
        for input in self.entries:
            self.fields.append(Input_Field(input[0]))

    # displaying the staff object in a labeled frame with a button to register it
    def display(self, root, row, column):
        self.root = root
        
        frame = LabelFrame(root, text=self.type)
        frame.grid(row=row, column=column, padx=0, pady=0)

        for index, field in enumerate(self.fields):
            field.display(frame, index)

        button = Button(frame, text="Registrera", command=self.store_data)
        button.grid(row=len(self.fields)+1, column=0,
                    padx=0, pady=(15, 10), columnspan=2)
               

    # getting the values of the input fields and appending them to a json file
    def store_data(self):
        attributes = dict()
        
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
                
            #print(type(val),self.entries[i][1])
            
            #validate data type
            if type(val) == self.entries[i][1]:
                attributes[field.text] = val
            else:
                Label(self.root, text='1 or more of wrong data type').grid()
                return
            
        attributes['type'] = self.type

        with open('Personalregister/database.json', 'a+', encoding='utf-8') as file:

            try:
                staff = json.load(file)
            except json.JSONDecodeError:
                staff = list()

            staff.append(attributes)

            json.dump(staff, file, indent=3)
            file.truncate()
            
            
    def display_data(self, root, row, column, text):
        #create labelframe
        label_frame = LabelFrame(root, text=text)
        label_frame.grid(row=row, column=column, padx=0, pady=0)
        
        button = Button(label_frame, text="Registrera", command=self.store_data)
        button.grid(row=len(self.fields)+1, column=0,
                    padx=0, pady=(15, 10), columnspan=2)
        
        #for i, n in enumerate(dicts):
            #val = list(dicts[i].values())
            
        pass
    
    
class Window():
    
    def __init__(self):
        self.root = None
        self.type = None
        self.items = list()
        
    def load_items(self):
        with open('Personalregister/database.json', 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def insert_items(self, list):
        # add items to listbox
        for i, item in self.items:
            list.insert(i, item)
            
    def display(self, root, row, column):
        self.root = root
        
        frame = LabelFrame(self.root, text=self.type)
        frame.grid(row=row, column=column, padx=0, pady=0)
        
        list_items = Variable(value=self.items) #TODO fixa skit, https://www.pythontutorial.net/tkinter/tkinter-listbox/
        
        lb = Listbox(frame, listvariable=list_items)
        #self.insert_items(lb)
        
        
class Register(Window):
    
    def __init__(self):
        super().__init__()
        self.type = 'register'
        self.list_items()
        
    def list_items(self):
        items = self.load_items()
        for item in items:
            # delete the salary key
            del item['salary']
            print(self.items)


class Salesman(Staff):

    def __init__(self):
        super().__init__()
        self.type = 'salesman'
        self.entries.extend([['Provision', float], ['Försäljning', int]])
        self.make_entries()


"""class Consultant(Staff):

    def __init__(self):
        super().__init__()
        self.type = 'consultant'
        self.entries.extend([['Pay', int], ['Hours', int]])
        self.gen_entries()


class Clerk(Staff):

    def __init__(self):
        super().__init__()
        self.type = 'clerk'
        self.entries.extend([['Wage', int]])
        self.gen_entries()"""