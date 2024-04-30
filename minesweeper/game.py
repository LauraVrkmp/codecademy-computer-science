import random
from PIL import Image, ImageTk

class Game:
    def makeBombs(self):
        self.bombs = []
        for row in range(self.dimensions[0]):
            bombs_row = []
            for col in range(self.dimensions[1]):
                bomb = random.random() < self.probability
                bombs_row.append(bomb)
            self.bombs.append(bombs_row)

        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                if self.bombs[x][y] == False:
                    count = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if 0 <= x + dx < self.dimensions[0] and 0 <= y + dy < self.dimensions[1]:
                                if self.bombs[x + dx][y + dy] == True:
                                    count -= 1
                    self.bombs[x][y] = count
        
        return self.bombs

    def setFlag(self, event):
        index_x = event.widget.index[0]
        index_y = event.widget.index[1]
        image_names = self.get_image_names()
        if self.running == False:
            return
        elif self.labels[index_x][index_y].clicked == True:
            return
        elif self.labels[index_x][index_y].flag == False:
            img = Image.open(image_names[11])
            self.labels[index_x][index_y].flag = True
        else:
            img = Image.open(image_names[10])
            self.labels[index_x][index_y].flag = False
        new_img = self.resizeImage(img, self.sized)
        self.labels[index_x][index_y].configure(image = new_img)
        self.labels[index_x][index_y].image = new_img

    def reveal(self, event):
        index_x = event.widget.index[0]
        index_y = event.widget.index[1]
        numBombs = -1
        if self.running == False or self.labels[index_x][index_y].flag == True:
            return
        elif self.labels[index_x][index_y].bomb == False:
            numBombs = -self.bombs[index_x][index_y]
            img = Image.open(self.image_names[numBombs])
            self.labels[index_x][index_y].clicked = True
            self.labels[index_x][index_y].visited = True
        else:
            img = Image.open(self.image_names[9])
            self.labels[index_x][index_y].clicked = True
            self.running = False
        new_img = self.resizeImage(img, self.sized)
        self.labels[index_x][index_y].configure(image = new_img)
        self.labels[index_x][index_y].image = new_img
        if numBombs == 0:
            self.game.revealNeighbors(self, index_x, index_y)
    
    def revealNeighbors(self, x, y):
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if 0 <= x + dx < self.dimensions[0] and 0 <= y + dy < self.dimensions[1]:
                    if self.labels[x + dx][y + dy].visited == False:
                        self.game.revealAutomatic(self, x + dx, y + dy)

    def revealAutomatic(self, index_x, index_y):
        numBombs = -self.bombs[index_x][index_y]
        img = Image.open(self.image_names[numBombs])
        self.labels[index_x][index_y].clicked = True
        self.labels[index_x][index_y].visited = True
        new_img = self.resizeImage(img, self.sized)
        self.labels[index_x][index_y].configure(image = new_img)
        self.labels[index_x][index_y].image = new_img
        if numBombs == 0:
            self.game.revealNeighbors(self, index_x, index_y)