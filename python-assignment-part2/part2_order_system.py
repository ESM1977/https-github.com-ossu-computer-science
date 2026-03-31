# part2_order_system.py
# Restaurant Menu & Order Management System

import copy   # needed for deep copy later

# ------------------ GIVEN DATA ------------------

menu = {
    "Paneer Tikka":   {"category": "Starters",  "price": 180.0, "available": True},
    "Chicken Wings":  {"category": "Starters",  "price": 220.0, "available": False},
    "Veg Soup":       {"category": "Starters",  "price": 120.0, "available": True},
    "Butter Chicken": {"category": "Mains",     "price": 320.0, "available": True},
    "Dal Tadka":      {"category": "Mains",     "price": 180.0, "available": True},
    "Veg Biryani":    {"category": "Mains",     "price": 250.0, "available": True},
    "Garlic Naan":    {"category": "Mains",     "price":  40.0, "available": True},
    "Gulab Jamun":    {"category": "Desserts",  "price":  90.0, "available": True},
    "Rasgulla":       {"category": "Desserts",  "price":  80.0, "available": True},
    "Ice Cream":      {"category": "Desserts",  "price": 110.0, "available": False},
}

inventory = {
    "Paneer Tikka": {"stock": 10, "reorder_level": 3},
    "Chicken Wings": {"stock": 8, "reorder_level": 2},
    "Veg Soup": {"stock": 15, "reorder_level": 5},
    "Butter Chicken": {"stock": 12, "reorder_level": 4},
    "Dal Tadka": {"stock": 20, "reorder_level": 5},
    "Veg Biryani": {"stock": 6, "reorder_level": 3},
    "Garlic Naan": {"stock": 30, "reorder_level": 10},
    "Gulab Jamun": {"stock": 5, "reorder_level": 2},
    "Rasgulla": {"stock": 4, "reorder_level": 3},
    "Ice Cream": {"stock": 7, "reorder_level": 4},
}

