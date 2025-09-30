

def safe_divide(numerator, denominator):
    try:
        """ numerator = int(input("Enter your numerator: "))
        denominator = int(input("Enter your denominator: ")) """
        num = float(numerator)
        den = float(denominator)
        result = num/den
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("Error: Please enter numeric values only.")
        return None
    
    else:
        print(f"The result of the division is {result}")