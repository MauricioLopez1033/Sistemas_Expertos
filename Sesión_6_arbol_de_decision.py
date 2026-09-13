from sklearn.tree import DecisionTreeClassifier, export_text
import numpy as np
 
# Columnas de X: [Edad, Horas_Online, Compras_Previas]
X = np.array([
    [22, 5, 3],
    [45, 1, 0],
    [19, 8, 5],
    [60, 0, 0],
    [25, 6, 4],
    [50, 2, 1],
    [30, 7, 6],
    [55, 1, 0],
    [21, 9, 2],
    [40, 3, 1],
])
 
# Y: 1 = Hizo clic en el anuncio, 0 = Lo ignoro
Y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
 
arbol = DecisionTreeClassifier(max_depth=3)
arbol.fit(X, Y)
 
nombres_variables = ["Edad", "Horas_Online", "Compras_Previas"]
reglas_texto = export_text(arbol, feature_names=nombres_variables)
 
print("Base de Reglas generada automaticamente por el arbol:\n")
print(reglas_texto)