sales_log = {
    "2025-01-01": [
        {"order_id": 1, "items": ["Paneer Tikka", "Garlic Naan"], "total": 220.0},
        {"order_id": 2, "items": ["Gulab Jamun", "Veg Soup"], "total": 210.0},
        {"order_id": 3, "items": ["Butter Chicken", "Garlic Naan"], "total": 360.0},
    ],
    "2025-01-02": [
        {"order_id": 4, "items": ["Dal Tadka", "Garlic Naan"], "total": 220.0},
        {"order_id": 5, "items": ["Veg Biryani", "Gulab Jamun"], "total": 340.0},
    ],
    "2025-01-03": [
        {"order_id": 6, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
        {"order_id": 7, "items": ["Butter Chicken", "Veg Biryani"], "total": 570.0},
        {"order_id": 8, "items": ["Garlic Naan", "Gulab Jamun"], "total": 130.0},
    ],
    "2025-01-04": [
        {"order_id": 9, "items": ["Dal Tadka", "Garlic Naan", "Rasgulla"], "total": 300.0},
        {"order_id": 10, "items": ["Paneer Tikka", "Gulab Jamun"], "total": 270.0},
    ],
}

# ------------------ TASK 1: Explore the Menu ------------------

print("\n--- MENU ---")

# collect all categories first
categories = set(item["category"] for item in menu.values())

# print items category-wise
for cat in categories:
    print(f"\n===== {cat} =====")
    for name, details in menu.items():
        if details["category"] == cat:
            status = "Available" if details["available"] else "Unavailable"
            print(f"{name:15} ₹{details['price']:6.2f} [{status}]")

# basic stats
print("\nTotal number of items on the menu:", len(menu))

available = sum(1 for i in menu.values() if i["available"])
print("\nTotal number of available items:", available)

# find most expensive item
exp_item = max(menu.items(), key=lambda x: x[1]["price"])
print("\nMost expensive Item:", exp_item[0], exp_item[1]["price"])

# items below 150
print("\nItems priced under ₹150:")
for name, details in menu.items():
    if details["price"] < 150:
        print(name, details["price"])


# ------------------ TASK 2: Cart Operation ------------------

cart = []   # empty cart

# function to add item
def add_item(name, qty):
    if name not in menu:
        print(f"Cannot add '{name}' -> Item not present in menu")
        return
    
    if not menu[name]["available"]:
        print(f"Cannot add '{name}' -> Item currently not available")
        return
    
    # check if already in cart
    for i in cart:
        if i["item"] == name:
            i["quantity"] += qty
            print(f"Updated '{name}' quantity to {i['quantity']}.")
            return
    
    # otherwise add new entry
    cart.append({
        "item": name,
        "quantity": qty,
        "price": menu[name]["price"]
    })
    print(f"Added '{name}' x {qty} to cart.")

# remove item
def remove_item(name):
    for i in cart:
        if i["item"] == name:
            cart.remove(i)
            return
    print(f"Cannot remove '{name}' -> Item not found in cart")

# Function to update quantity
def update_quantity(name, qty):
    for i in cart:
        if i["item"] == name:
            i["quantity"] = new_quantity
            print(f"Quantity of '{name}' updated to {new_quantity}.")
            return
    print(f"Cannot update '{name}' -> Item not found in cart.")

# simulation
add_item("Paneer Tikka", 2)
add_item("Gulab Jamun", 1)
add_item("Paneer Tikka", 1)   # should increase quantity
add_item("Mystery Burger", 1) # not in menu
add_item("Chicken Wings", 1)  # unavailable
remove_item("Gulab Jamun")

# print cart
print("\n--- CART ---")
subtotal = 0

for i in cart:
    total = i["quantity"] * i["price"]
    subtotal += total
    print(f"{i['item']:15} x{i['quantity']} ₹{total}")

gst = subtotal * 0.05
print("Subtotal:", subtotal)
print("GST:", gst)
print("Total:", subtotal + gst)


# -------TASK 3: Inventory Tracker with Deep Copy -------------

# take backup before changes
inventory_backup = copy.deepcopy(inventory)

print("\n========== Deep Copy Check ==========")
print("Before manual change:")
print("Original inventory stock of Paneer Tikka:", inventory["Paneer Tikka"]["stock"])
print("Backup inventory stock of Paneer Tikka  :", inventory_backup["Paneer Tikka"]["stock"])

# Manually change one stock value in inventory
inventory["Paneer Tikka"]["stock"] = 9

print("\nAfter manual change in inventory:")
print("Original inventory stock of Paneer Tikka:", inventory["Paneer Tikka"]["stock"])
print("Backup inventory stock of Paneer Tikka  :", inventory_backup["Paneer Tikka"]["stock"])

# Restore inventory to original state before continuing
inventory = copy.deepcopy(inventory_backup)

print("\nAfter restoring inventory:")
print("Original inventory stock of Paneer Tikka:", inventory["Paneer Tikka"]["stock"])
print("Backup inventory stock of Paneer Tikka  :", inventory_backup["Paneer Tikka"]["stock"])

# Simulate order fulfilment using final cart from Task 2
print("\n========== Order Fulfilment ==========")

for i in cart:
    name = entry["item"]
    qty_needed = entry["quantity"]
    stock_available = inventory[name]["stock"]

    if stock_available >= qty_needed:
        inventory[name]["stock"] -= qty_needed
        print(f"{name}: Deducted {qty_needed} unit(s). Remaining stock = {inventory[name]['stock']}")
    else:
        print(f"Warning: Insufficient stock for {name}. Needed {qty_needed}, available {stock_available}.")
        inventory[name]["stock"] = 0
        print(f"{name}: Deducted only {stock_available} unit(s). Remaining stock = 0")

# Print reorder alerts
print("\n========== Reorder Alerts ==========")

for item, details in inventory.items():
    if details["stock"] <= details["reorder_level"]:
        print(f"⚠ Reorder Alert: {item} — Only {details['stock']} unit(s) left (reorder level: {details['reorder_level']})")

# Print final inventory and backup inventory
print("\n========== Final Inventory ==========")
for item, details in inventory.items():
    print(f"{item:<16} Stock: {details['stock']}, Reorder Level: {details['reorder_level']}")

print("\n========== Backup Inventory ==========")
for item, details in inventory_backup.items():
    print(f"{item:<16} Stock: {details['stock']}, Reorder Level: {details['reorder_level']}")


# -------TASK 4: Daily Sales Log Analysis ----------

print("\n============Revenue per day=========")

# function to calculate revenue
def show_revenue():
    result = {}
    for date, orders in sales_log.items():
        total = sum(o["total"] for o in orders)
        result[date] = total
        print(date, ":", total)
    return result

rev = show_revenue()

# best day
best = max(rev, key=rev.get)
print("\nBest selling day:", best)

# most ordered item
count = {}
for orders in sales_log.values():
    for o in orders:
        for item in o["items"]:
            count[item] = count.get(item, 0) + 1

print("\nMost ordered item:", max(count, key=count.get))

# adding new day
sales_log["2025-01-05"] = [
    {"order_id": 11, "items": ["Butter Chicken", "Gulab Jamun", "Garlic Naan"], "total": 490.0},
    {"order_id": 12, "items": ["Paneer Tikka", "Rasgulla"], "total": 260.0},
]

print("\n=========Updated revenue per day:===========")
updated_best_day = ""
updated_best_revenue = 0

for date, orders in sales_log.items():
    total = 0
    for order in orders:
        total += order["total"]
    
    print(f"{date} : ₹{total:.2f}")
    
    if total > updated_best_revenue:
        updated_best_revenue = total
        updated_best_day = date

print(f"\nUpdated best-selling day: {updated_best_day} — ₹{updated_best_revenue:.2f}")


# print all orders with numbering
print("\nAll Orders:")
num = 1
for date, orders in sales_log.items():
    for o in orders:
        print(f"{num}. [{date}] Order #{o['order_id']} ₹{o['total']} Items: {', '.join(o['items'])}")
        num += 1
