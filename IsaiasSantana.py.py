import random
import statistics
import csv


trabajadores = ["Juan Perez", "María Garcia", "Carlos López", "Ana MartInez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]


def asignar_sueldos():
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    return sueldos


def clasificar_sueldos(sueldos):
    clasificacion = {
        'menores a 800000': [],
        'entre 800000 y 2000000': [],
        'mayores a 2000000': []
    }
    for i in range(len(sueldos)):
        if sueldos[i] < 800000:
            clasificacion['menores a 800000'].append((trabajadores[i], sueldos[i]))
        elif 800000 <= sueldos[i] <= 2000000:
            clasificacion['entre 800000 y 2000000'].append((trabajadores[i], sueldos[i]))
        else:
            clasificacion['mayores a 2000000'].append((trabajadores[i], sueldos[i]))
    return clasificacion


def ver_estadisticas(sueldos):
    sueldo_maximo = max(sueldos)
    sueldo_minimo = min(sueldos)
    promedio_sueldo = statistics.mean(sueldos)
    media_geometrica = statistics.geometric_mean(sueldos)
    return sueldo_maximo, sueldo_minimo, promedio_sueldo, media_geometrica


def calcular_sueldo_liquido(sueldo):
    descuento_salud = sueldo * 0.07
    descuento_afp = sueldo * 0.12
    sueldo_liquido = sueldo - descuento_salud - descuento_afp
    return sueldo, descuento_salud, descuento_afp, sueldo_liquido


def reporte_sueldos(sueldos):
    reporte = []
    for i in range(len(sueldos)):
        sueldo_base, descuento_salud, descuento_afp, sueldo_liquido = calcular_sueldo_liquido(sueldos[i])
        reporte.append([trabajadores[i], sueldo_base, descuento_salud, descuento_afp, sueldo_liquido])
    return reporte


def exportar_a_csv(reporte):
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Suelo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        writer.writerows(reporte)


def main():
    sueldos = []
    while True:
        print("Menu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de suelodos")
        print("5. Salir del programa")
        opcion = input("Seleccione una opcion: ")

        if opcion == '1':
            sueldos = asignar_sueldos()
            print("Sueldos asignados:", sueldos)

        elif opcion == '2':
            if sueldos:
                clasificacion = clasificar_sueldos(sueldos)
                for key, value in clasificacion.items():
                    print(f"\n{key.upper()} TOTAL: {len(value)}")
                    for empleado, sueldo in value:
                        print(f"{empleado}  ${sueldo}")
            else:
                print("Debe asignar sueldos primero.")

        elif opcion == '3':
            if sueldos:
                sueldo_maximo, sueldo_minimo, promedio_sueldo, media_geometrica = ver_estadisticas(sueldos)
                print(f"Sueldo maas alto: ${sueldo_maximo}")
                print(f"Sueldo mas bajo: ${sueldo_minimo}")
                print(f"Promedio de sueldos: ${promedio_sueldo}")
                print(f"Media geometrica: ${media_geometrica}")
            else:
                print("Debe asignar sueldos primero.")

        elif opcion == '4':
            if sueldos:
                reporte = reporte_sueldos(sueldos)
                exportar_a_csv(reporte)
                print("Reporte de sueldos generado y exportado a 'reporte_sueldos.csv'.")
                for fila in reporte:
                    print(f"{fila[0]}  ${fila[1]}  ${fila[2]}  ${fila[3]}  ${fila[4]}")
            else:
                print("Debe asignar sueldos primero.")

        elif opcion == '5':
            print("Finalizando programa...  ")
            print ("Desarrollado por Isaias Santana RUT 17835682-8")
            break

        else:
            print("Opción no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
else:
    print("Ejecutar como script principal para usar el programa.")
