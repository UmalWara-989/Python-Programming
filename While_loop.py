# While loop
print("\"Situation 1\"")
print("Enter \'1\' to start program : ", end=" ")
choice = input()
print()

count_Even = 0
count_Odd = 0

while choice == "1":
  print("Note: I will tell you weather, you entered an even or an odd value!")
  print("Enter any number : ", end=" ")
  num = int(input())
  if num % 2 == 0:
  print(f"The number \'{num}\' is an \"Even number\"!")
  print()
  count_Even += 1
  else:
  print(f"The number \'{num}\' is an \"Odd number\"!")
  print()
  count_Odd += 1
  print("Note: 1-->yes, 0-->no")    
  print("Do you want to continue? (yes/no)")
  choice = input()
  print()

  if choice == "0":
  print("The total \"Even numbers\" you entered is : \'",count_Even,"\'")
  print("The total \"Odd numbers\" you entered is : \'",count_Odd,"\'")
  print()
  print("\"Exiting\" the program!")
  break
