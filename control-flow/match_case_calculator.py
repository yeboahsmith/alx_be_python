
num1 = input("Enter the first number:")
num2 = input("Enter the second number:")

operation = input("Choose the operation (+, -, *, /):") 

match operation:
    case " + ":
      print( "the results is " + num1 + num2)
    case " -":
      print("the results is " + num1 - num2)
     case " * ":
       print("the results is " + num1 * num2)
    case  " / ":
      print("the results is " + num1 / num2):
     case "/":
        if num2 != 0:
            print("The result is", num1 / num2)
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation.")
      
