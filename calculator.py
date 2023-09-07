import math

def calculate_expression(expression):
    try:
        # Replace '^' with '**' for exponentiation
        expression = expression.replace('^', '**')
        
        # Evaluate the expression
        result = eval(expression)
        
        # Check if the result is a float and round it to 2 decimal places if necessary
        if isinstance(result, float):
            result = round(result, 2)
        
        return result
    except (SyntaxError, ZeroDivisionError) as e:
        return f"Error:(3*) {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    while True:
        user_input = input("Enter an expression (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            break
        
        result = calculate_expression(user_input)
        print(f"Result: {result}")
