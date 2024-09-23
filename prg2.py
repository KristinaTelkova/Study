import turtle as t # подключили "черепашку"

# RAM - random access memory
# DRY - do not repeat yourself (code should be clear)
sides = 8 # число сторон замкнутой фигуры
dist = 120 # переменной dist присвоено значение 120
angle = 360 / sides # переменной присвоено значение 360/sides

t.forward(dist) #100-длина в пикселях
t.right(angle) #90-повернуть на 90 градусов
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)

t.mainloop()
