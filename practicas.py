import math

def media(datos):
    #suma = 0
    #for dato in datos:
    #    suma += dato
    #return suma/len(datos)
    m = sum(datos)/len(datos)
    return m

def moda(datos):
    repeticiones = 0

    for dato in datos:
        apariciones = datos.count(dato)
        if (apariciones > repeticiones):
            repeticiones = apariciones
    
    modas = []

    for dato in datos:
        apariciones = datos.count(dato)
        if (apariciones == repeticiones) and dato not in modas:
            modas.append(dato)

    if(len(datos) == len(modas)):
        modas = []

    return modas
    
def mediana(datos):
    datos.sort()
    mitad = len(datos) / 2

    if len(datos) % 2 == 0:
        mediana = (datos[mitad - 1] + datos[mitad]) / 2
    else:
        mediana = datos[len(datos) // 2]

    return mediana

def varianza(datos):
    sumatoria = 0
    promedio = media(datos)
    for dato in datos:
        sumatoria += (dato - promedio)**2

    varianza = sumatoria/len(datos)

    return varianza

def desviacionEstandar(datos):
    return math.sqrt(varianza(datos))

def covarianza(x, y):
    sumatoria = 0
    mediax = media(x)
    mediay = media(y)
    n = len(x)

    for i in range(n):
        sumatoria += ((x[i]-mediax) * (y[i] - mediay))

    covarianza = sumatoria / n

    return covarianza

def distanciaEuclidean(x, y, length):
    distance = 0
    for i in range(length):
        distance += pow((x[i] - y[i]), 2)
    return math.sqrt(distance)