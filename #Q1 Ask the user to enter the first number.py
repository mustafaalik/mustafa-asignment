# Ask the user to enter the first number
first_number = float(input("Enter the first number: "))

# Ask the user to enter the second number
second_number = float(input("Enter the second number: "))

# Calculate the average using the formula average = (sum of numbers) / 2
average = (first_number + second_number) / 2

# Display the average with two decimal places using string formatting
print("The average of the two numbers is: {:.2f}".format(average))