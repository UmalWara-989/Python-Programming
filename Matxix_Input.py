# 2D Array

print("\"2D Array\"")
print("Note: It contains rows and coloumns")
print()
print("Enter number of rows : ", end=" ")
rows = int(input())
print("Enter number of coloumns : ", end=" ")
coloumns = int(input())
print()

# Creating a 2D array (list of lists)
arr = []
print("\"Provide values for 2D array\"")
for i in range(rows):
  row = []
  for j in range(coloumns):
      print(f"Element at index [{i}][{j}] : ", end=" ")
      element = int(float(input()))
      row.append(element)
      arr.append(row)

print()
# Print 2D array in matrix form
print("\"Provided 2D list\"", end=" ")
for i in range(rows):
    print()
    print("  |", end=" ")
    for j in range(coloumns):
        print("",arr[i][j], end=" ")

    print("|", end=" ")  


print()
print()
# Print 2D array in index form
print("\"Matrix in index form\"")
for i in range(rows):  
  for j in range(coloumns):
    print(f"Element at index [{i}][{j}] : {arr[i][j]}")

print()
print()        

