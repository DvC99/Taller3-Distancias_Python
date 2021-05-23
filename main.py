""" Taller 2.3 Distancia mas corta #
    Daniel Valencia Cordero
    Mayo 13-2021 """
import numpy as np

def calcular_distancia_c1_a1(xc1,yc1,xa1,ya1):
  return ( np.sqrt( (xc1-xa1)**2 + (yc1-ya1)**2  ) )
#-------------------------------------------
def calcular_distancia_a1_ch(xa1,ya1,xch,ych):
  return ( np.sqrt( (xch-xa1)**2 + (ych-ya1)**2  ) )
#-------------------------------------------
def calcular_distancia_ch_a2(xch,ych,xa2,ya2):
  return ( np.sqrt( (xch-xa2)**2 + (ych-ya2)**2  ) )
#-------------------------------------------
def calcular_distancia_a2_c2(xa2,ya2,xc2,yc2):
  return ( np.sqrt( (xc2-xa2)**2 + (yc2-ya2)**2  ) )
#-------------------------------------------
def obtener_distancia_total (d1,d2,d3,d4):
  return ( d1+d2+d3+d4 )

#======================================================================
#   Algoritmo principal Punto de entrada a la aplicación (Conquistar)
# =====================================================================
#lectura coordenadas celular 1
xcelular1 = int (input("Digite el valor de la coordenada X del Celular 1 \n"))
ycelular1 = int(input("Digite el valor de la coordenada Y del Celular 1 \n"))

#lectura coordenadas antena 1
xantena1 = int(input("Digite el valor de la coordenada X del Antena 1 \n"))
yantena1 = int(input("Digite el valor de la coordenada Y del Antena 1 \n"))

#lectura coordenadas central holi 
xcentralHoli = int(input("Digite el valor de la coordenada X del Central Holi \n"))
ycentralHoli = int(input("Digite el valor de la coordenada Y del Central Holi \n"))

#lectura coordenadas antena 2
xantena2 = int(input("Digite el valor de la coordenada X del Antena 2 \n"))
yantena2 = int(input("Digite el valor de la coordenada Y del Antena 2 \n"))

#lectura coordenadas celular 2
xcelular2 = int(input("Digite el valor de la coordenada X del Celular 2 \n"))
ycelular2 = int(input("Digite el valor de la coordenada Y del Celular 2 \n"))

d1 = calcular_distancia_c1_a1(xcelular1,ycelular1,xantena1,yantena1)
d2 = calcular_distancia_a1_ch(xantena1,yantena1,xcentralHoli,ycentralHoli)
d3 = calcular_distancia_ch_a2(xcentralHoli,ycentralHoli,xantena2,yantena2)
d4 = calcular_distancia_a2_c2(xantena2,yantena2,xcelular2,ycelular2)

distancia_total=obtener_distancia_total (d1,d2,d3,d4)
print("La distancia otal es",distancia_total)


