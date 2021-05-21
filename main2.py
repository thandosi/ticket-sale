# Importing the tkinter module
from tkinter import *
from tkinter import ttk
from tkinter import messagebox   # importing the messagebox from tkinter


class ClsTicketSales:
    def __init__(self, master):
        self.root = root
        self.root.title("ticket sale")
        self.root.geometry("1000x800")

        # Cell number label
        self.cell_lbl = Label(master, text="Enter Cell Number:")
        self.cell_lbl.place(x=10, y=30)
        self.cell_entry = Entry(master)
        self.cell_entry.place(x=200, y=30)

        # Category
        self.category_lbl = Label(master, text="Select Ticket Category:")
        self.category_lbl.place(x=10, y=80)
        self.var = StringVar()
        self.category_list = ttk.Combobox(master, textvariable=self.var, width=18, value=["Soccer", "Movie", "Theater"])
        self.category_list.place(x=200, y=74)

        # tickets label
        self.tickets_bought = Label(master, text="Number Of Tickets Bought:")
        self.tickets_bought.place(x=10, y=130)
        self.bought_entry = Spinbox(master, from_=1, to=100, width=17)
        self.bought_entry.place(x=200, y=130)

        # My btn
        self.calculate_button = Button(master, text="Calculate Ticket", fg="black", command=self.calc)
        self.calculate_button.place(x=10, y=180)
        self.clear_button = Button(master, text="Clear Entries", fg="black", command=self.clear)
        self.clear_button.place(x=200, y=180)

        # Output section
        self.lb1 = Label(master, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.lb1.place(x=10, y=230)

        self.payable = Label(master, text="Amount Payable: ")
        self.payable.place(x=10, y=260)
        self.payable_output = Label(master, text="", )
        self.payable_output.place(x=180, y=260)

        self.reservation = Label(master, text="Reservation: ")
        self.reservation.place(x=10, y=290)
        self.reservation_output = Label(master, text="", )
        self.reservation_output.place(x=180, y=290)

        self.num_of_tics = Label(master, text="No of Tickets: ")
        self.num_of_tics.place(x=10, y=320)
        self.num_of_tics_out = Label(master, text="", )
        self.num_of_tics_out.place(x=180, y=320)

        self.number = Label(master, text="Cell Number: ")
        self.number.place(x=10, y=350)
        self.number_out = Label(master, text="", )
        self.number_out.place(x=180, y=350)

        self.lb2 = Label(master, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        self.lb2.place(x=10, y=380)

        # Exit Button
        self.exit_btn = Button(master, text="Exit", fg="black", width=15, command=self.exit)
        self.exit_btn.place(x=120, y=410)

    # defining a method to validate the inputs from the customer and make calculations
    def calc(self):
        # to make sure all entries are filled
        if self.category_list.get() == "" or self.bought_entry.get() == "" or self.cell_entry.get() == "":
            self.message_box = messagebox.showerror('Input Error', 'Please make sure all the input fields are filled')

        # If yes continue
        else:

            # for Soccer
            if self.category_list.get() == "Soccer":

                # Calculations
                vat = (40 * int(self.bought_entry.get())) * 0.14
                total = (40 * int(self.bought_entry.get())) + vat

                # Printing the outputs to the interface
                self.payable_output.config(text=str(total))
                self.num_of_tics_out.config(text=str(self.bought_entry.get()))
                self.reservation_output.config(text=str(self.category_list.get()))
                self.number_out.config(text=str(self.cell_entry.get()))

             # Movie
            elif self.category_list.get() == "Movie":
                # Calculations
                vat = (75 * int(self.bought_entry.get())) * 0.14
                total = (75 * int(self.bought_entry.get())) + vat

                # Printing the outputs to the interface
                self.payable_output.config(text=str(total))
                self.num_of_tics_out.config(text=str(self.bought_entry.get()))
                self.reservation_output.config(text=str(self.category_list.get()))
                self.number_out.config(text=str(self.cell_entry.get()))

             # Theater
            elif self.category_list.get() == "Theater":
                # Calculations
                vat = (100 * int(self.bought_entry.get())) * 0.14
                total = (100 * int(self.bought_entry.get())) + vat

                # Printing the outputs
                self.payable_output.config(text=str(total))
                self.num_of_tics_out.config(text=str(self.bought_entry.get()))
                self.reservation_output.config(text=str(self.category_list.get()))
                self.number_out.config(text=str(self.cell_entry.get()))

    # to clear the output
    def clear(self):
        self.cell_entry.delete(0, END)
        self.category_list.delete(0, END)
        self.bought_entry.delete(0, END)
        self.payable_output.config(text="")
        self.num_of_tics_out.config(text="")
        self.reservation_output.config(text="")
        self.number_out.config(text="")

    # exit btn
    def exit(self):
        self.message_box = messagebox.askquestion('Exit Application', 'Are you sure you want to exit the application')
        if self.message_box == 'yes':
            self.root.destroy()
        else:
            pass


root = Tk()
app = ClsTicketSales(root)
root.mainloop()
