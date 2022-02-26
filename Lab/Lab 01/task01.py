import numpy as np

def count(x, y, matrix, visit):

  if (not ((len(matrix)) > x >= 0)) or not (((len(matrix[0])) > y >= 0)) or (matrix[x][y] == "N") or (visit[x][y] != 0):
    return 0

  if visit[x][y] != 1:
    matrix[x][y] = "N"
    visit[x][y]=1
    c = 1

    for x1 in range(x-1, x+2):
      for y1 in range(y-1, y+2):
          if not x == x1 or not y == y1:
              c += count(x1, y1, matrix, visit)
    return c

def infected_person(filename):

  f = open(filename, "r")
  matrix = []
  infected = 0

  for i in f.readlines():
    temp=[]
    for j in i:
      if j == "Y" or j == "N":
        temp.append(j)
    matrix.append(temp)
    
  matrix = np.array(matrix)
  row = matrix.shape[0]
  column = matrix.shape[1]
  visit = np.zeros((row,column))

  # a = x, b = y
  for a in range(row):
    for b in range(column):
        infected = max(infected, count(a, b, matrix, visit))
  print(infected)

print("Sample input 1:")
infected_person("input.txt")
print("Sample input 2:")
infected_person("input 2.txt")
