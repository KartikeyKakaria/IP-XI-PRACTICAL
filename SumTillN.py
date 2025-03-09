#find the sum till n numbers

n = int(input("Enter the limit: "));
sum = 0;

for i in range(1, n+1):
    sum += i

print("The sum of first", n, "natural numbers is", sum);

