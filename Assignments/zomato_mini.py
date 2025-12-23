# -----------------------------
# ZOMATO MINI APPLICATION
# -----------------------------

# 1️⃣ tuple (food categories)
food_categories = ("Biryani", "Pizza", "Burger","Hot chipps")

# 2️⃣ set (delivery cities)
delivery_cities = {"Hyderabad", "Bangalore", "Chennai"}

# 3️⃣ dict (food prices)
food_prices = {
    "Biryani": 250.0,   # float
    "Pizza": 180.0,    # float
    "Burger": 120.0    # float
}

# 4️⃣ str (customer name)
customer_name = input("Enter customer name: ")

# 5️⃣ str (food items input)
item1 = input("Enter food item 1: ").title()
item2 = input("Enter food item 2: ").title()

# 6️⃣ int (quantity)
quantity = int(input("Enter quantity: "))

# 7️⃣ list (ordered items)
order_items = [item1, item2]

# Price calculation
if item1 in food_prices and item2 in food_prices:
    total_bill = (food_prices[item1] + food_prices[item2]) * quantity
else:
    print("❌ Invalid food item selected")
    exit()

# Output
print("\n🍽️ Welcome to Zomato")
print("Customer Name:", customer_name)
print("Food Categories:", food_categories)
print("Delivery Cities:", delivery_cities)
print("Ordered Items:", order_items)
print("Quantity:", quantity)
print("Total Bill Amount: ₹", total_bill)
