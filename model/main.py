'''
Created on 29 Sep 2017

@author: Carmen Ramirez
'''


from RegularCoffee import *
from DecafCoffee import *
from extra import *
from string import upper

answer = 'A'                
while answer != 'Y':
    answer = 'B'
    order = raw_input("Introduce the order: ")
    orderDivided = order.split(",")
    print '------'
    #print orderDivided
    print 'The order is:'
    for i in orderDivided:
        print i.lstrip()
    print '------'
    while answer!='Y' and answer !='N':
        print 'Are the products correct? (Y/N)'
        answer = upper(raw_input())
        #print answer
        if answer!='Y' and answer !='N': 
            print 'Please press Y or N'
            
    if answer =='N':
        print 'Try it again, please'
    elif answer == 'Y':
        break
    
    

total = 0
totalF = 0

for i in orderDivided:
    #print i
    products= i.split()
    #print products
    amountProduct = int(products[0]) 
    
    if products[2]=='regular' or products[2] == 'decaf':
        
        if products[2]=='regular':
            regular = RegularCoffee()
            total = regular.getCost() * amountProduct
            print '--Regular coffees: ' + str(total)
        
        elif products[2] == 'decaf':
            decaf = DecafCoffee ()
            total = decaf.getCost() * amountProduct
            print '--Decaf coffeess: ' + str(total)
    
        addMilk = False
        addSugar = False
        addCream = False
        addSprinkles = False
        for i in products:
            suma = extra()
            if i == 'milk' and addMilk == False:           
                total = total + (suma.getMilk()*amountProduct)
                addMilk = True
            elif i == 'sugar' and addSugar == False:
                total = total + (suma.getSugar()*amountProduct)
                addSugar = True
            elif i == 'cream' and addCream == False:
                total = total + (suma.getCream()*amountProduct)
                addCream = True
            elif i == 'sprinkles' and addSprinkles == False:
                total = total + (suma.getSprinkles()*amountProduct)
                addSprinkles = True
        
        if addMilk or addSugar or addCream or addSprinkles:
            print 'Price with sides: ' + str(total)
    
    
    if products[2] == 'xigua':
        sliceXigua = extra() 
        total = sliceXigua.xigua * int(products[0])
        print '--Xigua total: ' + str(total)
        
    totalF = totalF + total

print 'Final bill is $: ' + str(totalF)
  












