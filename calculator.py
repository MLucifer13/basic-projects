def main():
    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Exit")
    print("Choose the operator:")

    while True:
        choice = int(input("Enter your choice: "))
        if choice == 6:
            break
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if choice == 1:
            print(f"a + b = {addition(a, b)}")
        elif choice == 2:
            print(f"a - b = {subtraction(a, b)}")
        elif choice == 3:
            print(f"a * b = {multiplication(a, b)}")
        elif choice == 4:
            print(f"a / b = {division(a, b)}")
        elif choice == 5:
            print(f"a ** b = {power(a, b)}")
        
        

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        print("Cannot divide by zero")

def power(a,b):
    return a**b

if __name__ == "__main__":
    main()