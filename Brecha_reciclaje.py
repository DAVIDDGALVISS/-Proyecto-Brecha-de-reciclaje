def calcular_brecha_reciclaje(sector, residuos_generados_kg, residuos_reciclados_kg):
    if residuos_generados_kg <= 0:
        return "Error: Los residuos deben ser mayores a cero."

    brecha_kg = residuos_generados_kg - residuos_reciclados_kg
    porcentaje_brecha = (brecha_kg / residuos_generados_kg) * 100

    if porcentaje_brecha >= 70:
        alerta = "CRÍTICO 🔴"
    elif porcentaje_brecha >= 40:
        alerta = "MODERADO 🟡"
    else:
        alerta = "ÓPTIMO 🟢"

    return {
        "Sector": sector,
        "Generados (kg)": residuos_generados_kg,
        "Reciclados (kg)": residuos_reciclados_kg,
        "Brecha (kg)": brecha_kg,
        "Porcentaje de Brecha": f"{porcentaje_brecha:.2f}%",
        "Nivel": alerta
    }


Explicacion: 
if _name_ == "_main_":
    print(calcular_brecha_reciclaje("Zona Centro", 10000, 2500))
  def calcular_brecha_reciclaje(sector, residuos_generados_kg, residuos_reciclados_kg):
    if residuos_generados_kg <= 0:
        return "Error: Los residuos deben ser mayores a cero."

    brecha_kg = residuos_generados_kg - residuos_reciclados_kg
    porcentaje_brecha = (brecha_kg / residuos_generados_kg) * 100

    if porcentaje_brecha >= 70:
        alerta = "CRÍTICO 🔴"
    elif porcentaje_brecha >= 40:
        alerta = "MODERADO 🟡"
    else:
        alerta = "ÓPTIMO 🟢"

    return {
        "Sector": sector,
        "Generados (kg)": residuos_generados_kg,
        "Reciclados (kg)": residuos_reciclados_kg,
        "Brecha (kg)": brecha_kg,
        "Porcentaje de Brecha": f"{porcentaje_brecha:.2f}%",
        "Nivel": alerta
    }

if __name__ == "__main__":
    print(calcular_brecha_reciclaje("Zona Centro", 10000, 2500))
      'Sector': 'Zona Centro',
    'Generados (kg)': 10000,
    'Reciclados (kg)': 2500,
    'Brecha (kg)': 7500,
    'Porcentaje de Brecha': '75.00%',
    'Nivel': 'CRÍTICO 🔴'
