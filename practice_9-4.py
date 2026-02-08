## 9-4

class Restaurant:
    """"""
    def __init__(self, restaurant_name , cuisine_type):
        """Initialize restaurant_name and cuisine_type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurant name is {self.restaurant_name}.")
        print(f"Cuisine_type is {self.cuisine_type}.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

    def set_number_served(self, number):
        self.number_served = number
    
    def incremet_number_served(self, number):
        self.number_served += number

restaurant = Restaurant('nanami diner', 'Italian')
print(restaurant.number_served)

restaurant.set_number_served(15)
print(restaurant.number_served)

restaurant.incremet_number_served(5)
print(restaurant.number_served) 