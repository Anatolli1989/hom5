# import random
#
# # Create a list of 10 random integers ranging from -50 до 50
# random_numbers = [random.randint(-50, 50) for _ in range(10)]
#
# sum_negative = sum(x for x in random_numbers if x < 0)
#
# sum_even = sum(x for x in random_numbers if x % 2 == 0)
#
# sum_odd = sum(x for x in random_numbers if x % 2 != 0)
#
# product_index3 = 1
# for i in range(0, len(random_numbers), 3):
#     product_index3 *= random_numbers[i]
#
# min_index = random_numbers.index(min(random_numbers))
# max_index = random_numbers.index(max(random_numbers))
# product_between_min_max = 1
# if min_index < max_index:
#     product_between_min_max = 1
#     for i in range(min_index + 1, max_index):
#         product_between_min_max *= random_numbers[i]
#
# positive_indices = [i for i, x in enumerate(random_numbers) if x > 0]
# if len(positive_indices) >= 2:
#     sum_between_positive = sum(random_numbers[positive_indices[0]+1:positive_indices[-1]])
# else:
#     sum_between_positive = 0
#
# print("List of random numbers:", random_numbers)
# print("Sum of negative numbers:", sum_negative)
# print("Sum of even numbers:", sum_even)
# print("Sum of odd numbers:", sum_odd)
# print("Product of elements with multiples of indexes 3:", product_index3)
# print("Product of elements between the minimum and maximum elements:", product_between_min_max)
# print("Sum of elements between the first and last positive elements:", sum_between_positive)

#2

# import random
#
# random_numbers = [random.randint(-20, 30) for _ in range(10)]
#
# even_numbers = [x for x in random_numbers if x % 2 == 0]
#
# odd_numbers = [x for x in random_numbers if x % 2 != 0]
#
# negative_numbers = [x for x in random_numbers if x < 0]
#
# positive_numbers = [x for x in random_numbers if x > 0]
#
# print("List of random numbers:", random_numbers)
# print("List of even numbers:", even_numbers)
# print("List of odd numbers:", odd_numbers)
# print("List of negative numbers:", negative_numbers)
# print("List of positive numbers:", positive_numbers)