import tkinter  as tk 


class Input_Field():
    def __init__(self, root, title, x, y):
        self.root = root
        self.title = title
        self.x = x
        self.y = y

        self.display()

    def display(self):

        text = tk.Label(root, text = self.title)
        text.place(x = self.x, y = self.y)

        entry = tk.Entry(self.root) 
        entry.place(x = self.x+50, y = self.y)
        entry.config(font=('helvetica', 14))
       
        canvas1.create_window(self.x, self.y, window=entry)


class Säljare():
    def init(self, root, namn) -> None:
        self.root = root
        self.namn = namn

    def display(self):
        entry1 = tk.Entry(self.root) 
        entry1.config(font=('helvetica', 14))
        canvas1.create_window(200, 100, window=entry1)

        entry2 = tk.Entry(self.root) 
        entry2.config(font=('helvetica', 14))
        canvas1.create_window(200, 160, window=entry2)

        entry3 = tk.Entry(self.root) 
        entry3.config(font=('helvetica', 14))
        canvas1.create_window(200, 200, window=entry3)



 
#Window object
root = tk.Tk()


canvas1 = tk.Canvas(root, width=400, height=300)
canvas1.pack()



Input_Field(root, "Namn", 0, 50)
Input_Field(root, "Provision", 0, 90)
Input_Field(root, "Försäljning", 0, 130)


def printSomething():
    # x1 = entry1.get()
    # print(x1)
    pass

w = tk.Button (root, text="press me", command= printSomething)
w.pack()
 
#Update popup screen
root.mainloop()