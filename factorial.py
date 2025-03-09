# Calculate the value of n!
n = int(input("Enter the value: "));

factorial = 1;

# Calculate the factorial  
for i in range(1, n + 1):  
        factorial = factorial * i;

print("The factorial of", n, "is", factorial);