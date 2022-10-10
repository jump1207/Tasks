#2) Дан трикутник координати вершин якого А(0,0), В(4,4), С(6,1). Користувач
#вводить з клавіатури координати точки x та y. Написати програму, яка
#визначить, знаходиться ця точка всередині треугольника чи ні.
xa = 0
ya = 0
xb = 4
yb = 4
xc = 6
yc = 1
xo = float(input("Input x "))
yo = float(input("Input y "))

sabc = abs((xa * yb + xb * yc + xc * ya) - (ya * xb + yb * xc + yc * xa)) / 2
print("Sabc =  ", sabc)

sabo = abs((xa * yb + xb * yo + xo * ya) - (ya * xb + yb * xo + yo * xa)) / 2
print("Sabo =  ", sabo)

sobc = abs((xo * yb + xb * yc + xc * yo) - (yo * xb + yb * xc + yc * xo)) / 2
print("Sobc =  ", sobc)

saoc = abs((xa * yo + xo * yc + xc * ya) - (ya * xo + yo * xc + yc * xa)) / 2
print("Saoc =  ", saoc)

if sabc == sabo + sobc + saoc:
    print("The Point lies inside the triangle")
else:
    print("The Point lies outside the triangle")
