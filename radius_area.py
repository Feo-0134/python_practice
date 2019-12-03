# from math import pi

# r = float(input(" r = "))

# print("周长: " + str((2*pi)*r))
# print("面积: " + str(pi*(r**2)))

from math import pi

radius = float(input('请输入圆的半径: '))
perimeter = 2 * pi * radius
area = pi * radius * radius

print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)