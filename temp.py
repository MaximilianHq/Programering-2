from tkinter import *
from tkinter import messagebox
import PersonalRegisterKlasser

#Lista på arbetare
employees = []



reg = Tk()

#Variabeldefinition
strSellerName = StringVar()
strProvision = StringVar()
strSale = StringVar()
strConsultantName = StringVar()
strHourRate = StringVar()
strHoursWorked = StringVar()
strPenpusherName = StringVar()
strMonthsPay = StringVar()

#Funktionsdefinition
def relist():
    listBoxRegister.delete(0, END)

    for e in employees:
        listBoxRegister.insert(0, e)
    
    #listBoxSaleries.delete(0, END)

    #for e in employees:
        #listBoxSaleries.insert(0, e)

#Skickar inmatade värden fårn säljar-inmatningsfälten till klassen och matar in det i listan av arbetare
def buttonSeller():

    try:
        seller = PersonalRegisterKlasser.Seller(strSellerName.get(), int(strProvision.get()), int(strSale.get()))  
        print("done1")
        employees.append(seller)
        relist()
    except:
        messagebox.showerror("Obs! Provision och försäljning kräver heltalssiffror som värde.")

#Skickar inmatade värden fårn konsult-inmatningsfälten till klassen och matar in det i listan av arbetare
def buttonConsultant():

    try:
        consultant = PersonalRegisterKlasser.Consultant(strConsultantName.get(), int(strHourRate.get()), int(strHoursWorked.get()))
        employees.append(consultant)
        relist()
    except:
        messagebox.showerror("Obs! Timlön och antal arbetstimmar kräver heltalssiffror som värde.")
#Skickar inmatade värden fårn kontorist-inmatningsfälten till klassen och matar in det i listan av arbetare
def buttonPenpusher():

    try:
        penpusher = PersonalRegisterKlasser.Penpusher(strPenpusherName.get(), int(strMonthsPay.get()))
        employees.append(penpusher)
        relist()
    except:
        messagebox.showerror("Obs! Timlön och antal arbetstimmar kräver heltalssiffror som värde.")
def countSalaries():
    pass

reg.geometry("650x350")

#Fönster för säljare
labelForSeller = LabelFrame(reg, text = "Säljare", width=220, height=150, container= True).place(x=15, y=10)
labelForConsultant = LabelFrame(reg, text = "Konsult", width=220, height=150, container= True).place(x=250, y=10)
labelForPenpusher = LabelFrame(reg, text = "Kontorist", width=220, height=150, container= True).place(x=480, y=10)

labelSellerName = Label(labelForSeller, text = "Namn").place(x = 30, y =30)
entrySellerName = Entry(labelForSeller, textvariable=strSellerName).place(x = 100, y = 30)
labelProvision = Label(labelForSeller, text = "Provision").place(x = 30, y =60)
entryProvision = Entry(labelForSeller, textvariable=strProvision).place(x = 100, y = 60)
labelSale = Label(labelForSeller, text = "Försäljning").place(x = 30, y =90)
entrySale = Entry(labelForSeller, textvariable=strSale).place(x = 100, y = 90)


#Fönster för konsult
labelConsultantName = Label(labelForConsultant, text = "Namn").place(x = 265, y =30)
entryConsultantName = Entry(labelForConsultant, textvariable=strConsultantName).place(x = 335, y = 30)
labelHourRate = Label(labelForConsultant, text = "Timlön").place(x = 265, y =60)
entryHourRate = Entry(labelForConsultant, textvariable=strHourRate).place(x = 335, y = 60)
labelHoursWorked = Label(labelForConsultant, text = "Arbetstid").place(x = 265, y =90)
entryHoursWorked = Entry(labelForConsultant, textvariable=strHoursWorked).place(x = 335, y = 90)


#Fönster för kontorist
labelPenpusherName = Label(labelForPenpusher, text = "Namn").place(x = 495, y =30)
entryPenpusherName = Entry(labelForPenpusher, textvariable=strPenpusherName).place(x = 565, y = 30)
labelMonthsPay = Label(labelForPenpusher, text = "Månadslön").place(x = 495, y =60)
entryMonthsPay = Entry(labelForPenpusher, textvariable=strMonthsPay).place(x = 565, y = 60)

#Registeringsknappar för de olika typerna av arbetare
buttonSeller2 = Button(labelForSeller, command=lambda: [buttonSeller(), print(employees)], text="Registrera", width=26).place(x = 30, y = 120)
buttonConsultant2 = Button(labelForConsultant, command=buttonConsultant, text="Registrera", width=26).place(x = 265, y = 120)
buttonPenpusher2 = Button(labelForPenpusher, command=buttonPenpusher, text="Registrera", width=26).place(x = 495, y = 120)

#Register Listboxen
labelRegister = Label(reg, text = "Register").place(x = 30, y = 170)
listBoxRegister = Listbox(reg, width=30, height=8)
listBoxRegister.place(x = 30, y= 190)

#Lön listboxen
labelSaleries = Label(reg, text = "Löner").place(x = 265, y = 170)
listBoxSaleries = Listbox(reg, width=30, height=8)
listBoxSaleries.place(x = 265, y= 190)


reg.mainloop()