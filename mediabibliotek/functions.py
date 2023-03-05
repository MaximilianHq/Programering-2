class Media:

    #give every media object a title
    def __init__(self) -> None:
        self.item = dict()
        while True:
            self.title = input("Define title: ").capitalize()
            if self.title != "":
                break
        self.item['title'] = self.title
            
            
class Book(Media):

    def __init__(self) -> None:
        #inherit from parent
        super().__init__()
        self.type = "book"
        self.pages = dataTint("pages (int): ")
        self.item['type'] = self.type
        self.item['pages'] = self.pages 
        
    def __dict__(self) -> dict:
        return self.item


class Soundtrack(Media):

    def __init__(self) -> None:
        #inherit from parent
        super().__init__()
        self.type = "soundtrack"
        self.playTime = dataTint("playtime (min): ")
        self.item['type'] = self.type
        self.item['playTime'] = self.playTime
        
        def __dict__(self) -> dict:
            return self.item


class Movie(Soundtrack):

    def __init__(self) -> None:
        #inherit from parent
        super().__init__()
        self.type = "movie"
        self.resolution = dataTint("resolution (ex. 1080): ")
        self.item['type'] = self.type
        self.item['resolution'] = self.resolution

        def __dict__(self) -> dict:
            return self.item

def dataTint(attribute):
    while True:
        value = input(f"Define {attribute}")
        if value.isdigit() == True:
            return value
        else:
            print("Input must be an int")