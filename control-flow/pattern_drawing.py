# pattern_drawing.py
# Objective: Draw a square pattern using while and nested for loops

# Prompt the user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use while loop to iterate through rows
while row < size:
    # Use for loop to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
