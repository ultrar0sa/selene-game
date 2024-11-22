from turtle import *
from turtle import RawTurtle
from tkinter import Canvas
from tkinter import *
import json
class Maps:
    def handle_window_close():
        print("", end="")
        pass

    def __init__(self):
        tk = Tk()
        tk.title("Map Window")
        self.artistCanvas = Canvas(tk, width=648, height=768)
        tk.protocol("WM_DELETE_WINDOW", lambda : print("", end="")) 
        self.artistCanvas.pack()
    
        self.artist = RawTurtle(self.artistCanvas) #above is to handle user manually closing map window because program crashes if map is written again if window isn't present
        self.artist.fillcolor("white")
        self.artist.speed(0)
        self.artist.pensize(5)
        self.artist.hideturtle()

    def draw_text(self, starting_x_coord, starting_y_coord, text, color="black"):
        self.artist.penup()
        self.artist.pencolor(color)
        self.artist.goto(starting_x_coord, starting_y_coord)
        self.artist.pendown()
        self.artist.write(text)
        self.artist.pencolor("black")

    def draw_rectangle(self,starting_x_coord, starting_y_coord, width, height):
        self.artist.penup()
        self.artist.goto(starting_x_coord, starting_y_coord)
        self.artist.pendown()
        self.artist.begin_fill()
        count = 1
        while count <= 4:
            # print(self.artist.position())
            if(count % 2 == 0):
                self.artist.forward(height)
                self.artist.right(90)
            else:
                self.artist.forward(width)
                self.artist.right(90)          
            count += 1
        self.artist.end_fill()

    def load_file(self, mapPath):
        self.artist.screen.bgpic("nopic")
        self.artist.clear()
        loadPath = mapPath
        with open(loadPath, "r", encoding="utf-8") as file:
            loadedDict = json.load(file)
            for dict in loadedDict:
                if "backgroundImage" in dict:
                    if dict["backgroundImage"] != "":
                        self.artist.screen.bgpic(dict["backgroundImage"])
                elif "rectHeight" in dict:
                    self.draw_rectangle(int(dict["rectXCoord"]), int(dict["rectYCoord"]), int(dict["rectWidth"]), int(dict["rectHeight"]))
                elif "text" in dict:
                    self.draw_text(int(dict["textXCoord"]), int(dict["textYCoord"]), dict["text"], dict["textColor"])