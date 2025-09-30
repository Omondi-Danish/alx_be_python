

def safe_divide(numerator, denominator):
    try:
        """ numerator = int(input("Enter your numerator: "))
        denominator = int(input("Enter your denominator: ")) """
        num = float(numerator)
        den = float(denominator)
        
        return num/den
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
    except ValueError:
        print("Error: Please enter a numeric value")
        return None
    finally:
        print("Division attempt complete")