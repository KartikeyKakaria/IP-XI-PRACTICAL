# Check if a number is odd or even
num = int(input("Enter a number: "));

# Check if the number is positive or negative

if num >= 0:
    if num % 2 == 0:
        print(num, "is an even number.")
    else:
        print(num, "is an odd number.")
else:
    print(num, "is a negative number.")
