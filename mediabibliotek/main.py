import library
import sys
import time
import json

#load database
with open('mediabibliotek/database.json', 'r', encoding='utf-8') as json_file:
    dicts = json.load(json_file)

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./100) #<-- denominators value defines typing speed

def writeData():
    with open('mediabibliotek/database.json', 'w', encoding='utf-8') as file:
        json.dump(dicts, file, indent=2)
        file.close()
        
def displayData(type:str):
    #^displays data of certain type
    print("\nList of", type + "s:")
    for i in range(0, len(dicts)):
        if dicts[i]['type'] == type or type == 'all':
            val = list(dicts[i].values())
            print(*val, sep = " : ")
            
def getTypes() -> list:
    #^displays mediatype
    types = list()
    for i in range(0, len(dicts)):
        if types.count(dicts[i]['type']) == 0:
            types.append(dicts[i]['type'])
            
    return types

def editLibrary():
    #select mediatype
    while True:
        types = getTypes()
        type = input(f"Select type of obj. {types}: ")
        if types.count(type) > 0:
            break
        else:
            print("no such type")
            
    while True:
        displayData(type)
        
        #slect item to edit
        val = input("\nSelect item name: ")
        for i in range(0, len(dicts)):
            if dicts[i]['title'].lower() == val.lower() and dicts[i]['type'] == type:
                print(dicts[i])
                while True:
                    #select attribute to edit
                    val = input("Select action: delete, edit attribute(input): ")
                    #look for input in dicts
                    retVal = dicts[i].get(val)
                    if retVal is not None or val == 'delete':
                        break
                    else:
                        print("no such attribute")
                            
                if val == 'delete':
                    dicts.pop(i)
                else:
                    newAtrb = input(f"Change {val} to: ")
                    dicts[i][val] = newAtrb
                return
            
        print("no such item")
        continue
                    
#################### PROGRAM ####################

slowprint("\nWelcome to THE Library, here you can both add and access unfathomable amounts of media")

while True:
    print("\n*_*_*_ MENU _*_*_*\n")
    print("1. Show list all")
    print("2. Show list books")
    print("3. Show list soundtracks")
    print("4. Show list movies")
    print("5. New Book")
    print("6. New Soundtrack")
    print("7. New Movie")
    print("8. Edit list")
    print("9. Save 'n' Exit\n")

    #save action
    val = input()

    if val == '1':
        displayData('all')
            
    elif val == '2':
        displayData('_book')
                
    elif val == '3':
        displayData('_soundtrack')
                
    elif val == '4':
        displayData('_movie')

    elif val == '5':
        #add new book
        print("\nNew book")
        book = library.Book().get()
        dicts.append(book)

    elif val == '6':
        #add new soundtrack
        print("\nNew soundtrack")
        soundtrack = library.Soundtrack().get()
        dicts.append(soundtrack)

    elif val == '7':
        #add new movie2
        print("\nNew movie")
        movie = library.Movie().get()
        dicts.append(movie)

    elif val == '8':
        editLibrary()
                
    elif val == '9':
        #exit program
        break
    
    else:
        print("no such action")
    
#overwrite database
writeData()