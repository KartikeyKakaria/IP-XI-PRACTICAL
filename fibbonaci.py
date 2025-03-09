# Print the fibonacci series till a fixed point
limit = int(input("Enter the limit of the fibonacci series: "));

fibonacci = [1];

for i in range(1, limit):
    if i <= 1:
        fibonacci.append(1);
        print("1")
    else:
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2]);
    print(fibonacci[-1])