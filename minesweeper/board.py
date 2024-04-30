import tkinter as tk
from PIL import Image, ImageTk
import os
from game import Game

class Board:
    def __init__(self, size, dimensions):
        self.size = size
        self.header = 'Minesweeper'
        self.window = tk.Tk()
        self.sized = self.getSize()
        self.images_path = 'images'
        self.image_names = self.get_image_names()
        self.dimensions = dimensions
        self.probability = 0.2
        self.running = True

        self.game = Game
        self.bombs = self.game.makeBombs(self)

    def get_image_names(self):
        image_names = []

        for filename in os.listdir(self.images_path):
            name = self.images_path + '/' + filename
            image_names.append(name)
        
        return image_names
    
    def getSize(self):
        size = self.size
        size = size.split('x')
        size = [int(i) for i in size]
        return size

    def draw(self):
        self.window.geometry(self.size)
        self.window.title(self.header)

        self.labels = []

        for index_x in range(len(self.bombs)):
            row = []
            for index_y in range(len(self.bombs[index_x])):
                img = Image.open(self.image_names[10])
                new_img = self.resizeImage(img, self.sized)
                label = tk.Label(self.window, image = new_img)
                label.index = (index_x, index_y)
                label.bind('<Button-1>', self.callReveal)
                label.bind('<Button-3>', self.callSetFlag)
                label.photo = new_img
                if self.bombs[index_x][index_y] == True:
                    label.bomb = True
                else:
                    label.bomb = False
                label.flag = False
                label.clicked = False   
                label.visited = False             
                label.grid(row=index_x % self.dimensions[0], column=index_y % self.dimensions[1])
                row.append(label)
            self.labels.append(row)

        self.window.mainloop()
    
    def resizeImage(self, image, size):
        resized = image.resize((int(size[0] / (self.dimensions[0] * 1.04)), int(size[1] / (self.dimensions[1] * 1.04))))
        return ImageTk.PhotoImage(resized)

    def callReveal(self, event):
        self.game.reveal(self, event)

    def callSetFlag(self, event):
        self.game.setFlag(self, event)