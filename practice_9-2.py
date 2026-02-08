## 9-2

class Restaurant:
    """"""
    def __init__(self, restaurant_name , cuisine_type):
        """Initialize restaurant_name and """
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}.")
        print(f"Cuisine_type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

restaurant1 = Restaurant('Sakura', 'Japanese')
restaurant2 = Restaurant('Luigi', 'Italian')
restaurant3 = Restaurant('Dragon', 'Chinese')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()