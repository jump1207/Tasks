#1) Є коло з центром на початку координат та радіусом 4. Користувач вводить з
#клавіатури координати точки x та y. Написати програму, яка визначить, знаходиться
#ця точка всередині кола  чи ні.
r = 4
x0 = 0
y0 = 0
x = float(input("Input x "))
y = float(input("Input y "))

if (x - x0)**2 + (y - y0)**2 < r**2:
    print("The Point lies inside the circle")
else:
    print("The Point lies outside or on the circle")
