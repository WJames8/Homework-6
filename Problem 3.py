age = int(input("Please enter your age: "))

if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 65:
    print("Adult")
elif age <= 100:
    print("Senior")
else:
    print("Congrats on appearing on the Smucker's jar!")