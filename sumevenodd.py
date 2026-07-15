def sum_even_odd(numbers):
    even_sum = 0
    odd_sum = 0
    for j in numbers:
        if j % 2 == 0:
            even_sum += j
        else:
            odd_sum += j
    return (even_sum, odd_sum)      
numbers=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even_sum, odd_sum = sum_even_odd(numbers)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

