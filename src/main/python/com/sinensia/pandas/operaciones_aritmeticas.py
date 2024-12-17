import pandas as pd

serie1 = pd.Series([10, 20, 30, 40])
serie2 = pd.Series([1, 2, 3, 4])

#Series - Suma
suma = serie1 + serie2
print("Suma:\n", suma)

#Series - Resta
resta = serie1 - serie2
print("Resta:\n", suma)

#Concatenacion
serie_concatenada = pd.concat([serie1, serie2])
print("Serie Concatenada:\n", serie_concatenada)

#Multiplicacion
serie_multiplicada = serie1 * serie2
print("Multiplicacion:\n", serie_multiplicada)

#Division
serie_dividida = serie1 / serie2
print("Division:\n", serie_dividida)

#Operaciones estadisticas - Series
#Media
media = serie1.mean()
print("Media de serie1:", media)

#Mediana
mediana = serie1.median()
print("Mediana de serie1:", mediana)

#Desviacion estandar
desviacion_estandar = serie1.std()
print("Desviacion estandar de serie1:", desviacion_estandar)

#Suma total
suma_total = serie1.sum()
print("Suma total de serie1:", suma_total)

#Minimo y maximo
minimo = serie1.min()
maximo = serie1.max()
print("Minimo de serie1:", minimo)
print("Maximo de serie1:", maximo)

#count
conteo = serie1.count()
print("Numero de elementos en serie1:", conteo)

#unique
valores_unicos = serie1.unique()
print("Valores unicos en serie1:", valores_unicos)

#value_counts
valores_cuenta = serie1.value_counts()
print("Conteo de valores en serie1:\n", valores_cuenta)

#moda
moda = serie1.mode()
print("Moda de serie1:", moda)

#varianza
varianza = serie1.var()
print("Varianza de serie1:", varianza)

#describe
description = serie1.describe()
print("Descripcion de serie1:\n", description)

#Correlacion
corr = serie1.corr(serie2)
print("Correlacion entre serie1 y serie2:", corr)

#Covarianza
cov = serie1.cov(serie2)
print("Covarianza entre serie1 y serie2:", cov)

cuantil_25 = serie1.quantile(0.25)
cuantil_50 = serie1.quantile(0.5)       #Equivale a mediana
cuantil_75 = serie1.quantile(0.75)
print("Cuantil 25% de serie1:", cuantil_25)
print("Cuantil 50% (mediana) de serie1:", cuantil_50)
print("Cuantil 75% de serie1:", cuantil_75)

serie_negativa = pd.Series([-1, -2, -3, 4])
valores_absolutos = serie_negativa.abs()
print("Valores absolutos:", valores_absolutos)

suma_acumulativa = serie1.cumsum()
print("Suma acumulativa de serie1:", suma_acumulativa)

producto_acumulativo = serie1.cumprod()
print("Producto acumulativo de serie1:", producto_acumulativo)