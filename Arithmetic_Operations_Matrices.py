# 2D array
# Situation --> Arithmetic operations on matrices

print("\"2D Array\"")
print("Note: It contains horizontal and vertical values")
print()

print("Enter number of rows : ", end=" ")
row = int(input())
print("Enter number of coloumns : ", end=" ")
col = int(input())
print()

# Creating a 2D array (list of lists)
matrix_1 = []
matrix_2 = []

print("\"Provide values for 1st matrix\"")
for i in range(row):
  r = []
  for j in range(col):
    print(f"Element at index [{i}][{j}] : ", end=" ")
    element = int(float(input()))
    r.append(element)
    matrix_1.append(r)

    print()

print("\"Provide values for 2nd matrix\"")
for i in range(row):
  r2 = []
  for j in range(col):
    print(f"Element at index [{i}][{j}] : ", end=" ")
    element = int(float(input()))
    r2.append(element)
    matrix_2.append(r2)

   print()


# User provided 2D lists --> Print values
print("\" The 1st matrix you entered\"")
for i in range(row):
    print()
    print("  |", end=" ")
    for j in range(col):
        print("",matrix_1[i][j], end=" ")

    print("|", end=" ")

print()
print()
print("\" The 2nd matrix you entered\"")
for i in range(row):
    print()
    print("  |", end=" ")
    for j in range(col):
        print("",matrix_2[i][j], end=" ")

    print("|", end=" ")

print()
# Addition of matrices
# Calculation
print()
print("\"Addition of the 2 matrices\"")
result = []
for i in range(row):
    r3 = []
    for j in range(col):
        sum = matrix_1[i][j] + matrix_2[i][j]     # From here any arithmetic operation can be performed
        r3.append(sum)
        result.append(r3) 

# Result --> Print      
for i in range(row):
    print()
    print("  |", end=" ")
    for j in range(col):
        print("",result[i][j], end=" ")

    print("|", end=" ")


# Index presenting for each matrix
# Matrix 1
print()
print()
print("\"Indices for \'Matrix 1\'\"")
for i in range(row):
    for j in range(col):
        print(f"Element at index [{i}][{j}] : {matrix_1[i][j]}")

print()

# Matrix 2
print("\"Indices for \'Matrix 2\'\"")
for i in range(row):
    for j in range(col):
        print(f"Element at index [{i}][{j}] : {matrix_2[i][j]}")

print()  

# Resultant matrix
print("\"Resultant matrix\"")
for i in range(row):
    for j in range(col):
        print(f"Element at index [{i}][{j}] : {result[i][j]}")
