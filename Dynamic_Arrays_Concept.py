print("\"Situation 2\"")
# Taking size of the array
print("Enter number of employees that are applied for the scholarship : ", end=" ")
size = int(input())
print()

# Declaring array
names = []
age = []
timing = []

# Counting approved or rejected application
count_approved = 0
count_regected = 0

print("\"Employees Information\"")
# Using "for loop" for continuously user interaction 
for i in range(size):
  print("\'Candidate",i+1,"\'")
  print("Enter name at index [",i,"] : ", end=" ")
  names.append(input())
  print("Enter age at index [",i,"] : ", end=" ")
  age.append(int(input()))
  print("Enter timing at index [",i,"] : ", end=" ")
  timing.append(input())
  if names[i] == "Umal" and age[i] > 18 or timing[i] == "perfect":
  print()
  print(f"Congratulations! {names[i]} You are eligible for the scholarship!")
  count_approved += 1
  print()
  else:
  print()
  print(f"Sorry! {names[i]} You are not eligible for the scholarship!")
  count_regected += 1
  print()

print()
print()
print("\"The candidates applied for the scholarship\"")     
print("Names : ", names)
print("Age : ", age)
print("Timing : ", timing) 
print()  
print("Number of approved applications : ", count_approved)
print("Number of rejected applications : ", count_regected)
