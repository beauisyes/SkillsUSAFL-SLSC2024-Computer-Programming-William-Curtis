import datetime
import tkinter as tk

class Expense:
    def __init__(self, name : str, date : str, description : str, amount : float, category : str):
        self.name = name
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

    def get_name(self):
        return self.name
    
    def get_date(self):
        return self.date
    
    def get_description(self):
        return self.description
    
    def get_amount(self):
        return self.amount
    
    def get_category(self):
        return self.category
    
    def toString(self):
        return self.get_date() + " | " + self.get_description() + " | $" + str(self.get_amount()) +" | "+ self.get_category()
        