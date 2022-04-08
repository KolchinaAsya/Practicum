from tkinter import *
import numpy as np
phi = np.arange(0, 2*np.pi, 0.01)
radius = 50

class roundwithpoint():
	def __init__(self, x_round, y_round, speed, vertical):
		self.x_round = x_round
		self.y_round = y_round
		self.vertical = vertical
		self.iter = 0
		self.x_point = x_round + radius 
		self.y_point = y_round + radius / 2
		self.speed = speed
		self.ball = c.create_oval(self.x_point, self.y_point, self.x_point,
								 self.y_point, width=5, outline='white')
		c.create_oval(          
            self.x_round, self.y_round, self.x_round + radius, y_round + radius, outline="white", width=1
        )
		if self.vertical == 0:
			self.line = c.create_line(0, self.y_point, 550, self.y_point, fill='white', width=1)
		elif self.vertical == 1:
			self.line = c.create_line(self.x_point, 0, self.x_point, 550, fill='white', width=1)


	def motion(self):
		global phi
		global radius
		for i in range(self.speed):
			x_delta = radius/2*np.cos(phi[self.iter]) - c.coords(self.ball)[0] + radius/ 2 + self.x_round
			y_delta = -c.coords(self.ball)[3] - radius/2*np.sin(phi[self.iter]) + radius/ 2 + self.y_round
			self.iter += 1
			if self.iter == len(phi) - 1:
				self.iter = 0
			if self.vertical == 0:
				c.move(self.line, 0, y_delta)
			elif self.vertical == 1:
				c.move(self.line, x_delta, 0)
			c.move(self.ball, x_delta, y_delta)


