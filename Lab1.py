from tkinter import *
import numpy as np


def motion():
    global iter 
    
    # x_delta, y_delta - смещение точки по оси 
    if orientation == 1:   # Если направление по часовой стрелке. 
        x_delta = 200*np.cos(phi[iter]) - c.coords(ball)[0] + 300   # Точки считаются для 0,0, потом  смещаем
        y_delta = 200*np.sin(phi[iter]) - c.coords(ball)[3] + 300   
        c.move(ball, x_delta, y_delta)  # перемещение точки на x_delta, y_delta
    elif orientation == -1:     # Направление против часовой стрелки
        x_delta = 200*np.cos(phi[iter]) - c.coords(ball)[0] + 300
        y_delta = -c.coords(ball)[3] - 200*np.sin(phi[iter]) + 300
        c.move(ball, x_delta, y_delta)
    iter += 1
    if iter < len(phi):                        
        root.after(int(2000 / speed), motion)   # Вызов функции анимации(motion) через n миллисекунд; root,after(ms, function)

# Создание окна приложения
root = Tk()     
root.geometry('600x600')   
c = Canvas(root, width=600, height=600, bg="white") 
c.pack()    
c.create_oval(          # Большой кружок
            100, 100, 500, 500, outline="black",
            fill="white", width=2
        )
ball = c.create_oval(200, 200, 201, 201, width=9, fill='blue')  # Создание "точки"

phi = np.arange(0, 2*np.pi, 0.01)   # углы от 0 до 360 в радианах
iter = 0
orientation = -1    # Направление (1 - по часовой, -1 - против часовой)
speed = 20  
 
motion()
 
root.mainloop()