from tkinter import *
import random
import time
class Ball:
    def __init__(self, canvas,paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.color = color
        self.canvas.bind_all('<KeyPress-Up>', self.restart)
        self.reset()

    def restart(self, evt):
        if self.hit_bottom == True:
           self.reset() 
        
        
    def reset(self):
        self.hit_bottom = False
        self.id = canvas.create_oval(10, 10, 25, 25, fill=self.color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        random.shuffle(starts)
        self.y = starts[0]

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if self.hit_paddle(pos) == True:
           self.y = -3
        if pos[1] <= 0:
           self.y = -self.y
        if pos[3] >= 400:
           self.y = -self.y
        if pos[0] <= 0 or pos[2] >= 500:
           self.x = -self.x
        if pos[3] >= 400:
            self.hit_bottom = True
            self.canvas.create_text(220, 200, text='game over', font=('Courier', 30),fill='red')
        


class Paddle:
      def __init__(self, canvas, color):
          self.canvas = canvas
          self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
          self.canvas.move(self.id, 200, 300)
          self.x = 0
          self.canvas_width = 500
          self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
          self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
      def turn_left(self, evt):
          self.x = -5
    
      def turn_right(self, evt):
          self.x = 5
      


      def draw(self):
          self.canvas.move(self.id, self.x, 0)
          pos = self.canvas.coords(self.id)
          if pos[0] <= 0:
             self.x = 0
          elif pos[2] >= self.canvas_width:
             self.x = 0
        

tk = Tk()
tk.title("Game")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, paddle, 'orange')


tk.update()
while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
