#Importar las bibliotecas

import numpy as np
import matplotlib.pyplot as plt
import numba
from numba import njit
from scipy.ndimage import convolve, generate_binary_structure

#Red cuadrada 50x50
N = 50

#Generar algunas cuadrículas iniciales aleatorias de espines
init_random = np.random.random((N,N))
lattice_n = np.zeros((N,N))
lattice_n[init_random>=0.75] = 1
lattice_n[init_random<0.75] = -1

init_random = np.random.random((N,N))
lattice_p = np.zeros((N,N))
lattice_p[init_random>0.25] = 1
lattice_p[init_random<0.25] = -1

plt.imshow(lattice_p)