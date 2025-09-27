# arithmetic_operations.py

DIV_ZERO_MSG = "Error: Division by zero is not allowed."
INVALID_OP_MSG = "Error: Invalid operation."

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform a basic arithmetic operation between two numbers.
    """
    op = (operation or "").strip().lower()

    if op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2
    elif op == "multiply":
        return num1 * num2
    elif op == "divide":
        if num2 == 0:
            return DIV_ZERO_MSG
        return num1 / num2
    else:
        return INVALID_OP_MSG
