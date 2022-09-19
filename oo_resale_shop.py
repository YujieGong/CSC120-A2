"""
   Filename: oo_resale_shop.py
Description: object oriented programming version of the resale shop
     Author: Yujie Gong
       Date: 18 September 2022
"""
from typing import Dict
from typing import Optional
from computer import Computer


class ResaleShop():
    # What attributes will it need?

    def __init__(self):
        self.inventory: Dict[int, Computer] = {}
        self.item_id = 0
    
    def buy(self, computer):
        self.item_id =+ 1
        self.inventory[self.item_id] = computer
        print(f"Buying {computer.description}")
        return self.item_id
        

    def refurbish(self, item_id, new_operating_system):
        computer = self.inventory[item_id]
        old_operating_system = computer.operating_system
        if item_id in self.inventory:
            self.change_price_in_refurbish(item_id)
            if new_operating_system is not None:
                self.new_operating_system(item_id, new_operating_system)
                print(f'Refurbishing Item id: {item_id} , updating {old_operating_system} to {new_operating_system}')
        else:
            print(f'Item {item_id} not found. Please select another item to refurbish.')
    
    def change_price_in_refurbish(self, item_id):
        computer = self.inventory[item_id]
        if computer.year_made < 2000:
            computer.set_price(0)
        elif computer.year_made < 2012:
            computer.set_price(250)
        elif computer.year_made < 2018:
            computer.set_price(550)
        else:
            computer.set_price(1000)
    
    def new_operating_system(self,item_id:int, new_operating_system: str):
        computer = self.inventory[item_id]
        computer.set_operating_system(new_operating_system)
    
    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory:
            self.inventory[item_id].set_price(new_price)
        else:
             print(f'Item {item_id} not found. Cannot update price.')

    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print(f'Selling Item ID: {item_id}')
            print(f'Item {item_id} sold!')
        else:
            print(f'Item {item_id} not found. Please select another item to sell.')
    
    def print_computer(self, item_id: int):
        if item_id in self.inventory:
            print(f'Item ID: {item_id} {self.inventory[item_id]}')
        else:
            print("No inventory to display.")
    

     
    


# What attributes will it need? 




    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
   # You'll remove this when you fill out your constructor
# What methods will you need?
#storing information about a specific computer
#storing the inventory for the store
#updating a computer's price
#updating a computer's OS
#buying a computer (add to inventory)
#selling a computer (remove from inventory)
#refurbishing a computer

