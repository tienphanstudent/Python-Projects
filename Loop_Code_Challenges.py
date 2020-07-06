# Tien Phan
# Loop Code Challange Problems

def newLine():
    return print("\n")

def divider():
    return print("\n########################################################################")

def header(num, title):
    return print("Problem # " + str(num) + " - " + title)

# Problem # 1 - Divisible by 10
header(1, "Divisible by 10")
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
#
# Return the count of how many numbers in the list are divisible by 10.

# Write your function here
def divisible_by_ten(nums):
    count = 0
    for i in nums:
        if i % 10 == 0:
            count += 1
        else:
            continue
    return count

# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))
divider()

# Problem # 2 - Greetings
header(2, "Greetings")
# Create a function named add_greetings() which takes a list of strings named names as a parameter.
#
# In the function, create an empty list that will contain each greeting. Add the string "Hello, "
# in front of each name in names and append the greeting to the list.
#
# Return the new list containing the greetings.

# Write your function here
def add_greetings(names):
    lst = ["Hello, " + greeting for greeting in names]
    return lst

# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))
divider()

# Problem # 3 - Delete Starting Even Numbers
header(3, "Delete Starting Even Numbers")

# Write a function called delete_starting_evens() that has a parameter named lst.
#
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
#
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
#
# Make sure your function works even if every element in the list is even!

# Write your function here
def delete_starting_evens(lst):
    for i in lst:
        if i % 2 != 0:
            return lst
        else:
            lst = lst[1:]
    return lst
# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
divider()

# Problem # 4 - Odd Indices
header(4, "Odd Indices")

# Create a function named odd_indices() that has one parameter named lst.
#
# The function should create a new empty list and add every element from lst that has an odd index.
# The function should then return this new list.
#
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

# Write your function here
def odd_indices(lst):
    newList = []

    for i in range(1, len(lst), 2):
        newList.append(lst[i])
    return newList


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))
divider()

# Problem # 5 - Exponents
header(5, "Exponents")

# Create a function named exponents() that takes two lists as parameters named bases and powers.
# Return a new list containing every number in bases raised to every number in powers.
#
# For example, consider the following code.
# exponents([2, 3, 4], [1, 2, 3])
#
# the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first.
# Then two to the second. Then two to the third, and so on.

# Write your function here
def exponents(bases, powers):
  newList = []
  for i in bases:
    for j in powers:
      newList.append(i**j)
  return newList

# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))
divider()

# Problem # 6 - Larger Sum
header(6, "Larger Sum")

# Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
#
# The function should return the list whose elements sum to the greater number.
# If the sum of the elements of each list are equal, return lst1.

# Write your function here
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0

  for i in lst1:
    for j in lst2:
      sum1 += i
      sum2 += j

  if sum1 > sum2:
    return lst1
  elif sum2 > sum1:
    return lst2
  elif sum1 == sum2:
    return lst1


# Uncomment the line below when your function is done
print(larger_sum([1, 9, 5], [2, 3, 7]))
divider()

# Problem # 7 - Over 9000
header(7, "Over 9000")

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
#
# The function should sum the elements of the list until the sum is greater than 9000. When this happens,
# the function should return the sum. If the sum of all of the elements is never greater than 9000,
# the function should return total sum of all the elements. If the list is empty, the function should return 0.
#
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

# Write your function here
def over_nine_thousand(lst):
  sum = 0

  if lst == []:
    return 0

  for i in lst:
    if sum < 9000:
      sum += i
    elif sum > 9000:
      return sum

  return sum
# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))
divider()

# Problem # 8 - Max Num
header(8, "Max Num")

# Create a function named max_num() that takes a list of numbers named nums as a parameter.
#
# The function should return the largest number in nums

# Write your function here
def max_num(nums):
    max_number = nums[0]

    for i in nums:
        if i > max_number:
            max_number = i
    return max_number

# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))
divider()

# Problem # 9 - Same Values
header(9, "Same Values")

# Write a function named same_values() that takes two lists of numbers of equal size as parameters.
#
# The function should return a list of the indices where the values were equal in lst1 and lst2.
#
# For example, the following code should return [0, 2, 3]
# same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

# Write your function here
def same_values(lst1, lst2):
    new_list = []
    count = 0
    number = 0
    if len(lst1) == len(lst2):
        for i in lst1:
            number = lst2[count]
            if i == number:
                new_list.append(count)
                count += 1
            else:
                count += 1
                continue
    else:
        return ("Lists are not equal")

    return new_list
# Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
divider()

# Problem # 10 - Reversed List
header(10, "Reversed List")
# Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
#
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
#
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

# Write your function here
def reversed_list(lst1, lst2):
    new_list = []
    placeholder = 0
    count = 0
    counter = 0
    if len(lst1) == len(lst2):
        for i in lst2:
            placeholder = lst2[-1 - count]
            new_list.append(placeholder)
            count += 1
        for j in lst1:
            if lst1[counter] == new_list[counter]:
                counter += 1
                continue
            else:
                return False

        return True
    else:
        return ("Lists are not equal")

# Uncomment the lines below when your function is done

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))