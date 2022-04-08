from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import math

def draw(event):
    canv.delete('all')  # Очищение холства
    n = scale_n.get()   # Получение значения со слайдера
    d = scale_d.get()
    phi = np.arange(0, 2*np.pi, 0.01)   
    rho = []
    for i in range(len(phi)):   # Нахождение точки в полярных координатах
        rho.append((n*np.sin(d * phi[i]), phi[i]))
    x, y = [], []
    for i in range(len(rho)):   # Из полярных координат переход в x, y
        x.append(rho[i][0] * math.cos(rho[i][1]))
        y.append(rho[i][0] * math.sin(rho[i][1]))
    for i in range(len(x) - 1):     # Отрисовка графика
        canv.create_line((x[i] + 50)*5, (y[i]+50)*5, (x[i+1] + 50)*5, (y[i+1]+50)*5, width=2, fill='white')

root = Tk()
root.title("Лабораторная 2")
root.geometry('600x600')
label_n = Label(root, text='n = ')  # Создание  элемента label("текст в приложении")
label_n.place(x=10, y=20)   # Расположение элемента
scale_n = Scale(root,orient=HORIZONTAL,length=300,from_=10,to=100,tickinterval=10,resolution=10)   #Создание слайдера 
scale_n.bind("<B1-Motion>",draw)    # Привязка изменение слайдера к функции
scale_n.place(x=40, y=10)

label_d = Label(root, text='d = ')
label_d.place(x=10, y=60)
scale_d = Scale(root,orient=HORIZONTAL,length=300,from_=1,to=15,tickinterval=1,resolution=1)
scale_d.bind("<B1-Motion>",draw)
scale_d.place(x=40, y=50)
canv=Canvas(root,width=500,height=500,bg="lightblue",cursor="pencil")   # Создание холста для рисования
canv.place(x=0,y=90)
root.mainloop()
