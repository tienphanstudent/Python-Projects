# Tien Phan
# Python Lists Practice Problems

def newLine():
    return print("\n")

def divider():
    return print("\n########################################################################")

print("Problem # 1 - Append Sum")

# Write a function named append_sum that has one parameter — a list named named lst.
#
# The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

# Write your function here
def append_sum(lst):
    listSum = (lst[-2] + lst[-1])
    lst.append(listSum)
    listSum = lst[-2] + lst[-1]
    lst.append(listSum)
    listSum = lst[-2] + lst[-1]
    lst.append(listSum)

    return lst

# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

divider()

print("Problem # 2 - Larger List")

# Write a function named larger_list that has two parameters named lst1 and lst2.
#
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

# Write your function here

def larger_list(lst1, lst2):
#    if lst1.count(lst1) == lst2.count(lst2):
#        return lst1[-1]
#    elif (lst1.count(lst1) > lst2.count(lst2)) or (lst2.count(lst2) > lst1.count(lst1)):
#        if lst1.count(lst1) > lst2.count(lst2):
#            return lst1[-1]
#        else:
#            return lst2[-1]

    list1Size = len(lst1)
    list2Size = len(lst2)

    if list1Size == list2Size:
        return lst1[-1]
    elif (list1Size > list2Size) or (list2Size > list1Size):
        if list1Size > list2Size:
            return lst1[-1]
        else:
            return lst2[-1]

# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

divider()
print("Problem # 3 - More than N")

# Create a function named more_than_n that has three parameters named lst, item, and n.
#
# The function should return True if item appears in the list more than n times. The function should return False otherwise.

# Write your function here
def more_than_n(lst, item, n):
    item = lst.count(item)
    if item > n:
        return True
    else:
        return False

# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

divider()
print("Problem # 4 - Append Size")

# Create a function called append_size that has one parameter named lst.
#
# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.
#
# For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.

# Write your function here

def append_size(lst):
    placeholder = len(lst)
    lst.append(placeholder)
    return lst

# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

divider()
print("Problem # 5 - Combine Sort")

# Write a function named combine_sort that has two parameters named lst1 and lst2.
#
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

# Write your function here

def combine_sort(lst1, lst2):
    combineList = lst1 + lst2
    combineList.sort()
    return combineList

# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))