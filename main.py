def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def square(x, y):
    return x ** y

print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiply")
print("4. Divide")
print("5. Square root")

while True:
    choice = input("Enter a choice now: ")

    if choice in ('1', '2', '3', '4', '5'):
        num1 = float(input("Enter 1st number: "))
        num2 = float(input("Enter 2nd number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "/", num2, "=", square(num1, num2))
            
        next_calculation = input("Another calculation")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid input")