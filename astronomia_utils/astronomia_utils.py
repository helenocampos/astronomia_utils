def forca_gravitacional(massa1, massa2, distancia):
    G = 6.67430e-11  # Constante gravitacional universal (em m^3/kg/s^2)
    forca = (G * massa1 * massa2) / distancia**2
    return forca

def peso_na_superficie(massa, gravidade):
    peso = massa * gravidade
    return peso