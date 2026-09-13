import numpy as np
 
def defuzzificar_centroide(x, curva):
    numerador = np.sum(x * curva)
    denominador = np.sum(curva)
    return numerador / denominador
 
x_prueba = np.array([10, 20, 30, 40])
mu_prueba = np.array([0.2, 0.8, 0.8, 0.0])
 
resultado_prueba = defuzzificar_centroide(x_prueba, mu_prueba)
print("Resultado de validacion (debe coincidir con el calculo a mano):", resultado_prueba)
 
x_frenado = np.linspace(0, 100, 100)
 
centro = 70
sigma = 10
curva_frenado = np.exp(-((x_frenado - centro) ** 2) / (2 * sigma ** 2))
 
fuerza_frenado_final = defuzzificar_centroide(x_frenado, curva_frenado)
print(f"La fuerza de frenado exacta calculada es: {fuerza_frenado_final:.2f} Newtons")
