## 9-1

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

restaurant = Restaurant('Tomato and Onion', 'Itarian')

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()