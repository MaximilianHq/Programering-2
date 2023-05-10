from tkinter import*
from personnel import*

# creating three staff objects of different types
salesman = Salesman()
"""consultant = Consultant()
clerk = Clerk()"""

# create registry
registry = Register()

# creating a window for the gui
window = Tk()
window.title('Staffregister')
window.geometry('600x400')

# displaying the staff objects in the window
salesman.display(window, 0, 0)
"""consultant.display(window, 0, 1)
clerk.display(window, 0, 2)"""

# display the staff members
registry.display(window, 1, 0)

# starting the main loop of the window
window.mainloop()