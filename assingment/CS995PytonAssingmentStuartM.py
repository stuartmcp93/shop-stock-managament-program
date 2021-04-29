"""
CS995: Introduction to programming principles
    - Python Assingment
    - Stuart McPherson 27/10/2020
"""


#Import CSV module
import csv

#create ItemAndQty class
class ItemAndQty:
    def __init__(self, name = "", price = 0., quantity = 0):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
    
    #Representation function 
    def __repr__(self):
        return f"Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

    #cost function 
    def cost(self):
        cost = self.price * self.quantity
        return float(cost)
    

#Create Shop class - Which will be passed an ItemAndQty object
class Shop:
    def __init__(self, itemAndQtyObj):

        #dictionary to hold itemAndQty objects
        self.itemAndQtyObjDict = {itemAndQtyObj.name: itemAndQtyObj}

        #remove empty default keys before csv file is loaded
        del self.itemAndQtyObjDict[""]

    #addItemAndQty function
    def addItemAndQty(self, itemName, price, qty):
        
        #create new object with rows from csv file
        newItemObj = ItemAndQty(itemName, price, qty)
            

        #Check if item doesn't already exist in te shop object
        if newItemObj.name not in self.itemAndQtyObjDict: 
            
            #Update dictioanry
            self.itemAndQtyObjDict.update({newItemObj.name: newItemObj})
            

        else:
            #If does exist add quantity to existing item
            self.itemAndQtyObjDict[itemName].quantity += int(qty)
            
            
    #Load intial stock function to read CSV file 
    def loadInitialStock(self, fileName):
        csvFile = open(fileName, "r", newline='')
        csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')

        #Skip over column headings
        next(csvReader)

        #Iterate over rows in csv file to create ItemAndQty objects by calling addItemAndQty function
        for row in csvReader:
            self.addItemAndQty(row[0], row[1], row[2])
            


    #Check item and quantity by name function
    def itemAndQtyByName(self, itemName):

        #Check if name exists in object
        if itemName in self.itemAndQtyObjDict.keys():

            #return the object if it exists with the quantity in the shop
            return f"{itemName}: {self.itemAndQtyObjDict[itemName].quantity} in stock"

        else:
            return None


    #Check itemAndQtyByName function
    def itemsInStock(self, itemName):

        #Check if item name exists in object
        if itemName in self.itemAndQtyObjDict:

            #Call the itemAndQtyByName function
            return self.itemAndQtyByName(itemName)
        
        else:
            return f"{itemName}: 0 in stock"
            

#Create shopping object class - Which is passed a shop object       
class ShoppingBasket:
    def __init__(self, shopObj):

        #Get Shop object dictionary
        self.shopObj = shopObj.itemAndQtyObjDict
        
        #empty dictionary where basket items from the shop object will be added 
        self.basketDict = {}

    #addItemAndQty function - which takes name and quantity as arguments
    def addItemAndQty(self, name, qty):
        
        #Check that name is in the shop object
        if name not in self.shopObj.keys():
            return 0
        
        else:
            #get price from shopObj - need price to create ItemAndQty object that will be added to the basket
            price = self.shopObj[name].price

            #check that quantity is available in the shop object
            if qty <= self.shopObj[name].quantity:

                #If True subtract qty amount from quantity in the shop object
                self.shopObj[name].quantity -= qty

                #Create new object with the name, price and qty to be added to shopping basket dictionary
                addToBasket = ItemAndQty(name, price, qty)

            
            else:
                #If qty is more than what is in the shop object
                qty = self.shopObj[name].quantity

                #Set quantity in shop object to 0
                self.shopObj[name].quantity = 0

                #Create new object with amount to add 
                addToBasket = ItemAndQty(name, price, qty)
        
        #update basket with itemAndQty object
        self.basketDict.update({addToBasket.name: addToBasket}) 

    #Total cost function
    def totalCost(self):

        #Create variable to hold result
        total = 0

        #Iterate over keys in the dictionary 
        for i in self.basketDict.keys():

            #Call cost function on each item and add to total 
            total += self.basketDict[i].cost()
            
        #return the total cost
        return f"The total cost is {total}"
                
    #Function to clear the dictionary 
    def empty(self):
        self.basketDict.clear()



        
#A program to test functionality
if __name__ == "__main__":
    itemObj = ItemAndQty()
    shopObj = Shop(itemObj)
    shoppingB = ShoppingBasket(shopObj)

    #Pass csv file into shop object
    shopObj.loadInitialStock("shopItems.csv")

    #print out shop object dictionary of items 
    print(shopObj.itemAndQtyObjDict)
    print("=====================================")

    #Adding extra items to shop object and searching stock amount of other items 
    shopObj.addItemAndQty("beer", 2.5, 10) #Beer isn't on csv file
    shopObj.addItemAndQty("apples", 0.3, 5)
    print(shopObj.itemsInStock("apples"))
    print(shopObj.itemsInStock("pizza"))
    print(shopObj.itemAndQtyObjDict)
    print("=====================================")

    #Adding items from shop to basket and subtracting quantities from shop
    shoppingB.addItemAndQty("apples", 3)
    shoppingB.addItemAndQty("beer", 5)
    print(shopObj.itemAndQtyObjDict)
    print(shoppingB.basketDict)
    print(shoppingB.totalCost())
    print("=====================================")

    #Empty the shopping basket 
    shoppingB.empty()
    print(shoppingB.basketDict)
    



