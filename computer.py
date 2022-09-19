#create the class computer
class Computer:
   # the init method
    def __init__(self,description: str, processor_type: str, hard_drive_capacity: int,
                memory:int,operating_system:str,
                year_made:int,price:int):
        #instance variable needed for the class computer
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    
    # use the _str_ method to format the output of computer information 
    def __str__(self):
        return f'<Description: {self.description}, Processor_type:{self.processor_type}, hard_drive_capacity:{self.hard_drive_capacity}, Memory: {self.memory},Operating_system: {self.operating_system}, year_made: {self.year_made} Price: {self.price}>'

    # the method used to update to new operating system
    def set_operating_system(self, new_operating_system: str):
        self.operating_system = new_operating_system
    # used to update to new price
    def set_price(self, new_price: int):
        self.price = new_price
    # help with the output of operating system
    def operating_system(self):
        return f'<{self.operating_system}>'
    # help with the output of description
    def description(self):
        return f'<{self.description}>'
    # help with the output of year made
    def year_made(self):
        return f'<{self.year_made}>'


    # What attributes will it need?
    # description, processor_type, hard_drive_capacity, memory, operating_system,
    #year_made, price
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
   # You'll remove this when you fill out your constructor

    # What methods will you need?