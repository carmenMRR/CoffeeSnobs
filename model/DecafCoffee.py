'''
Created on 28 Sep 2017

@author: CarmenM
'''

from Beverage import  *

class DecafCoffee(Beverage):    
    
    def __init__(self):         #contructor de la clase
        self.price = 1.51
        self.description = 'Decaf Coffee'