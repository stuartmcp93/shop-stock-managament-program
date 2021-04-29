import unittest
import CS995PytonAssingmentStuartM
from CS995PytonAssingmentStuartM import ItemAndQty
from CS995PytonAssingmentStuartM import Shop
from CS995PytonAssingmentStuartM import ShoppingBasket



class unitTest(unittest.TestCase):
        #create  item object needed for Shop class
        itemObj = ItemAndQty()
        #create a Shop object
        shopObj = Shop(itemObj)
        
        #A test function to test loading of CSV file into object
        def test_loadCsvIntoShop(self):
            #Load CSV file and save to variable
            loadedTest = self.shopObj.loadInitialStock("shopitems.csv")
            
            #Compare loadedTest variable by calling loadInitialStock()
            self.assertEqual(loadedTest, self.shopObj.loadInitialStock("shopItems.csv"))

        #A test function for testing adding items to shop object and checking stock items
        def test_addItemToShop(self):

            #Add new item, price and quantity to the shop
            self.shopObj.addItemAndQty("beer", 2.5, 10)

            #Check shop has 10 beers in stock
            self.assertEqual("beer: 10 in stock", self.shopObj.itemsInStock("beer"))

            #Check shop has 0 pizza in stock
            self.assertEqual("pizza: 0 in stock", self.shopObj.itemsInStock("pizza"))
        
        #A test function for testing shopping basket fucntionality
        def test_shoppingBasket(self):

            #adding new items to shop object
            self.shopObj.addItemAndQty("cakes", 0.5, 5)
            self.shopObj.addItemAndQty("tea", 1, 10)

            #Create a chopping basket object
            shoppingB = ShoppingBasket(self.shopObj)

            #Add items to the shopping basket
            shoppingB.addItemAndQty("cakes", 2)
            shoppingB.addItemAndQty("tea", 2)

            #Test totalCost of shopping basket function
            self.assertEqual("The total cost is 3.0", shoppingB.totalCost())

            #Test itemsInstock function
            self.assertEqual("cakes: 3 in stock", self.shopObj.itemsInStock("cakes"))





if __name__ == "__main__":
    unittest.main()