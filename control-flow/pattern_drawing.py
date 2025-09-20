# pattern_drawing.py

# Prompt the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop to control rows
while row < size:
    # For loop to print asterisks in each row
    for col in range(size):
        print("*", end="")
    # Move to the next line after each row
    print()
    row += 1