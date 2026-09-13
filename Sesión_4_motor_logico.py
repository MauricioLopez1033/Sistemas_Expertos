grados = {
    "desempeno_bajo": 0.1,
    "desempeno_promedio": 0.5,
    "desempeno_excelente": 0.85,
    "antiguedad_corta": 0.2,
    "antiguedad_larga": 0.6
}
 
def evaluar_bono(grados):
    bono_bajo = max(grados["desempeno_bajo"], grados["antiguedad_corta"])
    bono_medio = grados["desempeno_promedio"]
    bono_alto = min(grados["desempeno_excelente"], grados["antiguedad_larga"])
    return {"BAJO": bono_bajo, "MEDIO": bono_medio, "ALTO": bono_alto}
 
resultado = evaluar_bono(grados)
print("Niveles de activacion del bono:", resultado)
 
fuerza_regla_a = 0.4
fuerza_regla_b = 0.7
bono_alto_final = max(fuerza_regla_a, fuerza_regla_b)
print("Fuerza final agregada para 'Bono Alto':", bono_alto_final)