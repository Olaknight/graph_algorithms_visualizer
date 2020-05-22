import pygame

num_cols = cols = 100
num_rows = rows = row = 100
openSet = []
closedSet = []
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
grey = (220, 220, 220)
white = (255, 255, 255)
w = RECT_WIDTH = 800 / cols
h = RECT_HEIGHT = 800 / rows
cameFrom = []
screen = pygame.display.set_mode((800, 800))

class Grid:
    def __init__(self):
        self.grid = []

        for i in range(num_rows):
            temp = []
            for j in range(num_cols):
                temp.append(Spot(i, j))
            self.grid.append(temp)
        

    def displayGrid(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].show(white, 1)
    
    def get(self, i, j):
        return self.grid[i][j]

    def generateNeigbours(self):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j].addNeighbors(self)


class Spot:
    def __init__(self, i, j):
        self.x_coord = i
        self.y_coord = j
        self.f = self.g = self.h = 0
        self.neighbors = []
        self.previous = None
        self.obs = False
        self.closed = False
        self.value = 1
    
    def show(self, color, st):
        pygame.draw.rect(screen, color, (self.x_coord * w, self.y_coord * h, w, h), st)
        pygame.display.update()

    def path(self, color, st):
        pygame.draw.rect(screen, color, (self.i * w, self.j * h, w, h), st)
        pygame.display.update()

    def addNeighbors(self, grid):
        i, j = self.x_coord, self.y_coord

        for x,y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
            if 0 <= x < cols and 0 <= y < rows:
                self.neighbors.append(grid.get(x, y))


def mousePress(x, grid):
    t = x[0]
    w = x[1]
    g1 = t // (800 // cols)
    g2 = w // (800 // row)
    acess = grid.get(g1, g2)
    if acess != start and acess != end:
        if acess.obs == False:
            acess.obs = True
            acess.show((255, 255, 255), 0)