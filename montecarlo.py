import numpy as np

def generar_red_cuadrada(tamano,p):
    #genera una matriz de tamaño tamano x tamano con todos los elementos igual a cero
    red = np.zeros((tamano,tamano))


    # itera sobre cada sitio y asigna aleatoriamente un valor de ocupación igual a 1 con probabilidad p
    for i in range(tamano):
      for j in range(tamano):
          if np.random.rand() < p:
              red[i][j] = 1

    return red

  #tamaño de la red cuadrada
tamano = 10

  #probabilidad de asignar ocupación igual a 1 a un sitio
p = 0.5

  #genera la red cuadrada con los valores de ocupación asignados aleatoriamente
red_generada = generar_red_cuadrada(tamano, p)

print("Red cuadrada generada:")
print(red_generada)