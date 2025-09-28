# arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation.

    Parameters:
        num1 (float): first number
        num2 (float): second number
        operation (str): 'add', 'subtract', 'multiply', or 'divide'

    Returns:
        float or str: result of the operation, or an error message string
                      (e.g., for division by zero or invalid operation)
    """
    # Normalize operation string so input is flexible
    operation = operation.strip().lower()

    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        # Handle division by zero in a clear way that main.py can print
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
