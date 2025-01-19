def function_with_alternative_error_handling(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = float('nan')  # Using NaN (Not a Number) for undefined results
        print("Error: Division by zero. Returning NaN.")
    return result

result = function_with_alternative_error_handling(10, 0)
print(result)  # Output: nan

result = function_with_alternative_error_handling(0, 5)
print(result)  # Output: 0.0

result = function_with_alternative_error_handling(10, 5)
print(result)  # Output: 2.0