from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import math

def draw(event):
    canv.delete('all')  # Очищение холства
    a = scale_a.get()   # Получение значения со слайдера
    b = scale_b.get()
    k = a/b
    phi = np.arange(0, 2*np.pi, 0.01)   
    x, y = [], []
    for i in range(len(phi)):   # Вычисление координат x, y
        x.append((a + b)*math.cos(phi[i]) - a*math.cos(0.5 + (a + b)/2*phi[i]))
        y.append((a + b)*math.sin(phi[i]) - a*math.sin(0.5 + (a + b)/2*phi[i]))
    for i in range(len(x) - 1):     # Отрисовка графика
        canv.create_line((x[i] + 50)*5, (y[i]+50)*5, (x[i+1] + 50)*5, (y[i+1]+50)*5, width=2, fill='white')

root = Tk()
root.title("Лабораторная 2")
root.geometry('600x600')
label_n = Label(root, text='a = ')  # Создание  элемента label("текст в приложении")
label_n.place(x=10, y=20)   # Расположение элемента
scale_a = Scale(root,orient=HORIZONTAL,length=300,from_=1,to=12,tickinterval=2,resolution=2)   #Создание слайдера 
scale_a.bind("<B1-Motion>",draw)    # Привязка изменение слайдера к функции
scale_a.place(x=40, y=10)

label_d = Label(root, text='b = ')
label_d.place(x=10, y=60)
scale_b = Scale(root,orient=HORIZONTAL,length=300,from_=1,to=12,tickinterval=2,resolution=2)
scale_b.bind("<B1-Motion>",draw)
scale_b.place(x=40, y=50)
canv=Canvas(root,width=500,height=500,bg="lightblue",cursor="pencil")   # Создание холста для рисования
canv.place(x=0,y=90)
root.mainloop()
