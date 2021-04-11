import math
precisao = float(input("digite o valor da precisao: "))
if (precisao < 0):
    comprimento = math.pi*math.pow((1.22 + precisao),2)
else:
    comprimento = math.pi*math.pow((1.22 + precisao),2)
print(round(comprimento, 2))
