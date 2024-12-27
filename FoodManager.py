from Models.FoodItem import FoodItem
from Models.FoodMenu import FoodMenu
from Models.Restaurant import Restaurant

class FoodManager:
    def __init__(self):
        self.Restaurants = self.__PrepareRestaurants

    def __PrepareFoodItems(self):
        item1 = FoodItem("VegBiriyani",4,150,"****")
        item2 = FoodItem("ChickenBiriyani",4.2,200,"****")
        item3 = FoodItem("Parota",4.5,70,"****")
        item4 = FoodItem("Dosa",4.9,35,"****")
        item5 = FoodItem("Noodles",3.8,160,"****")
        return [item1,item2,item3,item4,item5]

    def __PrepareFoodMenus(self):
        FoodItems = self.__PrepareFoodItems()

        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [FoodItems[0],FoodItems[3]]
        menu2 = FoodMenu("Non-Veg")
        menu2.FoodItems = [FoodItems[1],FoodItems[2]]
        menu3 = FoodMenu("Chinese")
        menu3.FoodItems = [FoodItems[4]]
        return [menu1,menu2,menu3]



    def __PrepareRestaurants(self):
        FoodMenus = self.PrepareFoodMenus()
        res1 = Restaurant("A2B",5,"Chennai",10)
        res1.FoodMenus = [FoodMenus[0]]
        res2 = Restaurant("Kanti",4.8,"Bangalore",15)
        res2.FoodMenus = [FoodMenus[0],FoodMenus[1]]
        res3 = Restaurant("KFC",3,"Dubai",30)
        res3.FoodMenus = [FoodMenus[1],FoodMenus[2]]
        return [res1,res2,res3]

