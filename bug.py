def function_with_uncommon_error(a, b):
    if a == 0:
        return 0  # Correct handling of a zero
    elif b == 0:
        return float('inf') # Uncommon error, but correct way to handle divide by zero
    else:
        return a / b

result = function_with_uncommon_error(10, 0)
print(result)  # Output: inf

result = function_with_uncommon_error(0, 5)
print(result)  # Output: 0

result = function_with_uncommon_error(10,5)
print(result) # Output: 2.0