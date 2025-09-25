def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform arithmetic operation on two numbers.

    Parameters:
        num1 (float): First number
        num2 (float): Second number
        operation (str): 'add', 'subtract', 'multiply', 'divide'

    Returns:
        float or str: Result of the operation, or error message for invalid inputs.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error: Division by zero"  # You can handle this in main.py
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation"