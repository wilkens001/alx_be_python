def perform_operation(num1, num2, operation):
    """
    Performs arithmetic operations on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float: Result of the operation
        str: Error message in case of division by zero
    """
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            # Handle division by zero
            if num2 == 0:
                return "elif"
            return num1 / num2
        case _:
            return "Error: Invalid operation"