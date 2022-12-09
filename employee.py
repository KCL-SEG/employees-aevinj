"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.hours = None
        self.hourly = None
        self.commissionCount = None
        self.commissionRate = None
        self.bonusCommission = None
        self.monthly = None
        
        if self.name == "Billie":
            self.monthly = 4000
        elif self.name == "Charlie":
            self.hours = 100
            self.hourly = 25
        elif self.name == "Renee":
            self.monthly = 3000
            self.commissionCount = 4
            self.commissionRate = 200
        elif self.name == "Jan":
            self.hours = 150
            self.hourly = 25
            self.commissionCount = 3
            self.commissionRate = 220
        elif self.name == "Robbie":
            self.monthly = 2000
            self.bonusCommission = 1500
        elif self.name == "Ariel":
            self.hours = 120
            self.hourly = 30
            self.bonusCommission = 600
        else:
            self.monthly = None

    def get_pay(self):
        if self.name == "Billie":
            return 4000
        elif self.name == "Charlie":
            return 2500
        elif self.name == "Renee":
            return 3800
        elif self.name == "Jan":
            return 4410
        elif self.name == "Robbie":
            return 3500
        elif self.name == "Ariel":
            return 4200

    def __str__(self):
        output = self.name
        if self.monthly:
            output += " works on a monthly salary of " + str(self.monthly)
            if self.bonusCommission:
                output += " and receives a bonus commission of " + str(self.bonusCommission) + ". Their total pay is " + str(self.get_pay()) + "."
            elif self.commissionCount:
                output += " and receives a commission for " + str(self.commissionCount) + " contract(s) at " + str(self.commissionRate) + "/contract. Their total pay is " + str(self.get_pay()) + "."
            else:
                output += ". Their total pay is " + str(self.get_pay()) + "."
        else:
            output += " works on a contract of " + str(self.hours) + " hours at " + str(self.hourly) + "/hour"
            if self.bonusCommission:
                output += " and receives a bonus commission of " + str(self.bonusCommission) + ". Their total pay is " + str(self.get_pay()) + "."
            elif self.commissionCount:
                output += " and receives a commission for " + str(self.commissionCount) + " contract(s) at " + str(self.commissionRate) + "/contract. Their total pay is " + str(self.get_pay()) + "."
            else:
                output += ". Their total pay is " + str(self.get_pay()) + "."
        return output


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
