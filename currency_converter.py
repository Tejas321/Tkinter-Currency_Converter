from tkinter import *
import tkinter.messagebox  as tsmg

root =Tk()
bg = PhotoImage(file="3.png")
label_pk=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
root.title("GUI : Currency Conversion")

Top = Frame(root, bg='yellow', pady=2, width=3000, height=100, relief=SUNKEN)
Top.grid(row=0, column=0)
headlabel =Label(Top, font=('Arial Black', 19, 'bold'),text='        Python Project         :        Currency Converter   ',
                     bg='orange', fg='white').grid(row=1, column=0, sticky=W)

variable1 = StringVar(root)
variable2 = StringVar(root)
variable1.set("currency")
variable2.set("currency")


def RealTimeCurrencyConversion():
    from forex_python.converter import CurrencyRates
    c = CurrencyRates()

    from_currency = variable1.get()
    to_currency = variable2.get()

    if (Amount1_field.get() == ""):
        tsmg.showinfo("Error !!", "Amount Not Entered.\n Please a valid amount.")

    elif (from_currency == "currency" or to_currency == "currency"):
        tsmg.showinfo("Error !!","Currency Not Selected.\n Please select FROM and TO Currency form menu.")

    else:
        new_amt = c.convert(from_currency, to_currency, float(Amount1_field.get()))
        new_amount = float("{:.4f}".format(new_amt))
        Amount2_field.insert(0, str(new_amount))

def clear_all():
    Amount1_field.delete(0, END)
    Amount2_field.delete(0, END)


CurrenyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR","IDR", "BGN",
"GBP", "JPY","SEK","SGD","HKD","CHF","HRK","NZD","RUB", "MXN","BRL"]

root.configure(background='gray')
root.geometry("700x480")
root.maxsize(700,480)

Label_1 = Label(root, font=('Arial Black', 27, 'bold'), text="", padx=0, pady=0, bg="gray", fg="black")
Label_1.grid(row=1, column=0, sticky=W)

label1 = Label(root, font=('Arial Black', 15, 'bold'), text="Amount            : ", bg="gray", fg="black")
label1.grid(row=2, column=0, sticky=W)

label1 = Label(root, font=('Arial Black', 15, 'bold'), text="From Currency : ", bg="gray", fg="black")
label1.grid(row=3, column=0, sticky=W)

label1 = Label(root, font=('Arial Black', 15, 'bold'), text="To Currency     : ", bg="gray", fg="black")
label1.grid(row=4, column=0, sticky=W)

label1 = Label(root,font=('Arial Black', 15,'bold'), text = "Converted Amount  :  ", bg="gray",fg = "black")
label1.grid(row=8, column=0,sticky=W)

Label_1 = Label(root, font=('Arial Black', 7, 'bold'), text="", padx=0, pady=0, bg="gray", fg="black")
Label_1.grid(row=5, column=0, sticky=W)

Label_1 = Label(root, font=('Arial Black', 7, 'bold'), text="", padx=0, pady=0, bg="gray", fg="black")
Label_1.grid(row=7, column=0, sticky=W)

Label_1 = Label(root, font=('Arial Black', 7, 'bold'), text="",padx=0,pady=0, bg="gray", fg="black")
Label_1.grid(row=8, column=0, sticky=N)


FromCurrency_option = OptionMenu(root, variable1, *CurrenyCode_list).grid(row=3, column=0, ipadx=80,sticky=E)
ToCurrency_option = OptionMenu(root, variable2, *CurrenyCode_list).grid(row=4, column=0, ipadx=80, sticky=E)


Amount1_field = Entry(root)
Amount1_field.grid(row=2, column=0, ipadx=64, sticky=E)
Amount2_field = Entry(root)
Amount2_field.grid(row=8, column=0, ipadx=64, sticky=E)


Convert_button = Button(root, font=('Arial Black', 16, 'bold'), text="   Convert  ", padx=2, pady=2, bg="light green",
                        fg="red",command=RealTimeCurrencyConversion).grid(row=6, column=0)

Clear_button = Button(root, font=('Arial Black', 16, 'bold'), text="   Clear All  ", padx=2, pady=2, bg="blue", fg="red",
                command=clear_all).grid(row=10, column=0)

root.mainloop()

