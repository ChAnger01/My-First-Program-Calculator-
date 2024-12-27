def output_add(num1, num2):
  return int(num1 + num2)

def output_sub(num1, num2):
  return int(num1 - num2)

def output_mul(num1, num2):
  return int(num1 * num2)

def output_div(num1, num2):
  return int(num1 / num2)


while True:
  method = input("""
  Please choose an operation:
    1. Add (1)
    2. Subtract (2)
    3. Multiply (3)
    4. Divide (4)
    Type 'stop' to quit the calculator: 
  """)
  if method not in ["1","2","3","4","exit"]:
   print("Please enter a valid number")
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  #add
  if method == "1":
    print(num1, "+", num2, "=", output_add(num1, num2))

  #sub
  elif method == "2":
    print(num1, "-", num2, "=", output_sub(num1, num2))

  #mul
  elif method == "3":
    print(num1, "*", num2, "=", output_mul(num1, num2))

  #div
  elif method == "4":
    print(num1, "/", num2, "=", output_div(num1, num2))

  #special
  elif method == "stop":
    break



