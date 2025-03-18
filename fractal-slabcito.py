import numpy as np
import pandas as pd
from FractalDimension import fractal_dimension
import matplotlib.pyplot as plt

# Adaptado de ChatzigeorgiuGroup para calcular dim. fractal por frame de simulación de dana
def fd_frames(n,r_CG):
    # Del código de Muri
    # Defino el grillado 3D
    # Calcula dim. fractal considerando un electrodo plano implícito
    # a t= 0
    nvx=304
    nvy=304
    nvz=304

    # Nodo inferior más cercano
    boxmin = [0., 0., -3.2]
    boxmax = [300., 300., 300.]
    h=[(boxmax[0]-boxmin[0])/(nvx-1), (boxmax[1]-boxmin[1])/(nvy-1), (boxmax[2]-boxmin[2])/(nvz-1)]
    box = np.zeros(shape = (nvx,nvy,nvz))
    zmin = boxmin[2]/h[2]
    izmin = int(abs(zmin))
    box[:,:,0] = 1.


    # Mask dendritas en grilla
    for n_cg in range(n):

        ip=(r_CG[n_cg,:]-boxmin[:])/h[:]+1

        # El radio de corte en r_cut= 3.2
        r_cut= 3.2

        # XXX: Esto asume que h[0]=h[1]=h[2]
        ia = r_cut/h[0]

        if (2*ia)<1 :
            print('WARNING: hay que mejorar la resolución de la malla')

        iia=int(ia)
        ia2=ia*ia

        # Nodo inferior + cercano
        ri=int(ip[0])
        rj=int(ip[1])
        rk=int(ip[2])
        # Para iterar en el rango del nodo
        fori= [ii for ii in range((ri-iia),(ri+iia+2))]
        forj= [ij for ij in range((rj-iia),(rj+iia+2))]
        fork= [ik for ik in range((rk-iia),(rk+iia+2))]

        for i in fori :
            for j in forj :
                for k in fork :

                    d2= (ip[0]-i)**2 + (ip[1]-j)**2 + (ip[2]-k)**2
                    if (d2>ia2):
                        continue

                    # Mask PBC
                    if (i>(nvx-1)):
                        continue
                    elif (i<0):
                        continue
                    if (j>(nvy-1)):
                        continue
                    elif (j<0):
                        continue
                    if (k<0):
                        continue

                    box[i,j,k] = 1

    # feta2= box[:,:,2]
    # df = pd.DataFrame(feta2)
    # df.to_csv("feta2.csv", sep=' ', header=False, index=False)

    global fd
    # fd = fractal_dimension(box,n_samples=20, max_box_size=6, plot =True)
    fd = fractal_dimension(box,n_samples=20, max_box_size=6, plot =False)
    # plt.show()
    return fd

# Input: CG.xyz generado con vmd topotools
with open('CG.xyz', 'r') as archivo:
    # abro archivo. sobreescribe anteriores versiones
    file = open('fd.dat', 'w')
    file.write('')
    file.close()

    # itero sobre los frames
    n_frames= int(archivo.readline())
    for i in range(n_frames):
        n = int(archivo.readline())     # asigno n como el entero que obtengo de leer la línea 1
        linea= archivo.readline()
        r_CG = np.zeros(shape = (n,3))  # asigno espacio en memoria para mi arreglo

        for nr in range(n):
            linea= archivo.readline()
            r_CG[nr,:]= [float(x) for x in linea.split()[1:4]]  # separa items del string a una lista. Tengo que extraer x y z--1 2 3

        if (n>0):
            fd_frames(n, r_CG)
            # guardo el gráfico calculado para cada frame
            # plt.savefig(f"box-count-{i}")
            # plt.close()
            # print(f"Fractal Dimension of the box: {fd}")
        else :
            # FIXME calcular solamente con un box con 0, sino no anda
            fd_frames(n, r_CG)
            # print(f"Fractal Dimension of the box: {fd}")
            # fd= 0.

        # Guardar fd vs frame
        with open('fd.dat', 'a') as file:
            # write variables using str() function
            file.write(str(i) + ' ' + str(fd) + '\n')

