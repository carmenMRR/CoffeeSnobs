'''
Created on 28 Sep 2017

@author: CarmenM
'''

class Beverage(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.price = 0
        self.description = ''
      
    
    def getDescription (self):
        return self.description 
        
    def getCost(self):
        return self.price