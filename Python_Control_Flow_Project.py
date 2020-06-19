# Tien Phan
# Python Control Flow Project

# defined global variable
premium_shipping = 125.00

# function that accepts a ground package weight and calculates the cost of shipping
def ground_shipping_cost(weight):
  if weight <= 2:
    cost = 20.00 + (1.50 * weight)
    return cost
  elif weight > 2 and weight <= 6:
    cost = 20.00 + (3.00 * weight)
    return cost
  elif weight > 6 and weight <= 10:
    cost = 20.00 + (4.00 * weight)
    return cost
  elif weight > 10:
    cost = 20.00 + (4.75 * weight)
    return cost

# function that accepts a drone package weight and calculates the cost of shipping
def drone_shipping_cost(weight):
  if weight <= 2:
    cost = 4.50 * weight
    return cost
  elif weight > 2 and weight <= 6:
    cost = 9.00 * weight
    return cost
  elif weight > 6 and weight <= 10:
    cost = 12.00 * weight
    return cost
  elif weight > 10:
    cost = 14.25 * weight
    return cost

# function that accepts weight and calculates the cheapest shipping cost
def cheapest_shipping_cost(weight):
  if ground_shipping_cost(weight) < drone_shipping_cost(weight) and ground_shipping_cost(weight) < premium_shipping:
    return print("Ground shipping would be the cheapest option for you and it would cost: " + str(ground_shipping_cost(weight)))
  elif drone_shipping_cost(weight) < ground_shipping_cost(weight) and drone_shipping_cost(weight) < premium_shipping:
    return print("Drone shipping would be the cheapest option for you and it would cost: " + str(drone_shipping_cost(weight)))
  else:
    return print("Premium shipping would be the cheapest option for you and it would cost: " + str(premium_shipping))

# tester for ground shipping cost function
print("The price for ground shipping is: " + str(ground_shipping_cost(8.4)) + "\n")

# tester for drone shipping cost function
print("The price for drone shipping is: " + str(drone_shipping_cost(1.5)) + "\n")

# tester for cheapest shipping cost function
cheapest_shipping_cost(4.8)
cheapest_shipping_cost(41.5)