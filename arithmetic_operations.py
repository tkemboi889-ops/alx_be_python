
def perform_operation(num1, num2, operation):

    if operation == "add":
        result= num1 + num2
        return result
    elif operation == "subtract":
        result= num1 - num2
        return result
    elif operation == "multiply":
        result= num1 * num2
        return result
    elif operation == "divide":
        if num2 == 0:
            print( "Error: Division by zero")
        else:
            return num1 / num2
    return result