import csv

def contar_valores_true(csv_file, columna, valor):
    conteoDesempleo = 0

    with open(csv_file, 'r') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')

        for fila in lector_csv:
            #print(fila)
            if fila[columna] == valor:
                conteoDesempleo += 1

    return conteoDesempleo

def contar_total_filas(csv_file):
    with open(csv_file, 'r') as archivo:
        lector_csv = csv.DictReader(archivo)
        filas = list(lector_csv)
        total_filas = len(filas)

    return total_filas

def porcentajeDesmpelados(csv_file):
    return contar_valores_true(csv_file, 'Desempleo', '1') / contar_total_filas(csv_file)

# Ejemplo de uso
archivo_csv = 'datos.csv'
columna_objetivo = 'Desempleo'
valor_objetivo = '1'

cantidad_true = contar_valores_true(archivo_csv, columna_objetivo, valor_objetivo)
print(f"La cantidad de valores '{valor_objetivo}' en la columna '{columna_objetivo}' es: {cantidad_true}")
print(f"El total del conteo es {contar_total_filas(archivo_csv)}")

print(f"El porcentaje de desempleados es: {porcentajeDesmpelados(archivo_csv)}")