import tkinter as tk
from tkinter import messagebox

# A list to hold all the team names
TEAM_NAMES = [
    "Hawks",
    "Eagles",
    "Bears",
    "Gorillas",
    "Cheetahs"
]

# BattingPercentagesInputGUI holds a GUI of the input form for the program
class BattingPercentagesInputGUI:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x600")
        self.master.title("Batting Percentages Calculator")

        # Creates the labels and the input fields for the program
        self.create_labels()
        self.create_entries()

        # Button to clear the input fields
        self.clear_button = tk.Button(self.master, padx=5,pady=5, text="Clear", command=lambda: self.clear())
        self.clear_button.grid(row=1, column=1, padx=5, pady=10)

        # Button to calculate the program
        self.calculate_button = tk.Button(self.master, padx=5,pady=5, text="Calculate", command=lambda: self.calculate())
        self.calculate_button.grid(row=2, column=1, padx=5, pady=10)

        # Button to close the program
        self.exit_button = tk.Button(self.master, text="Close", command=lambda: self.close())
        self.exit_button.grid(row=3, column=1, padx=5, pady=10)

    def calculate(self):
        # Attempts the correct conversion for each input before opening the output GUI
        # Provides an error if the conversion fails
        noErrors = True
        try:
            player_name = str(self.player_name.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a valid input for player name")
            noErrors = False
        
        try:
            team_code = int(self.team_code.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a valid input for team code")
            noErrors = False

        try:
            times_at_bat = int(self.times_at_bat.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a vaiid input for times at bat")
            noErrors = False

        try:
            singles = int(self.singles.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a valid input for singles")
            noErrors = False
        
        try:
            doubles = int(self.doubles.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a valid input for doubles")
            noErrors = False
        
        try:
            triples = int(self.triples.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a valid input for triples")
            noErrors = False

        try:
            homeruns = int(self.homeruns.get())
        except:
            messagebox.showinfo("Error!", "Ensure you have a valid input for homeruns")
            noErrors = False
        
        #opens the output GUI
        if noErrors:
            root2 = tk.Tk()
            app2 = OutputGUI(root2, player_name, team_code, times_at_bat, singles, doubles, triples, homeruns)
            root2.mainloop()
            
    # function to clear the entries
    def clear(self):
        self.entry_frame.forget()
        self.create_entries()

    # function to close the program
    def close(self):
        self.master.destroy()

    # function to create all the entries in a frame
    def create_entries(self):
        self.entry_frame = tk.Frame(self.master)
        self.entry_frame.grid(row=0, column=2)

        # Input field for player's name
        self.player_name = tk.Entry(self.entry_frame)
        self.player_name.pack(padx=5,pady=5)

        # Input field for team code
        self.team_code = tk.Entry(self.entry_frame)
        self.team_code.pack(padx=5,pady=5)

        # Input field for number of times at bat
        self.times_at_bat = tk.Entry(self.entry_frame)
        self.times_at_bat.pack(padx=5,pady=5)

        # Input field for the number of singles
        self.singles = tk.Entry(self.entry_frame)
        self.singles.pack(padx=5,pady=5)

        # Input field for the number of doubles
        self.doubles = tk.Entry(self.entry_frame)
        self.doubles.pack(padx=5,pady=5)

        # Input field for the number of triples
        self.triples = tk.Entry(self.entry_frame)
        self.triples.pack(padx=5,pady=5)

        # Input field for the number of homeruns
        self.homeruns = tk.Entry(self.entry_frame)
        self.homeruns.pack(padx=5,pady=5)

    # function to create all the labels inside a frame
    def create_labels(self):
        # Creates a label frame to hold all the labels for the inputs
        self.label_frame = tk.Frame(self.master)
        self.label_frame.grid(row=0, column=0)
        # Creates a label to help distinguish the player name input field
        self.player_name_label = tk.Label(self.label_frame, text="Player Name")
        self.player_name_label.pack(padx=5,pady=5)
        # Creates a label to help distinguish the team code input field
        self.team_code_label = tk.Label(self.label_frame, text="Team code")
        self.team_code_label.pack(padx=5,pady=5)
        # Creates a lable to help distinguish the amount of times the player was at bat input field
        self.times_at_bat_label = tk.Label(self.label_frame, text="Number of times the player was at bat")
        self.times_at_bat_label.pack(padx=5,pady=5)
        # Creates a lable to help distinguish the amount of singles input field
        self.singles_label = tk.Label(self.label_frame, text="How many singles did the player hit?")
        self.singles_label.pack(padx=5,pady=5)
        # Creates a lable to help distinguish the amount of doubles input field
        self.doubles_label = tk.Label(self.label_frame, text="How many doubles did the player hit?")
        self.doubles_label.pack(padx=5,pady=5)
        # Creates a lable to help distinguish the amount of triples input field
        self.triples_label = tk.Label(self.label_frame, text="How many triples did the player hit?")
        self.triples_label.pack(padx=5,pady=5)
        # Creates a lable to help distinguish the amount of homeruns input field
        self.homeruns_label = tk.Label(self.label_frame, text="How many homeruns did the player hit?")
        self.homeruns_label.pack(padx=5,pady=5)

# OutputGUI shows the calculations and results based on the inputs from the BattingPercentagesInputGUI
class OutputGUI:
    def __init__(self, master, player_name : str, team_code : int, times_at_bat : int, singles : int, doubles : int, triples : int, homeruns : int):
        self.master = master
        self.master.geometry("400x300")
        self.master.title("Output")

        # Creates a label to display the player's name
        self.name_label = tk.Label(self.master, text=player_name + " Stats", font=('Arial', 20))
        self.name_label.pack(padx=5,pady=5)

        # Creates a label to display the player's team
        self.team_name_label = tk.Label(self.master, text=self.find_team_name(team_code), font=('Arial', 17))
        self.team_name_label.pack(padx=5,pady=5)

        # Creates a label to distinguish the player's batting average
        self.batting_average_label = tk.Label(self.master, text="Batting Average", font=('Arial', 15))
        self.batting_average_label.pack(padx=5,pady=5)

        # Creates a label to display the player's batting average
        self.batting_average_display = tk.Label(self.master, text=str(self.calculate_batting_average(times_at_bat, singles, doubles, triples, homeruns)) +"%", font=('Arial', 14))
        self.batting_average_display.pack(padx=5,pady=5)

        # Creates a label to distinguish the player's slugging percentage
        self.slugging_percentage_label = tk.Label(self.master, text="Slugging Percentage", font=('Arial', 15))
        self.slugging_percentage_label.pack(padx=5,pady=5)

        # Creates a label to display the player's slugging percentage
        self.slugging_percentage_display = tk.Label(self.master, text=str(self.calculate_slugging_percentage(times_at_bat, singles, doubles, triples, homeruns)) + "%", font=('Arial', 14))
        self.slugging_percentage_display.pack(padx=5,pady=5)

        # Creates a button to close the output window
        self.close_button = tk.Button(self.master, text="Close", command=lambda: self.close_program())
        self.close_button.pack(padx=5,pady=5)
    
    # function to calculate and return the batting average
    def calculate_batting_average(self, times_at_bat, singles, doubles, triples, homeruns):
        total_hits = singles + doubles + triples + homeruns
        batting_average = total_hits/times_at_bat
        return round(batting_average,2) * 100
    
    # function to calculate and return the slugging percentage
    def calculate_slugging_percentage(self, times_at_bat, singles, doubles, triples, homeruns):
        bases_achieved = singles + (2 * doubles) + (3 * triples) + (4 * homeruns)
        slugging_percentage = bases_achieved/times_at_bat
        return round(slugging_percentage, 2) * 100
    
    # function to find the team name based on the team code
    def find_team_name(self, team_code):
        for i in range(len(TEAM_NAMES)):
            if i == team_code:
                return TEAM_NAMES[i]

    # function to close the output GUI
    def close_program(self):
        self.master.destroy()

#function to start the GUI
def main():
    root = tk.Tk()
    app = BattingPercentagesInputGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()