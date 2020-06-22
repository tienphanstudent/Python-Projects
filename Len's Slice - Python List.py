# Tien Phan
# Len's Slice - Python List Practice

# definitions

def newLine():
  return print("\n")

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

# store length of list toppings into variable
num_pizzas = len(toppings)

# tester for length variable
print("We sell " + str(num_pizzas) + " different kinds of pizza!\n")

# tester to combine two lists of prices and toppings
pizzas = list(zip(prices, toppings))
print(pizzas)
newLine()

# tester for sort of pizzas list
pizzas.sort()
print(pizzas)
newLine()

# tester to save first item in pizza in variable
cheapest_pizza = pizzas[0]
print(cheapest_pizza)
newLine()

# tester to save last item in pizza in variable
priciest_pizza = pizzas[-1]
print(priciest_pizza)
newLine()

three_cheapest = pizzas[:3]
print(three_cheapest)
newLine()

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)