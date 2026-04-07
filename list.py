numbers = [10, 4, 7, 2, 5, 90, 1, 1, 56, 23]

try:
    x = int(input("Enter a number: "))

    if x in numbers:
        print(f"Yes, {x} is in the list.")
    else:
        print(f"No, {x} is not in the list.")

except ValueError:
    print("Please enter a valid integer.")
