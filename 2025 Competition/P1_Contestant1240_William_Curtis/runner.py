import tkinter as tk
from tkinter import messagebox
from Expense import Expense
from tkcalendar import Calendar
import datetime

#in terminal use pip install tkcalendar to get the tkcalendar module

CATEGORIES = ["Food", "Gas", "Rent", "Entertainment", "Other"]
EXPENSES:list[Expense]= list()

class ExpenseTrackerMainMenuGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Expense Tracker")
        self.create_menu()

    def create_menu(self):
        self.menu_frame = tk.Frame(self.master)
        self.menu_frame.pack()

        self.menu_label = tk.Label(self.menu_frame, text="Expense Tracker", font=('Arial', 16))
        self.menu_label.pack(padx=5,pady=5)

        self.add_expense_button = tk.Button(self.menu_frame, text="Add Expense", command= lambda: self.add_expense())
        self.add_expense_button.pack(padx=5,pady=4)

        self.view_all_expenses_button = tk.Button(self.menu_frame, text="View all expenses", command= lambda: self.view_all_expenses())
        self.view_all_expenses_button.pack(padx=5,pady=4)

        self.view_total_by_category_button = tk.Button(self.menu_frame, text="View total spent by category", command=lambda: self.view_total_by_category())
        self.view_total_by_category_button.pack(padx=5,pady=4)

        self.view_total_spent_today_button = tk.Button(self.menu_frame, text="View total spent today", command=lambda: self.view_total_spent_today())
        self.view_total_spent_today_button.pack(padx=5,pady=4)

        self.exit_button = tk.Button(self.menu_frame, text="Exit", command=lambda: self.exit())
        self.exit_button.pack(padx=5,pady=4)

    def add_expense(self):
        self.add_expense_window = tk.Toplevel(self.master)
        self.add_expense_window.geometry("500x600")
        self.add_expense_window.title("Add expense")
        
        self.add_expense_label = tk.Label(self.add_expense_window, text="Add an expense", font=('Arial', 13))
        self.add_expense_label.pack(padx=5,pady=3)

        self.name_label = tk.Label(self.add_expense_window, text="Add name")
        self.name_label.pack(padx=5,pady=1)

        self.name_entry = tk.Entry(self.add_expense_window)
        self.name_entry.pack(padx=5,pady=1)

        self.date_label = tk.Label(self.add_expense_window, text="Add Date of Transaction", font=('Arial',11))
        self.date_label.pack(padx=5,pady=1)

        self.date_calendar = Calendar(self.add_expense_window, selectmode = "day", year = datetime.datetime.now().year, month = datetime.datetime.now().month, day = datetime.datetime.now().day)
        self.date_calendar.pack(padx=5,pady=3)

        self.description_label = tk.Label(self.add_expense_window, text="Add a description")
        self.description_label.pack(padx=5,pady=1)

        self.description_entry = tk.Entry(self.add_expense_window)
        self.description_entry.pack(padx=5,pady=1)

        self.amount_label = tk.Label(self.add_expense_window, text="Add amount of expense")
        self.amount_label.pack(padx=5,pady=1)

        #This is used to ensure the user can only input a float
        vcmd = (self.add_expense_window.register(self.validate_float), '%P')

        self.amount_entry = tk.Entry(self.add_expense_window, validate="key", validatecommand=vcmd)
        self.amount_entry.pack(padx=5,pady=1)

        self.category_label = tk.Label(self.add_expense_window, text="Which category is your expense?")
        self.category_label.pack(padx=5,pady=1)

        self.category_choice = tk.StringVar(value="Categories")

        self.category_optionmenu = tk.OptionMenu(self.add_expense_window, self.category_choice, *CATEGORIES)
        self.category_optionmenu.pack(padx=5,pady=1)

        self.submit_expense_button = tk.Button(self.add_expense_window, text="Add Expense", command=lambda: self.submit_expense())
        self.submit_expense_button.pack(padx=5,pady=5)

    def submit_expense(self):
        #check for errors
        if self.category_choice.get() == "Categories" or self.name_entry.get() == "" or self.description_entry.get() == "" or self.amount_entry.get() == "" or self.category_choice.get() == "":
            messagebox.showerror("Error","Ensure your inputs are properly done")
        else:
            EXPENSES.append(Expense(self.name_entry.get(), self.date_calendar.get_date(), self.description_entry.get(), float(self.amount_entry.get()), self.category_choice.get()))
            self.add_expense_window.destroy()
           
            
    def view_all_expenses(self):
        self.view_all_expenses_window = tk.Toplevel(self.master)
        self.view_all_expenses_window.geometry("500x500")
        self.view_all_expenses_window.title("View all expenses")

        for expense in EXPENSES:
            tk.Label(self.view_all_expenses_window, text=expense.toString(), font= ('Arial', 14)).pack()

    def view_total_by_category(self):
        self.view_total_by_category_window = tk.Toplevel(self.master)
        self.view_total_by_category_window.geometry("500x500")
        self.view_total_by_category_window.title("View Total Spent by Category")

        self.view_total_of_which_label = tk.Label(self.view_total_by_category_window, text="Pick a category to look at the total spent")
        self.view_total_of_which_label.pack(padx=5,pady=4)

        self.category_choice_for_total = tk.StringVar(value="Categories")

        self.category_optionmenu = tk.OptionMenu(self.view_total_by_category_window, self.category_choice_for_total, *CATEGORIES)
        self.category_optionmenu.pack(padx=5,pady=1) 

        self.view_total_of_which_button = tk.Button(self.view_total_by_category_window, text="View Total", command=lambda: self.show_total_by_category(self.category_choice_for_total))
        self.view_total_of_which_button.pack(padx=5,pady=3)

    def show_total_by_category(self, category):
        total = 0
        for expense in EXPENSES:
            if category.get() == "Catergories":
                messagebox.showerror("Error", "Choose a category")
                break
            if expense.get_category() == category.get():
                total += expense.get_amount()
        messagebox.showinfo("total","Total spent in category: $" + str(total))



    def view_total_spent_today(self):
        total = 0
        todays_date = str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().year)[2:4]
        for expense in EXPENSES:
            if expense.get_date() == todays_date:
                total += expense.get_amount()
        messagebox.showinfo("total spent today", "Total Spent Today: $" + total)


    
    def exit(self):
        self.master.destroy()

    

    def validate_float(self, new_value):
        if new_value == "":
            return True
        if new_value.count('.') > 1:
            return False
        try:
            float(new_value)
            return True
        except ValueError:
            return False



        
def main():
    root = tk.Tk()
    app = ExpenseTrackerMainMenuGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()