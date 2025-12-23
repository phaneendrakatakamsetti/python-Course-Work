# -----------------------------
# Zomato Mini Application
# -----------------------------

# Tuple (fixed food categories)
categories = ("Biryani", "Pizza", "Fast Food")

# Set (delivery cities)
delivery_cities = {"Hyderabad", "Bangalore", "Chennai"}

# Dictionary (food price list)
price_list = {
    "Biryani": 250.0,
    "Pizza": 180.0,
    "Burger": 120.0
}

# User Inputs
customer_name = input("Enter customer name: ")

item1 = input("Enter food item 1 (Biryani/Pizza/Burger): ").title()
item2 = input("Enter food item 2 (Biryani/Pizza/Burger): ").title()

quantity = int(input("Enter quantity: "))

# List (order items)
order_items = [item1, item2]

# Price calculation with validation
if item1 in price_list and item2 in price_list:
    total_price = (price_list[item1] + price_list[item2]) * quantity
else:
    print("\n❌ Invalid food item selected")
    exit()

# Output
print("\n🍽️ Welcome to Zomato")
print("Customer Name:", customer_name)
print("Food Categories:", categories)
print("Delivery Cities:", delivery_cities)
print("Ordered Items:", order_items)
print("Quantity:", quantity)
print("Total Bill Amount: ₹", total_price)
