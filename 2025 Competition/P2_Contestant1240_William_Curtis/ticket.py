class ticket:
    def __init__(self, name : str, email : str, phone_number : int, details : str):
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.details = details
        self.resolved = False

    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_details(self):
        return self.details
    
    def isResolved(self):
        return self.resolved
    
    def resolve(self):
        self.resolved = True
    
    def toString(self):
        return self.name + "\n" + self.email + "\n" + str(self.phone_number) + "\n" + self.details
    
    def savedData(self):
        return [self.name, self.email, str(self.phone_number), self.details]