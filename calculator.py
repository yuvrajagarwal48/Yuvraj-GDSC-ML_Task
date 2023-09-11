import math

def calculate_expression(expression):
    try:
        # Replace '^' with '**' for exponentiation
        expression = expression.replace('^', '**')        

        result = eval(expression)
        
        if isinstance(result, float):
            result = round(result, 2)
        
        return result
    except (SyntaxError, ZeroDivisionError) as e:
        return f"Error:(3*) {str(e)}"
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"


while True:
    user_input = input("Enter an expression (or 'quit' to exit): ")
    
    if user_input.lower() == 'quit':
        break
    
    result = calculate_expression(user_input)
    print(f"Result: {result}")
