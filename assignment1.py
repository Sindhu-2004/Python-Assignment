# '''inventory = [
#     # name,       category,   unit_price, units_sold, units_left
#     ["Strawberry", "Fruit",      3.50,        40,          10],
#     ["Broccoli",   "Vegetable",  2.20,        25,           8],
#     ["Cheddar",    "Dairy",      5.00,        18,           4],
#     ["Baguette",   "Bakery",     2.80,        35,           2],
#     ["Blueberry",  "Fruit",      4.00,        22,           6],
#     ["Spinach",    "Vegetable",  1.80,        30,          12],
#     ["Yogurt",     "Dairy",      1.20,        50,          15],
#     ["Croissant",  "Bakery",     3.00,        28,           3],
# ]'''
# def inventory():
#     return (("Strawberry", "Fruit",      3.50,        40,          10),
#             ("Broccoli",   "Vegetable",  2.20,        25,           8),
#             ("Cheddar",    "Dairy",      5.00,        18,           4),
#             ("Baguette",   "Bakery",     2.80,        35,           2),
#             ("Blueberry",  "Fruit",      4.00,        22,           6),
#             ("Spinach",    "Vegetable",  1.80,        30,          12),
#             ("Yogurt",     "Dairy",      1.20,        50,          15),
#             ("Croissant",  "Bakery",     3.00,        28,           3))

# name, category, unit_price, units_sold, units_left = inventory()

# # print(f'Name : {name}, Designation : {designation}, Salary : {salary}')  

# 

# total = unit_price * units_sold
# print(f'Total price : {total}')


def inventory():
    return (("Strawberry", "Fruit",      3.50,        40,          10),
            ("Broccoli",   "Vegetable",  2.20,        25,           8),
            ("Cheddar",    "Dairy",      5.00,        18,           4),
            ("Baguette",   "Bakery",     2.80,        35,           2),
            ("Blueberry",  "Fruit",      4.00,        22,           6),
            ("Spinach",    "Vegetable",  1.80,        30,          12),
            ("Yogurt",     "Dairy",      1.20,        50,          15),
            ("Croissant",  "Bakery",     3.00,        28,           3))



# 1. calculate the TotalRevenue
# Call the function and store data
items = inventory()

total_revenue = 0
for item in items:
    name, category, unit_price, units_sold, units_left = item
    revenue = unit_price * units_sold
    print(f"{name} revenue: ${revenue:.2f}")
    total_revenue += revenue

print(f"\nTotal revenue from all products: ${total_revenue:.2f}")


# 2. List Low stock item if stock is less than 5
for item in items:
    name, category, unit_price, units_sold, units_left = item
    if units_left < 5:
        print(item)

# 3.calculte the categorywise Revenue

items = inventory()

total_revenue = 0
for item in items:
    name, category, unit_price, units_sold, units_left = item
    revenue = unit_price * units_sold
    print(f"{name} revenue: ${revenue:.2f}")
    #total_revenue += revenue

#print(f"\nRevenue from all products: ${revenue:.2f}")
