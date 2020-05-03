import math
a = 3.0
b = 4.0
c = 5.0
# h 为三角形周长的一半
h = (a + b + c) / 2
# 三角形面积为
s = math.sqrt(h * (h-a) * (h-b) * (h-c))
# 输出面积
print(s)
