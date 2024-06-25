# Define the variable x and assign it a value

x = 2  

# Define the coefficients for the polynomial ax^3 + bx^2 + cx + d
a = 1  
b = -2  
c = 3   
d = -4 

# Evaluate the polynomial for the given value of x

polynomial_value = a*x**3 + b*x**2 + c*x + d

# Calculate the first derivative: 3ax^2 + 2bx + c

first_derivative = 3*a*x**2 + 2*b*x + c

# Calculate the second derivative: 6ax + 2b

second_derivative = 6*a*x + 2*b

# Print the results
print("Value of the polynomial at x =", x, "is:", polynomial_value)
print("Value of the first derivative at x =", x, "is:", first_derivative)
print("Value of the second derivative at x =", x, "is:", second_derivative)
