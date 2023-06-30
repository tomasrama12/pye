import csv

def contar_valores_desempleo(csv_file):
    conteoDesempleo = 0

    with open(csv_file, 'r') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')

        for fila in lector_csv:
            #print(fila)
            if fila['Desempleo'] == '1':
                conteoDesempleo += 1

    return conteoDesempleo

def contar_valores_pea(csv_file):
    conteoPea = 0

    with open(csv_file, 'r') as archivo:
        lector_csv = csv.DictReader(archivo, delimiter=';')

        for fila in lector_csv:
            #print(fila)
            if fila['PEA'] == '1':
                conteoPea += 1

    return conteoPea

def TDesempleo(csv_file):
    return contar_valores_desempleo(csv_file) / contar_valores_pea(csv_file)





def contar_total_filas(csv_file):
    with open(csv_file, 'r') as archivo:
        lector_csv = csv.DictReader(archivo)
        filas = list(lector_csv)
        total_filas = len(filas)

    return total_filas

def porcentajeDesmpelados(csv_file):
    return contar_valores_desempleo(csv_file) / contar_total_filas(csv_file)

# Ejemplo de uso
archivo_csv = 'datos.csv'
columna_objetivo = 'Desempleo'
valor_objetivo = '1'


print(f"El total del conteo es {contar_total_filas(archivo_csv)}")

print(f"El porcentaje de desempleados es: {porcentajeDesmpelados(archivo_csv)}")

print(f"El porcentaje de Tdesempleados es: {TDesempleo(archivo_csv)}")