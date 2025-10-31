import numpy as np
resultados = []
dados = [1, 2, 3, 4, 5, 6]
lanzamientos = 10000
ganancia= 9
acum = 0
for i in range(lanzamientos):
    suma = np.random.choice(dados, 2).sum()
    if suma in [9, 10]:
        acum = acum + ganancia
print(acum)