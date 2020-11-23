# METHOD 1:
X = [[12,7], [4 ,5], [3 ,8]]
result = [[0,0,0], [0,0,0]]
# iterate through rows
for i in range(len(X)):
   # iterate through columns
   for j in range(len(X[0])):
       result[j][i] = X[i][j]

# Or use this: result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
print("Matrix:")
for r in X:
   print(r)
print("Transpose of Matrix:")
for r in result:
   print(r)