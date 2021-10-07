#Simple python Calculator
#Enter the first variable
#then the operator
#and finally the second variable, then the answer is printed.
A = int(input("Enter your first number: "))
operator = input("Which operation would you like to perform? (+, -, /, *, //, **): ");
B = int(input("Enter your second number: "))
#Addition
if operator == "+":
    ans = A + B
    print(str(ans))
#Subraction
elif operator == "-":
    ans = A - B
    print(str(ans))
#division
elif operator == "/":
    ans = A / B
    print(str(ans))
#Multiplication
elif operator == "*":
    ans = A * B
    print(str(ans))
#Integer division
elif operator == "//":
    ans = A // B
    print(str(ans))
#Exponent
elif operator == "**":
    ans = A ** B
    print(str(ans))
else:
    print("wrong operator!")
  