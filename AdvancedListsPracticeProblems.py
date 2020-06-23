# Tien Phan
# Advanced Lists Practice Problems

def newLine():
    return print("\n")

def divider():
    return print("\n########################################################################")

print("Problem # 1 - Every Three Numbers")

# Create a function called every_three_nums that has one parameter named start.
#
# The function should return a list of every third number between start and
# 100 (inclusive). For example, every_three_nums(91) should return the list [91, 94, 97, 100].
# If start is greater than 100, the function should return an empty list.

# Write your function here
def every_three_nums(start):
    my_list = range(start, 101, 3)

    if start > 100:
        return []
    else:
        return list(my_list)
# Uncomment the line below when your function is done
print(every_three_nums(91))
print(every_three_nums(100))
divider()

print("Problem # 2 - Remove Middle")

# Create a function named remove_middle which has three parameters named lst, start, and end.
#
# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
#
# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:
# remove_middle([4, 8 , 15, 16, 23, 42], 1, 3)

# Write your function here
def remove_middle(lst, start, end):
    firstList = lst[:start]
    secondList = lst[end+1:]
    my_list = firstList + secondList
    return my_list

# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))
divider()

print("Problem # 3 - More Frequent Item")

# Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
#
# Return either item1 or item2 depending on which item appears more often in lst.
#
# If the two items appear the same number of times, return item1.

# Write your function here
def more_frequent_item(lst, item1, item2):
    firstItem = lst.count(item1)
    secondItem = lst.count(item2)

    if firstItem == secondItem:
        return item1
    elif(firstItem > secondItem) or (secondItem > firstItem):
        if firstItem > secondItem:
            return item1
        else:
            return item2

# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
divider()

print("Problem # 4 - Double Index")

# Create a function named double_index that has two parameters: a list named lst and a single number named index.
#
# The function should return a new list where all elements are the same as in lst except for the element at index.
# The element at index should be double the value of the element at index of the original lst.
#
# If index is not a valid index, the function should return the original list.
# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:
# double_index([1, 2, 3, 4], 2)
#
# After writing your function, un-comment the call to the function that we’ve provided for you to test your results.

#Write your function here

def double_index(lst, index):
    length_of_list = len(lst)
    if (index < 0 or index >= length_of_list):
        return lst
    else:
        number = lst[index]
        number = number * 2
        newList = lst

        newList[index] = number
        return newList

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
divider()

print("Problem # 5 - Middle Item")

# Create a function called middle_element that has one parameter named lst.
#
# If there are an odd number of elements in lst, the function should return the middle element.
# If there are an even number of elements, the function should return the average of the middle two elements.

# Write your function here
def middle_element(lst):
    size = len(lst)
    half_size = size//2
    if size % 2 == 0:
        average = (lst[half_size] + lst[half_size-1])//2
        return average
    else:
        return lst[half_size]


# Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))
