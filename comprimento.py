import math
precisao = float(input("digite o valor da precisao: "))
if (precisao < 0):
    comprimento = 2* math.pi*(1.22 + precisao)
else:
    comprimento = 2* math.pi*(1.22 + precisao)
print(round(comprimento, 2))
