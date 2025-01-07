import time, copy, random

width = 60
height = 20

next_cell = []
#用一个数组来装cell
for x in range(width):
    column = []
    for y in range(height):
        if random.randint(0, 1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cell.append(column)
while True:
    print('\n\n\n\n')
    currentCells = copy.deepcopy(next_cell)
    for y in range(height):
        for x in range(width):
            print(currentCells[x][y], end='')
        print()
    for x in range(width):
        for y in range(height):
            #找出四个方向
            leftcoord = (x - 1) % width
            rightcoord = (x + 1) % width
            topcoord = (y - 1) % height
            bottomcoord = (y + 1) % height

            #count the neighbors
            numneighbors = 0
            if currentCells[leftcoord][topcoord] == '#':
                numneighbors += 1
            if currentCells[x][topcoord] == '#':
                numneighbors += 1
            if currentCells[rightcoord][topcoord] == '#':
                numneighbors += 1
            if currentCells[leftcoord][y] == '#':
                numneighbors += 1
            if currentCells[rightcoord][y] == '#':
                numneighbors += 1
            if currentCells[leftcoord][bottomcoord] == '#':
                numneighbors += 1
            if currentCells[x][bottomcoord] == '#':
                numneighbors += 1
            if currentCells[rightcoord][bottomcoord]:
                numneighbors += 1

            if currentCells[x][y] == '#' and (numneighbors == 2 or numneighbors == 3):
                next_cell[x][y] = '#'
            elif currentCells == ' ' and (numneighbors == 3):
                next_cell[x][y] = '#'
            else:
                currentCells[x][y] = ' '
    time.sleep(1)


