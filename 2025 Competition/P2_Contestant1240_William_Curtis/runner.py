import tkinter as tk
from ticket import ticket
from tkinter import messagebox

Tickets : list[ticket] = list()

#Admin Commands are ran in the terminal after providing the admin password: ADMIN101

class CustomerServiceSubmissionInputGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x500")
        self.master.title("Customer Service Submission")
        self.new_submssion()

    #Creates the form and its widgets
    def new_submssion(self):
        self.new_submssion_frame = tk.Frame(self.master)
        self.new_submssion_frame.pack()

        self.title_label = tk.Label(self.new_submssion_frame, text="Customer Service Submission", font=('Arial',20))
        self.title_label.pack(padx=5,pady=8)

        self.new_name_label = tk.Label(self.new_submssion_frame, text="Enter your name")
        self.new_name_label.pack(padx=5,pady=2)

        self.new_name_entry = tk.Entry(self.new_submssion_frame)
        self.new_name_entry.pack(padx=5,pady=2)

        self.new_email_label = tk.Label(self.new_submssion_frame, text="Enter your email")
        self.new_email_label.pack(padx=5,pady=2)

        self.new_email_entry = tk.Entry(self.new_submssion_frame)
        self.new_email_entry.pack(padx=5,pady=2)

        self.new_phone_number_label = tk.Label(self.new_submssion_frame, text="Enter your phone number")
        self.new_phone_number_label.pack(padx=5,pady=2)

        vcmd = (self.new_submssion_frame.register(self.validate_int), '%P')

        self.new_phone_number_entry = tk.Entry(self.new_submssion_frame, validate="key", validatecommand=vcmd)
        self.new_phone_number_entry.pack(padx=5,pady=2)

        self.new_request_details_label = tk.Label(self.new_submssion_frame, text="Enter the details of your request")
        self.new_request_details_label.pack(padx=5,pady=2)

        self.new_request_details_entry = tk.Entry(self.new_submssion_frame)
        self.new_request_details_entry.pack(padx=5,pady=2)

        self.submit_new_request_button = tk.Button(self.new_submssion_frame, text="Submit", command=lambda: self.submit_ticket())
        self.submit_new_request_button.pack(padx=5,pady=5)

        self.admin_button = tk.Button(self.new_submssion_frame, text="Admin Panel (terminal)", command=lambda:self.admin_view())
        self.admin_button.pack(padx=5,pady=10)

        self.close_button = tk.Button(self.new_submssion_frame, text="Close", command=lambda: self.close())
        self.close_button.pack(padx=5,pady=5)
        
    def submit_ticket(self):
        errors = False

        if self.new_name_entry.get() == "" or self.new_email_entry.get() == "" or self.new_phone_number_entry.get() == "" or self.new_request_details_entry.get() == "":
            errors = True

        try:
            int(self.new_phone_number_entry.get())
        except:
            errors = True
        
        if not "@" in self.new_email_entry.get():
            errors = True

        
        if not errors:
            new_ticket = ticket(self.new_name_entry.get(), self.new_email_entry.get(), int(self.new_phone_number_entry.get()), self.new_request_details_entry.get())
            Tickets.append(new_ticket)
            messagebox.showinfo("Submitted", "Your Ticket has been submitted")
        else:
            messagebox.showerror("Error", "Ensure your inputs are correct")

    def close(self):
        self.master.destroy()

    def validate_int(self, new_value):
        if new_value == "":
            return True
        try:
            int(new_value)
            return True
        except:
            return False
    
    def admin_view(self):
        logging_in = True
        admin_password = "ADMIN101"
        while logging_in:
            login = input("Enter the Admin Password to Continue or q to quit\n")
            if admin_password == login:
                logging_in = False
            elif login.lower() == "q":
                quit()
            else:
                print("Wrong Password")
        choosing = True
        while choosing and logging_in == False:
            #Admin menu
            print("Admin View:")
            print("1. View Tickets Stats")
            print("2. Resolve Tickets")
            print("3. Close Admin Terminal Panel")

            #Menu Choosing
            choice = input()
            if not choice == "1" and not choice == "2" and not choice == "3":
                print("Input 1 or input 2")
            else:
                choosing = False
        #Ticket Stats Screen
        if choice == "1":
            print("Ticket count: " + str(len(Tickets)))
            print("Tickets Resolved: " + self.check_resolved_count())
            print("Tickets Unresolved: " + self.check_unresolved_count())
            self.admin_view()
        #Resolve Tickets Screen
        if choice == "2":
            for ticket in Tickets:
                if not ticket.isResolved():
                    print(ticket.toString())
                    resolve_choosing = True
                    while resolve_choosing:
                        resolve = input("Do you wish to resolve? (y/n)")
                        if resolve.lower() == "y" or resolve.lower() == "n":
                            resolve_choosing = False
                    if resolve.lower() == "y":
                        ticket.resolve()
            print("You have checked all the tickets")
            choosing = True
            self.admin_view()
        if choice == "3":
            quit()

    #Counts the amount of resolved tickets
    def check_resolved_count(self):
        count = 0
        for ticket in Tickets:
            if ticket.isResolved():
                count+=1
        return str(count)

    #Counts the amount of unresolved tickets
    def check_unresolved_count(self):
        count = 0
        for ticket in Tickets:
            if not ticket.isResolved():
                count+=1
        return str(count)

def main():
    root = tk.Tk()
    app = CustomerServiceSubmissionInputGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()