def chaos(k, x, n):
    for i in range(n):
        x = k * x * (1 - x)
        print(x)


k = float(input("Enter the value of k: "))
x = float(input("Enter the value of x (between 0 and 1): "))
n = int(input("Enter the number of iterations: "))

if x < 0 or x > 1:
    print("Error: x must be between 0 and 1.")
else:
    chaos(k, x, n)