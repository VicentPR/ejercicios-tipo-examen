import random
import math

# Lista de hogares
hogares = [
    "Familia Soto", "Familia Morales", "Familia Vásquez", "Familia Rojas",
    "Familia González", "Familia Castillo", "Familia Bravo", "Familia Contreras",
    "Familia Jara", "Familia Lagos", "Familia Palma", "Familia Reyes"
]

# Diccionario para almacenar consumo por hogar
consumo = {}

# Función 1: Asignar Consumo Aleatorio
def asignar_consumo():
    for hogar in hogares:
        consumo[hogar] = random.randint(8000, 30000)
    print("\nConsumo asignado correctamente.")

# Función 2: Clasificar Consumo
def clasificar_consumo():
    if not consumo:
        print("Primero debe asignar el consumo.")
        return

    print("\nClasificación de Consumo:")
    for hogar, litros in consumo.items():
        if litros < 12000:
            categoria = "Menores a 12.000 litros"
        elif 12000 <= litros <= 25000:
            categoria = "Entre 12.000 y 25.000 litros"
        else:
            categoria = "Mayores a 25.000 litros"
        print(f"{hogar}: {litros} litros → {categoria}")

# Función 3: Estadísticas
def estadisticas():
    if not consumo:
        print("Primero debe asignar el consumo.")
        return

    valores = list(consumo.values())
    maximo = max(valores)
    minimo = min(valores)
    promedio = sum(valores) / len(valores)

    producto = 1
    for v in valores:
        producto *= v
    media_geom = producto ** (1 / len(valores))

    print("\nEstadísticas de Consumo:")
    print(f"Consumo Máximo: {maximo} litros")
    print(f"Consumo Mínimo: {minimo} litros")
    print(f"Promedio de Consumo: {promedio:.2f} litros")
    print(f"Media Geométrica: {media_geom:.2f} litros")

# Función 4: Reporte Detallado
def reporte_detallado():
    if not consumo:
        print("Primero debe asignar el consumo.")
        return

    print("\nReporte Detallado:")
    for hogar, litros in consumo.items():
        descuento_subsidio = litros * 0.05
        impuesto = litros * 0.07
        consumo_neto = litros - descuento_subsidio + impuesto

        print(f"\n{hogar}")
        print(f"  Consumo Bruto: {litros} litros")
        print(f"  Descuento por Subsidio (5%): {descuento_subsidio:.2f} litros")
        print(f"  Impuesto (7%): {impuesto:.2f} litros")
        print(f"  Consumo Neto: {consumo_neto:.2f} litros")

# Función 5: Salir del Programa
def salir():
    print("\nNombre: Juan Pérez")
    print("RUT: 12.345.678-9")
    print("Carrera: Ingeniería en Informática")
    print("Gracias por usar el sistema.")

# Menú Principal
def menu():
    while True:
        print("\n=== Menú Principal ===")
        print("1. Asignar Consumo Aleatorio")
        print("2. Clasificar Consumo")
        print("3. Estadísticas")
        print("4. Reporte Detallado")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            asignar_consumo()
        elif opcion == "2":
            clasificar_consumo()
        elif opcion == "3":
            estadisticas()
        elif opcion == "4":
            reporte_detallado()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()