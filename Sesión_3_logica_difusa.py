def membresia_triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)
 
conductores = [3, 6, 12]
 
for tiempo in conductores:
    grado_novato = membresia_triangular(tiempo, 0, 0, 5)
    grado_intermedio = membresia_triangular(tiempo, 2, 5, 8)
    grado_experto = membresia_triangular(tiempo, 5, 10, 20)
 
    print(f"\nConductor con {tiempo} años de experiencia:")
    print(f"  Novato: {grado_novato:.2f}")
    print(f"  Intermedio: {grado_intermedio:.2f}")
    print(f"  Experto: {grado_experto:.2f}")
 
    grados = {"Novato": grado_novato, "Intermedio": grado_intermedio, "Experto": grado_experto}
    categoria = max(grados, key=grados.get)
    print(f"  -> Categoria que mejor encaja: {categoria}")
