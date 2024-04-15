import math


def is_even(k):
    if k&1 == 0:
        return True
    else:
        return False

print(is_even(1239879877))

def minmax(data):
    min = data[0]
    max = data[0]

    for i in data:
        if i > max:
            max = i

    for i in data:
        if i < min:
            min = i

    return min, max

numbers = [1,2,3,4,5,6,7,8,9]

print(minmax(numbers))

def sum_of_squares(n):
    positive_int_lower_n = []
    for i in range(0, n, 2):
        positive_int_lower_n.append(i)
    sum_of_squares = 0
    for i in positive_int_lower_n:
        sum_of_squares = sum_of_squares + math.sqrt(i)
    return sum_of_squares

print(sum_of_squares(12))

def number_of_devides(n):
    counter = 0
    while n>= 2:
        n = n / 2
        counter = counter + 1
    return counter

print(number_of_devides(16))