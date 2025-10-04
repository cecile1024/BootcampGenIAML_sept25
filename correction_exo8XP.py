sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# The deli has run out of pastrami, use a while loop to remove 
# all occurrences of Pastrami sandwich from sandwich_orders.

while "Pastrami sandwich" in sandwich_orders :
    sandwich_orders.remove("Pastrami sandwich")

print(sandwich_orders)

sandwich_orders_two = sandwich_orders[:] #copie

finished_sandwiches = []

for sandwich in sandwich_orders_two :
    finished_sandwiches.append(sandwich)
    sandwich_orders.remove(sandwich)