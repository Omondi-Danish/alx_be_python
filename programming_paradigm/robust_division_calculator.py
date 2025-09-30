

def safe_divide(numerator, denominator):
    try:
        """ numerator = int(input("Enter your numerator: "))
        denominator = int(input("Enter your denominator: ")) """
        num = float(numerator)
        den = float(denominator)
        result = num/den
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
    
    else:
        print(f"The result of the division is {result}")