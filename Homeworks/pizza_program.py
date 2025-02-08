# Simple program using "while", "for" and "if" statements


# Create a list of pizzas
pizzas = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

# Create a list of prices
prices = [2, 6, 1, 3, 2, 7, 2]


# Print the pizza and its price, if the price is greater than $3 print "too expensive" 
print("Pizzas and prices:")
for pizza, price in zip(pizzas, prices):
    if price > 3:
        print(f"{pizza.title()} pizza is ${price}. Too expensive!")
    else:
        print(f"{pizza.title()} pizza is ${price}.")
print()

# Removing the pizzas that are too expensive (greater than $3)
while True:
    for price in prices:
        if price > 3:
            index = prices.index(price)
            prices.pop(index)
            removed_pizza = pizzas.pop(index)
            print(f"{removed_pizza.title()} pizza was removed from the list.")
            break
    else:
        break

