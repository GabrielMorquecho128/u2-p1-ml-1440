import numpy as np

califas=np.array([60,70,90])
print(" ------------- ej 1 imprimir califas --------")
print(califas) # imprime la lista de califas
print(type(califas)) # muestra eltipo de arreglo 
print(" ------------- ej 0 dimenciones de un array--------")
califas=np.array(60)
print(califas)
print("Dimension :", califas.ndim)
print(" ------------- ej 1 dimension de un array--------")
califas=np.array([60,70,90])
print(califas)
print("Dimension :", califas.ndim)
print(" ------------- ej 2 dimension de un array--------")
califas=np.array([
    [60,70,90]
    [50,80,90]
    ]) # un arreglode 2 dimenciones es como una tabla de excel
print(califas)
print("Dimension :", califas.ndim)