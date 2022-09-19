class Computer:

    # What attributes will it need?
     # How will you set up your constructor?
    def __init__(self,description: str, processor_type: str, hard_drive_capacity: int,
                memory:int,operating_system:str,
                year_made:int,price:int):
   
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    # Remember: in python, all constructors have the same name (__init__)
    # What methods will you need?
    def __str__(self):
        return f'<Description: {self.description}, Processor_type:{self.processor_type}, hard_drive_capacity:{self.hard_drive_capacity}, Memory: {self.memory},Operating_system: {self.operating_system}, year_made: {self.year_made} Price: {self.price}>'


    def set_operating_system(self, new_operating_system: str):
        self.operating_system = new_operating_system

    def set_price(self, new_price: int):
        self.price = new_price
    
    def operating_system(self):
        return f'<{self.operating_system}>'
   
    def description(self):
        return f'<{self.description}>'

    def year_made(self):
        return f'<{self.year_made}>'


    # What attributes will it need?
    # description, processor_type, hard_drive_capacity, memory, operating_system,
    #year_made, price
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
   # You'll remove this when you fill out your constructor

    # What methods will you need?