def figure():
	rwpx1.motion()
	rwpx2.motion()
	rwpx3.motion()
	rwpx4.motion()
	rwpx5.motion()
	rwpy1.motion()
	rwpy2.motion()
	rwpy3.motion()
	rwpy4.motion()
	rwpy5.motion()
	rwpy6.motion()
	# 1 - 1
	c.create_oval(c.coords(rwpy1.line)[0], c.coords(rwpx1.line)[3],
					c.coords(rwpy1.line)[0], c.coords(rwpx1.line)[3], width=1, outline="white")
	# 2 - 2
	c.create_oval(c.coords(rwpy2.line)[0], c.coords(rwpx2.line)[3],
					c.coords(rwpy2.line)[0], c.coords(rwpx2.line)[3], width=1, outline="white")
	# 3 - 3
	c.create_oval(c.coords(rwpy3.line)[0], c.coords(rwpx3.line)[3],
					c.coords(rwpy3.line)[0], c.coords(rwpx3.line)[3], width=1, outline="white")
	# 4 - 4
	c.create_oval(c.coords(rwpy4.line)[0], c.coords(rwpx4.line)[3],
					c.coords(rwpy4.line)[0], c.coords(rwpx4.line)[3], width=1, outline="white")
	# 5 - 5
	c.create_oval(c.coords(rwpy5.line)[0], c.coords(rwpx5.line)[3],
					c.coords(rwpy5.line)[0], c.coords(rwpx5.line)[3], width=1, outline="white")
	# 1 - 2
	c.create_oval(c.coords(rwpy2.line)[0], c.coords(rwpx1.line)[3],
					c.coords(rwpy2.line)[0], c.coords(rwpx1.line)[3], width=1, outline="white")
	# 1 - 3
	c.create_oval(c.coords(rwpy3.line)[0], c.coords(rwpx1.line)[3],
					c.coords(rwpy3.line)[0], c.coords(rwpx1.line)[3], width=1, outline="white")
	# 1 - 4
	c.create_oval(c.coords(rwpy4.line)[0], c.coords(rwpx1.line)[3],
					c.coords(rwpy4.line)[0], c.coords(rwpx1.line)[3], width=1, outline="white")
	# 1 - 5
	c.create_oval(c.coords(rwpy5.line)[0], c.coords(rwpx1.line)[3],
					c.coords(rwpy5.line)[0], c.coords(rwpx1.line)[3], width=1, outline="white")
	# 1 - 6
	c.create_oval(c.coords(rwpy6.line)[0], c.coords(rwpx1.line)[3],
					c.coords(rwpy6.line)[0], c.coords(rwpx1.line)[3], width=1, outline="white")
	# 2 - 1
	c.create_oval(c.coords(rwpy1.line)[0], c.coords(rwpx2.line)[3],
					c.coords(rwpy1.line)[0], c.coords(rwpx2.line)[3], width=1, outline="white")
	# 2 - 3
	c.create_oval(c.coords(rwpy3.line)[0], c.coords(rwpx2.line)[3],
					c.coords(rwpy3.line)[0], c.coords(rwpx2.line)[3], width=1, outline="white")
	# 2 - 4
	c.create_oval(c.coords(rwpy4.line)[0], c.coords(rwpx2.line)[3],
					c.coords(rwpy4.line)[0], c.coords(rwpx2.line)[3], width=1, outline="white")
	# 2 - 5
	c.create_oval(c.coords(rwpy5.line)[0], c.coords(rwpx2.line)[3],
					c.coords(rwpy5.line)[0], c.coords(rwpx2.line)[3], width=1, outline="white")
	# 2 - 6
	c.create_oval(c.coords(rwpy6.line)[0], c.coords(rwpx2.line)[3],
					c.coords(rwpy6.line)[0], c.coords(rwpx2.line)[3], width=1, outline="white")
	# 3 - 1
	c.create_oval(c.coords(rwpy1.line)[0], c.coords(rwpx3.line)[3],
					c.coords(rwpy1.line)[0], c.coords(rwpx3.line)[3], width=1, outline="white")
	# 3 - 2
	c.create_oval(c.coords(rwpy2.line)[0], c.coords(rwpx3.line)[3],
					c.coords(rwpy2.line)[0], c.coords(rwpx3.line)[3], width=1, outline="white")
	# 3 - 4
	c.create_oval(c.coords(rwpy4.line)[0], c.coords(rwpx3.line)[3],
					c.coords(rwpy4.line)[0], c.coords(rwpx3.line)[3], width=1, outline="white")
	# 3 - 5
	c.create_oval(c.coords(rwpy5.line)[0], c.coords(rwpx3.line)[3],
					c.coords(rwpy5.line)[0], c.coords(rwpx3.line)[3], width=1, outline="white")
	# 3 - 6
	c.create_oval(c.coords(rwpy6.line)[0], c.coords(rwpx3.line)[3],
					c.coords(rwpy6.line)[0], c.coords(rwpx3.line)[3], width=1, outline="white")
	# 4 - 1
	c.create_oval(c.coords(rwpy1.line)[0], c.coords(rwpx4.line)[3],
					c.coords(rwpy1.line)[0], c.coords(rwpx4.line)[3], width=1, outline="white")
	# 4 - 2
	c.create_oval(c.coords(rwpy2.line)[0], c.coords(rwpx4.line)[3],
					c.coords(rwpy2.line)[0], c.coords(rwpx4.line)[3], width=1, outline="white")
	# 4 - 3
	c.create_oval(c.coords(rwpy3.line)[0], c.coords(rwpx4.line)[3],
					c.coords(rwpy3.line)[0], c.coords(rwpx4.line)[3], width=1, outline="white")
	# 4 - 5
	c.create_oval(c.coords(rwpy5.line)[0], c.coords(rwpx4.line)[3],
					c.coords(rwpy5.line)[0], c.coords(rwpx4.line)[3], width=1, outline="white")
	# 4 - 6
	c.create_oval(c.coords(rwpy6.line)[0], c.coords(rwpx4.line)[3],
					c.coords(rwpy6.line)[0], c.coords(rwpx4.line)[3], width=1, outline="white")
	# 5 - 1
	c.create_oval(c.coords(rwpy1.line)[0], c.coords(rwpx5.line)[3],
					c.coords(rwpy1.line)[0], c.coords(rwpx5.line)[3], width=1, outline="white")
	# 5 - 2
	c.create_oval(c.coords(rwpy2.line)[0], c.coords(rwpx5.line)[3],
					c.coords(rwpy2.line)[0], c.coords(rwpx5.line)[3], width=1, outline="white")
	# 5 - 3
	c.create_oval(c.coords(rwpy3.line)[0], c.coords(rwpx5.line)[3],
					c.coords(rwpy3.line)[0], c.coords(rwpx5.line)[3], width=1, outline="white")
	# 5 - 4
	c.create_oval(c.coords(rwpy4.line)[0], c.coords(rwpx5.line)[3],
					c.coords(rwpy4.line)[0], c.coords(rwpx5.line)[3], width=1, outline="white")
	# 5 - 6
	c.create_oval(c.coords(rwpy6.line)[0], c.coords(rwpx5.line)[3],
					c.coords(rwpy6.line)[0], c.coords(rwpx5.line)[3], width=1, outline="white")
	root.after(1, figure)


root = Tk()
root.geometry('550x550')
root.resizable(height = None, width = None)
c = Canvas(root, width=550, height=550, bg="black")
c.pack()

rwpx1 = roundwithpoint(10, 100, 5, 0)
rwpx2 = roundwithpoint(10, 160, 10, 0)
rwpx3 = roundwithpoint(10, 220, 15, 0)
rwpx4 = roundwithpoint(10, 280, 20, 0)
rwpx5 = roundwithpoint(10, 340,	25, 0)
rwpy1 = roundwithpoint(100, 10, 5, 1)
rwpy2 = roundwithpoint(160, 10, 10, 1)
rwpy3 = roundwithpoint(220, 10, 15, 1)
rwpy4 = roundwithpoint(280, 10, 20, 1)
rwpy5 = roundwithpoint(340, 10, 25, 1)
rwpy6 = roundwithpoint(400, 10, 30, 1)

figure()


root.mainloop()