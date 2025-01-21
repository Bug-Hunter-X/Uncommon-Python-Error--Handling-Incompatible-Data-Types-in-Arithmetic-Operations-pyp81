def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except TypeError:
        return "TypeError: Unsupported operand type(s) for /: 'str' and 'int'"
    except ZeroDivisionError:
        return "ZeroDivisionError: division by zero"
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    return result

print(function_with_uncommon_error(10, 0))  # ZeroDivisionError
print(function_with_uncommon_error(10, 'a'))  # TypeError
print(function_with_uncommon_error(10, 2))  # 5.0
print(function_with_uncommon_error([1,2],2)) # TypeError