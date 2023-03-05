import functions
import sys
import time
import io
import json

def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./100) #change the denominators value to change type speed
  
mediaList = list()

def intro():
    slowprint("\nWelcome to THE Library, here you can both add and access unfathomable amounts of media")

def writeData(item):
    with io.open("mediabibliotek/database.json", "a", encoding="utf-8") as file:
        json.dump(item, file)
        file.close()
        
def readData():
    with io.open("mediabibliotek/database.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        return lines
        
def displayData(type):
    for i in range(0, len(mediaList)):
        text = mediaList[i].split()
        if text[0] == type:
            print("\nList of", type + "s:")
            print(' '.join(mediaList[i].split()[2:]))
        elif type.lower() == "all":
            print(mediaList[i])
            
            
dict_example = {'a': 1, 'b': 2}
print(dict_example)
            
mediaList = readData()
intro()

book = functions.Book()
print(book)

while True:
    #menu
    slowprint("\n*_*_*_ MENU _*_*_*\n")
    slowprint("1. Show list all")
    slowprint("2. Show list books")
    slowprint("3. Show list soundtracks")
    slowprint("4. Show list movies")
    slowprint("5. New Book")
    slowprint("6. New Soundtrack")
    slowprint("7. New Movie")
    slowprint("8. Quit\n")

    #store input
    val = input()

    if val == "1":
        displayData("all")
            
    elif val == "2":
        displayData("book")
                
    elif val == "3":
        #show soundtracks from media list
        displayData("soundtrack")
                
    elif val == "4":
        #show movie from media list
        displayData("movie")

    elif val == "5":
        #add book to list media
        print("\nNew book")
        book = functions.Book()
        writeData(book)

    elif val == "6":
        #add book to list media
        print("\nNew soundtrack")
        soundtrack = functions.Soundtrack()
        writeData(soundtrack)

    elif val == "7":
        #add book to list media
        print("\nNew movie")
        movie = functions.Movie()
        writeData(movie)

    elif val == "8":
        #exit program
        break