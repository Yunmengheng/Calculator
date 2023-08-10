print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")
operation = input("select an operation to perform: ")
if operation == "1":
    num1 = input("Enter the first number ")
    num2 = input("Enter the second number ")
    print("The answer is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter the first number ")
    num2 = input("Enter the second number ")
    print("The answer is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter the first number ")
    num2 = input("Enter the second number ")
    print("The answer is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter the first number ")
    num2 = input("Enter the second number 1")
    print("The answer is " + str(int(num1) / int(num2)))
    print(" Invalid Entry")
