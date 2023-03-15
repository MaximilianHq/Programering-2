class Media:

    def __init__(self) -> None:
        self.item = dict()
        #set title
        while True:
            title = input("Define title: ").capitalize()
            if title != "":
                self.item['title'] = title
                break
            
            
class Book(Media):

    def __init__(self) -> None:
        #inherit from parent
        super().__init__()
        self.item['type'] = '_book'
        self.item['pages'] = getValue("pages (int): ")
        self.item = sort(self.item)
        
    def get(self) -> dict:
        return self.item


class Soundtrack(Media):

    def __init__(self) -> None:
        #inherit from parent
        super().__init__()
        self.item['type'] = '_soundtrack'
        self.item['playTime'] = getValue("playtime (min): ")
        self.item = sort(self.item)
        
    def get(self) -> dict:
        return self.item
    

class Movie(Soundtrack):

    def __init__(self) -> None:
        #inherit from parent
        super().__init__()
        self.item['type'] = '_movie'
        self.item['resolution'] = getValue("resolution (ex. 1080): ")
        self.item = sort(self.item)

    def get(self) -> dict:
        return self.item
    
    
def getValue(attribute:str) -> int:
    #^get int value
    while True:
        value = input(f"Define {attribute}")
        if value.isdigit() == True:
            return value
        else:
            print("Input must be an int")
            
def sort(d:dict) -> dict:
    #sort items in dict
    newDict = dict(sorted(d.items(), reverse=True))
    return newDict