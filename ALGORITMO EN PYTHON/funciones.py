import numpy as np


def funcion_recuadro(imagen,h,w,x,y):

    foto = imagen
    m = np.shape(foto)[0]
    n = np.shape(foto)[1]

    e = 4
    B = 0
    G = 255
    R = 0
    
    if (y-h/2-e > 0 and x-w/2-e > 0 and y+h/2+e < m and x+w/2+e < n):
        
        # Primera linea horizontal
        foto[int(y-h/2-e):int(y-h/2), int(x-w/2-e):int(x+w/2+e), :] = 0
        foto[int(y-h/2-e):int(y-h/2), int(x-w/2-e):int(x+w/2+e), 0] = B
        foto[int(y-h/2-e):int(y-h/2), int(x-w/2-e):int(x+w/2+e), 1] = G
        foto[int(y-h/2-e):int(y-h/2), int(x-w/2-e):int(x+w/2+e), 2] = R
            
            
        # Segunda linea horizontal
        foto[int(y+h/2):int(y+h/2+e), int(x-w/2-e):int(x+w/2+e), :] = 0
        foto[int(y+h/2):int(y+h/2+e), int(x-w/2-e):int(x+w/2+e), 0] = B
        foto[int(y+h/2):int(y+h/2+e), int(x-w/2-e):int(x+w/2+e), 1] = G
        foto[int(y+h/2):int(y+h/2+e), int(x-w/2-e):int(x+w/2+e), 2] = R

        # Primera linea vertical
        foto[int(y-h/2-e):int(y+h/2+e), int(x-w/2-e):int(x-w/2), :] = 0
        foto[int(y-h/2-e):int(y+h/2+e), int(x-w/2-e):int(x-w/2), 0] = B
        foto[int(y-h/2-e):int(y+h/2+e), int(x-w/2-e):int(x-w/2), 1] = G
        foto[int(y-h/2-e):int(y+h/2+e), int(x-w/2-e):int(x-w/2), 2] = R

        # Segunda linea vertical
        foto[int(y-h/2-e):int(y+h/2+e), int(x+w/2):int(x+w/2+e), :] = 0
        foto[int(y-h/2-e):int(y+h/2+e), int(x+w/2):int(x+w/2+e), 0] = B
        foto[int(y-h/2-e):int(y+h/2+e), int(x+w/2):int(x+w/2+e), 1] = G
        foto[int(y-h/2-e):int(y+h/2+e), int(x+w/2):int(x+w/2+e), 2] = R
        
        return foto

    else:
        #print("Cuadro fuera de rango")
        return foto

def funcion_mask_rgb(Imagen, rango_B, rango_G, rango_R):

    B = Imagen[:,:,0]
    G = Imagen[:,:,1]
    R = Imagen[:,:,2]
    
    bin_color_B = np.bitwise_and(B >= rango_B[0],B <= rango_B[1])
    bin_color_G = np.bitwise_and(G >= rango_G[0],G <= rango_G[1])
    bin_color_R = np.bitwise_and(R >= rango_R[0],R <= rango_R[1])
    
    mask = np.bitwise_and(bin_color_R, bin_color_G, bin_color_B)
  
    return mask

def funcion_centro(mask):
 
    lista_x = []
    lista_y = []
    for i in range(0,mask.shape[0],2): #step=2 para reducir el tiempo de procesamiento
        for j in range(0,mask.shape[1],2):
            if mask[i,j]==1:
                lista_y.append(i)
                lista_x.append(j)
                
    A = len(lista_x)+0.0001
    r = np.sqrt(A/np.pi)
    h = round(2*r);
    w = round(2*r);
    x = round(sum(lista_x)/A);
    y = round(sum(lista_y)/A);
    
    return [h,w,x,y]

def funcion_saturador(a,b):
    m, n = np.shape(a)
    c = np.zeros((m,n), dtype=np.uint8)
    for i in range(0,m):
        for j in range(0,n):
            if a[i,j] >= b[i,j]:
                c[i,j] = a[i,j]-b[i,j]
            else:
                c[i,j] = b[i,j]-a[i,j]     
    return c
