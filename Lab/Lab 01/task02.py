import numpy as np, collections as coll

def human(x, y, matrix):
    c = 0
    for i in range(x):
        for j in range(y):
            if matrix[i][j] == "H":
                c += 1
    return c


def time(row, column, matrix, visit, attack, human, alien):
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while alien:
        x1, y1, attack = alien.popleft()
        visit[x1][y1] = 1
        for x, y in direction:
            if (0 <= x1+x < row) and (0 <= y1+y < column) and (matrix[x1+x][y1+y] == "H") and (visit[x1][y1] == 1):
                visit[x1+x][y1+y] = 1
                matrix[x1+x][y1+y] = "A"
                human.remove((x1+x, y1+y))
                alien.append([x1+x, y1+y, attack+1])
    return attack


def position(x, y, matrix, visit):
    human = []
    alien = coll.deque()
    attack = 0
    for x1 in range(x):
        for y1 in range(y):
            if matrix[x1][y1] == "A":
                alien.append([x1, y1, attack])
            if matrix[x1][y1] == "H":
                human.append((x1, y1))  
    return time(x, y, matrix, visit, attack, human, alien)


def apocalypse(filename):
    f = open(filename, "r")
    r = f.read(4)
    row = int(r[0])
    column = int(r[2])
    matrix = []
    
    for i in f.readlines():
        temp = []
        if not i == row and not i == column:
            for j in i:
                if j == "A" or j == "H" or j == "T":
                    temp.append(j)
            matrix.append(temp)

    matrix = np.array(matrix)
    visit = np.zeros((row, column))
    print("Time:", position(row, column, matrix, visit), "minutes")

    if human(row, column, matrix) == 0:
        print("No one survived")
    else:
        print(human(row, column, matrix), "survived")


print("Sample input 1")
apocalypse("Question2 input1.txt")
print("Sample input 2")
apocalypse("Question2 input2.txt")
