monto_transaccion = 7000
pais_transaccion = "Rusia"
pais_cliente = "Colombia"
 
hechos = {
    "monto_alto": monto_transaccion > 5000,
    "pais_extranjero": pais_transaccion != pais_cliente,
    "tarjeta_reportada_robo": False,
    "compra_nocturna": True
}
 
reglas = [
    {"id": "R1",
     "condiciones": {"monto_alto": True},
     "conclusion": {"transaccion_inusual": True}},
 
    {"id": "R2",
     "condiciones": {"transaccion_inusual": True, "pais_extranjero": True},
     "conclusion": {"bloquear_tarjeta": True}},
 
    {"id": "R3",
     "condiciones": {"tarjeta_reportada_robo": True},
     "conclusion": {"bloquear_tarjeta": True}},
 
    {"id": "R4",
     "condiciones": {"transaccion_inusual": True, "compra_nocturna": True},
     "conclusion": {"alerta_seguridad": True}},
]
 
nuevos_hechos = True
while nuevos_hechos:
    nuevos_hechos = False
    for regla in reglas:
        condiciones_cumplidas = all(hechos.get(k) == v for k, v in regla["condiciones"].items())
        if condiciones_cumplidas:
            for clave, valor in regla["conclusion"].items():
                if clave not in hechos:
                    hechos[clave] = valor
                    nuevos_hechos = True
                    print(f"Disparando {regla['id']} -> Nuevo hecho: {clave}={valor}")
 
print("\nMemoria final de hechos:", hechos)
 
if hechos.get("bloquear_tarjeta"):
    print("\nRESULTADO: La tarjeta debe ser bloqueada por seguridad.")
else:
    print("\nRESULTADO: La transaccion parece normal.")
