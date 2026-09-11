servidor_estado = {
    "CPU_uso": 91,
    "memoria_libre": 10,
    "temperatura": 84,
    "ventilador_encendido": False
}

def diagnosticar_servidor (hechos):
    if hechos["temperatura"] >= 85 and not hechos ["ventilador_encendido"]:
        return "CRITICO: Sobrecalentamiento sin refrigeración activa."
    elif hechos["CPU_uso"] >= 93 and hechos ["memoria_libre"]< 10:
        return "CRITICO: Saturación total de CPU y memoria"
    elif hechos ["temperatura"] >= 85 and hechos ["ventilador_encendido"]:
        return "ADVERTENCIA: Temperatura alta, ventilador activo compensado"
    elif hechos ["CPU_uso"] >= 93 and hechos ["memoria_libre"] >= 10 and hechos ["temperatura"] <= 85:
        return "ADVERTENCIA: Procesador saturado, aún sin riesgo de memoria/calor"
    elif hechos ["memoria_libre"] < 10 and hechos ["CPU_uso"] <= 92 and hechos ["temperatura"] <= 85:
        return "ADVERTENCIA: Memoria escasa, resto de métricas normales"
    elif not hechos ["ventilador_encendido"] and hechos ["temperatura"] <= 85:
        return "ADVERTENCIA: Ventilador apagado de forma preventiva, vigilar temperatura"
    elif hechos ["CPU_uso"] <= 92 and hechos ["memoria_libre"] >= 10 and hechos ["temperatura"] <= 85:
        return "NORMAL: Todas las métricas dentro del rango"
    else:
        return "NO CLASIFICADO: Combinación de valores no prevista, revisar manualmente"

revision = diagnosticar_servidor (servidor_estado)
print ("SERVIDOR EN ESTADO:", revision)
