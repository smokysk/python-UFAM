precisao = float(input("Precisão: "))
comprimento = float(input("comprimento: "))
largura = float(input("largura: "))
altura = float(input("comprimento: "))
if precisao > 0:
    volume = (comprimento+precisao)*(largura+precisao)*(altura+precisao)
else:
    volume = (comprimento+precisao)*(largura+precisao)*(altura+precisao)
print(round(volume,2))
