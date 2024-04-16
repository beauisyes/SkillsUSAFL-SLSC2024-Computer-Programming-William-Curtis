import tkinter as tk
from tkinter import messagebox

# GUI that holds the input form
class inputGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x700")
        self.master.title("Registration Form")
        self.create_form()

    # function to create the form
    def create_form(self):
        # frame to hold the form in
        self.form_frame = tk.Frame(self.master)
        self.form_frame.pack(padx=5,pady=5)

        # Prompts user for name
        self.name_label = tk.Label(self.form_frame, text="What is your name?")
        self.name_label.pack(padx=5,pady=5)
        self.name = tk.Entry(self.form_frame)
        self.name.pack(padx=5,pady=5)

        # Prompts user for address
        self.address_label = tk.Label(self.form_frame, text="Enter your address (address line, city, state, and zip code)")
        self.address_label.pack(padx=5,pady=5)
        self.address = tk.Entry(self.form_frame)
        self.address.pack(padx=5,pady=5)

        # Prompts user for emergency contact information
        self.emergency_contact_label = tk.Label(self.form_frame, text="Enter your emergency contact's name and phone number")
        self.emergency_contact_label.pack(padx=5,pady=5)
        self.emergency_contact = tk.Entry(self.form_frame)
        self.emergency_contact.pack(padx=5,pady=5)

        # Asks the user if they're staying for half a day or the entire day
        self.choice_label = tk.Label(self.form_frame, text="half-day or a full-day?")
        self.choice_label.pack(padx=5,pady=5)

        self.day_choice = tk.StringVar()

        # List consisting of tuples to hold values for the radio button delcarations
        MODE = [
            ("Half-Day", "Half-Day"),
            ("Full-Day", "Full-Day")
        ]

        # Sets the automatic radio button selection
        self.day_choice.set("Half-Day")
        
        # Loops through the amount of tuples in the MODE list creating radio buttons
        for text, mode in MODE:
            tk.Radiobutton(self.form_frame, text=text, variable=self.day_choice, value=mode).pack(padx=5,pady=5)

        # Prompts the user for the amount of days they're staying
        self.day_count_label = tk.Label(self.form_frame, text="How many days are you staying?")
        self.day_count_label.pack(padx=5,pady=5)
        self.day_count=tk.Entry(self.form_frame)
        self.day_count.pack(padx=5,pady=5)

        # Tells the user to select any extra activites they want
        self.extra_activities_label = tk.Label(self.form_frame, text="Choose any other extra activities you wish to partake in")
        self.extra_activities_label.pack(padx=5,pady=5)

        self.extra_activity_swimming = tk.BooleanVar()
        self.extra_activity_canoeing = tk.BooleanVar()
        self.extra_activity_horseback_riding = tk.BooleanVar()
        self.extra_activity_crafts = tk.BooleanVar()

        #Creates the check buttons for each extra activity
        self.extra_activity_swimming_check = tk.Checkbutton(self.form_frame, text="Swimming", onvalue=True, offvalue=False, variable=self.extra_activity_swimming)
        self.extra_activity_canoeing_check = tk.Checkbutton(self.form_frame, text="Canoeing", onvalue=True, offvalue=False, variable=self.extra_activity_canoeing)
        self.extra_activity_horseback_riding_check = tk.Checkbutton(self.form_frame, text="Horseback Riding", onvalue=True, offvalue=False, variable=self.extra_activity_horseback_riding)
        self.extra_activity_crafts_check = tk.Checkbutton(self.form_frame, text="Crafts", onvalue=True, offvalue=False, variable=self.extra_activity_crafts)
        self.extra_activity_swimming_check.pack(padx=5,pady=5)
        self.extra_activity_canoeing_check.pack(padx=5,pady=5)
        self.extra_activity_horseback_riding_check.pack(padx=5,pady=5)
        self.extra_activity_crafts_check.pack(padx=5,pady=5)
        
        #Creates a button to clear the inputs of the form
        self.clear_button = tk.Button(self.form_frame, text="Clear", command=lambda: self.clear())
        self.clear_button.pack(padx=5,pady=5)

        #Creates a button to submit their order
        self.submit_button = tk.Button(self.form_frame, text="Submit", command=lambda: self.submit())
        self.submit_button.pack(padx=5,pady=5)

        #Creates a button to close the program
        self.close_button = tk.Button(self.form_frame, text="Close", command=lambda: self.close())
        self.close_button.pack(padx=5,pady=5)

    # function to clear the input fields
    def clear(self):
        self.form_frame.forget()
        self.create_form()

    # function to submit the form and open the output GUI
    def submit(self):
        # Attempts the necessary conversion and if it fails, throw an error popup
        noErrors = True
        try:
            name = str(self.name.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a valid input for the name")
            noErrors = False
        try:
            day_count = int(self.day_count.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a valid input for the amount of days you're staying")
            noErrors = False

        if self.emergency_contact.get() == "":
            messagebox.showinfo("Error!", "Please fill out the information for your emergency contact")
            noErrors = False

        if self.address.get() == "":
            messagebox.showinfo("Error!", "Please fill out your address")
            

        #If there were not any errors, it opens the second GUI
        if noErrors:
            root2 = tk.Tk()
            app2 = outputGUI(root2,name,day_count,self.day_choice.get(),self.extra_activity_swimming.get(),self.extra_activity_canoeing.get(),self.extra_activity_horseback_riding.get(),self.extra_activity_crafts.get())
            root2.mainloop()

    #function to close the program
    def close(self):
        self.master.destroy()

# Class that holds the outputs and calculations
class outputGUI:
    def __init__(self,master,name:str,day_count:int,day_choice:str,swimming:bool,canoeing:bool,horseback_riding:bool, crafts:bool):
        self.master = master
        self.master.title("Output")
        self.name = name
        self.day_count = day_count
        self.day_choice = day_choice
        self.swimming = swimming
        self.canoeing = canoeing
        self.horseback_riding = horseback_riding
        self.crafts = crafts

        #Displays the user's name
        self.name_label = tk.Label(self.master, text=self.name, font=('Arial',25))
        self.name_label.pack(padx=5,pady=5)

        #Displays the user's day choice
        self.day_choice_label = tk.Label(self.master, text="Day Choice", font=('Arial',22))
        self.day_choice_label.pack(padx=5,pady=5)
        self.day_choice_display = tk.Label(self.master, text=self.day_choice, font=('Arial',20))
        self.day_choice_display.pack(padx=5,pady=5)

        #Displays the extra activities that the user chose
        self.extra_activities_label = tk.Label(self.master, text="Extra Activities Chosen", font=('Arial', 22))
        self.extra_activities_label.pack(padx=5,pady=5)

        #If statements to ensure only the chosen extra activities are displayed
        if self.swimming:
            self.swimming_display = tk.Label(self.master, text="Swimming $5.00", font=('Arial', 15))
            self.swimming_display.pack(padx=5,pady=5)
        if self.canoeing:
            self.canoeing_display = tk.Label(self.master, text="Canoeing $7.50", font=('Arial', 15))
            self.canoeing_display.pack(padx=5,pady=5)
        if self.horseback_riding:
            self.horseback_riding_display = tk.Label(self.master, text="Horseback Riding $8.75", font=('Arial', 15))
            self.horseback_riding_display.pack(padx=5,pady=5)
        if self.crafts:
            self.crafts_display = tk.Label(self.master, text="Crafts $4.00", font=('Arial',15))
            self.crafts_display.pack(padx=5,pady=5)
        
        #Displays the amount of days the user will be staying
        self.day_count_display = tk.Label(self.master, text="You will be staying here for " + str(self.day_count) + " days", font=('Arial', 17))
        self.day_count_display.pack(padx=5,pady=5)

        #Displays the total cost of the order
        self.total_cost_label = tk.Label(self.master, text="Total Cost", font=('Arial', 25))
        self.total_cost_label.pack(padx=5,pady=5)
        self.total_cost_display = tk.Label(self.master, text="$" + str(self.calculate_total_price()), font=('Arial',18))
        self.total_cost_display.pack(padx=5,pady=5)

        #Asks the user if they are certain this is their final order
        self.confirmation_label = tk.Label(self.master, text="Is this your final order?", font=('Arial', 15))
        self.confirmation_label.pack(padx=5,pady=5)

        #Button to finalize the order
        self.confirmation_button = tk.Button(self.master, text="Order", command=lambda: self.submit())
        self.confirmation_button.pack(padx=5,pady=5)
        
        #Button to cancel the order and go back to the input form
        self.cancellation_button = tk.Button(self.master, text="Cancel", command=lambda: self.close())
        self.cancellation_button.pack(padx=5,pady=5)

    #function to finalize the order
    def submit(self):
        messagebox.showinfo("Confirmed", "Order has been made!")
        self.master.destroy()
        
    #function to close the output GUI and return to the input GUI
    def close(self):
        self.master.destroy()
        
    #Function to calculate the total price
    def calculate_total_price(self):
        price = 0
        if self.day_choice == "Half-Day":
            price += 25
        elif self.day_choice == "Full-Day":
            price += 35
        if self.swimming:
            price += 5
        if self.canoeing:
            price += 7.5
        if self.horseback_riding:
            price += 8.75
        if self.crafts:
            price += 4
        price *= self.day_count
        return price

def main():
    root = tk.Tk()
    app = inputGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()