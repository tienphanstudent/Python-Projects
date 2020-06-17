# Tien Phan
# Python Function Practice

# defined variable definitions
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1
c = 3*10**8

# function that accepts a fahrenheit temperature and converts it to celsius 
def f_to_c(f_temp):
  c_temp = (f_temp - 32) * 5/9
  return c_temp

# tester to check if f to c function works properly
f100_in_celsius = f_to_c(100)
print("Fahrenheit to Celsius: " + str(f100_in_celsius))

# function that accepts a celsius temperature and converts it to fahrenheit
def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

# tester to check if c to f function works properly
c0_in_fahrenheit = c_to_f(0)
print("Celsius to Fahrenheit: " + str(c0_in_fahrenheit))

# function that utilizes f = ma
def get_force(mass, acceleration):
  return mass * acceleration

# tester to check if force equation function works properly
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

# another function that calculates energy using the equation mass times constant
def get_energy(mass, c):
  return mass * c

# tester to check if energy equation function works properly
bomb_energy = get_energy(bomb_mass, c)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

# function that calculates work 
def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return force * distance

# tester to check if work equation function works properly
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")
