precio_por_barra = 2.5
descuento = 0.60
barras_vendidas = int(input("Introduce el número de barras no frescas vendidas: "))
precio_total = barras_vendidas * precio_por_barra
descuento_total = precio_total * descuento
precio_final = precio_total - descuento_total
print(f"Precio habitual: {precio_total:.2f}€")
print(f"Descuento: {descuento_total:.2f}€")
print(f"Coste final: {precio_final:.2f}€")