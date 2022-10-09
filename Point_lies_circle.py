#1) Есть круг с центром в начале координат и радиусом 4. Пользователь вводит с
#клавиатуры координаты точки x и y. Написать программу, которая определит,
#лежит ли эта точка внутри круга или нет
r = 4
x0 = 0
y0 = 0
x = float(input("Input x "))
y = float(input("Input y "))

if (x - x0)**2 + (y - y0)**2 < r**2:
    print("The Point lies inside the circle")
else:
    print("The Point lies outside or on the circle")