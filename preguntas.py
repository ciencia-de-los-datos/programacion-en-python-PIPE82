"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
#conexcion general
#((data.csv)) ruta relativa

with open("data.csv", "r") as file:
    archivo = file.readlines()
filas=len(archivo)
# Limpieza
#print(archivo)
#print(type(archivo))
archivo_eventos = [line.replace("\n", "") for line in archivo]
#print(type(archivo_eventos))
archivo_eventos = [line.split("\t") for line in archivo_eventos]


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    registros = len(archivo_eventos)
    sum = 0

    for n in range((registros)):
        dato = (archivo_eventos[n])
        op1 = int(dato[1])
        sum = sum + op1
   
    return sum


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    registros = len(archivo_eventos)
    numero = 0
    word_counts = []
    respuesta = []
    for n in range((registros)):
        dato = (archivo_eventos[n])
        op1 = str(dato[0])
        word_counts.append(op1)

    #print(word_counts, "pipe")

    # se creara un diccionario
    dict = {}
    numero = 0
    for n in word_counts:
        if n in dict:
            # contar el numero de veces
            dict[n] += 1
        else:
            dict[n] = 1

    # primero ordenar por orden alfabetico
    #print((dict), "pipe")
    dict = sorted(dict.items())
    #respuesta2 = (*dict,)
    respuesta2=dict
    #print(type(respuesta2))
    #print(respuesta2)


    return respuesta2


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    registros = len(archivo_eventos)
    numero = 0
    word_counts = []
    respuesta3 = []
    for n in range((registros)):
        dato = (archivo_eventos[n])
        op1 = str(dato[0])
        if op1 not in word_counts:
            word_counts.append(op1)

    word_counts = sorted(word_counts)

    for n in word_counts:
        cod = n
        suma = 0
        for n1 in archivo_eventos:
            if n1[0] == n:
                suma = suma + int(n1[1])
        respuesta3.append((cod, suma))
    #respuesta3 = (*respuesta3,)
    respuesta3=respuesta3
    #print(type(respuesta3))
    #print(respuesta3)
    return respuesta3


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    fechas = []
    for n in archivo_eventos:
        cadena = n[2]
        separador = "-"
        separado = cadena.split(separador)
        fechas.append((separado))

    #print(fechas)

    meses = []
    for n in fechas:
        op1 = str(n[1])
        meses.append(op1)

    #print(meses)

    # se creara un diccionario
    dict = {}
    numero = 0
    for n in meses:
        if n in dict:
            # contar el numero de veces
            dict[n] += 1
        else:
            dict[n] = 1

    dict = sorted(dict.items())
    #respuesta4 = (*dict,)
    respuesta4=dict
    #print(type(respuesta4))
    #print(respuesta4)

    return respuesta4



def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    registros = len(archivo_eventos)
    numero = 0
    word_counts = []
    respuesta5 = []
    for n in range((registros)):
        dato = (archivo_eventos[n])
        op1 = str(dato[0])
        if op1 not in word_counts:
            # puedo iterar para conocer el maximo y el minimo
            word_counts.append(op1)

    word_counts = sorted(word_counts)
    #print(word_counts)

    for n in (word_counts):
        dato = n[0]
        x_max = 0
        x_min = 99999
        # hallar el maximo
        for n in archivo_eventos:
            dato2 = n[0]
            # print(dato,lista2)
            if dato == dato2:  # igualdad de letra para buscar el mayor y el menor
                max = int(n[1])
                min = int(n[1])
                if x_max < max:
                    x_max = max
                if x_min > min:
                    x_min = min
        respuesta5.append((dato, x_max, x_min))

    return respuesta5


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    claves = []

    for n in archivo_eventos:
        cadena = n[4]
        separador = ","
        separado = cadena.split(separador)
        claves.append(separado)
    #print(claves)

    #print(type(claves))

    new_clave = []
    for n in claves:
        cadena = n
        for n1 in n:
            new_clave.append(n1.split(':'))

    #print(new_clave)

    # seleccionar las claves
    numero = 0
    word_counts = []
    respuesta6 = []
    for n in new_clave:
        op1 = (n[0])
        if op1 not in word_counts:
            word_counts.append(op1)

    word_counts = sorted(word_counts)
    #print(word_counts)

    for n in (word_counts):
        dato = n
        x_max = 0
        x_min = 99999
        # hallar el maximo
        for n1 in new_clave:
            dato2 = n1[0]
            if dato == dato2:  # igualdad de letra para buscar el mayor y el menor
                max = int(n1[1])
                min = int(n1[1])

                if x_max < max:
                    x_max = max
                if x_min > min:
                    x_min = min
        respuesta6.append((dato, x_min, x_max))
    #print(respuesta6)
    return respuesta6


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    numero = 0
    word_counts = []
    counts = []

    for n in archivo_eventos:
        op1 = int((n[1]))
        if op1 not in counts:
            counts.append(op1)

    counts = sorted(counts)
    #print(counts)

    for n in counts:
        dato = n
        variable = ""
        for n1 in archivo_eventos:
            if dato == int(n1[1]):
                if variable == "":
                    variable = n1[0]
                else:
                    variable = variable + ',' + n1[0]
        lista_letras: str = variable.split(",")
        word_counts.append((dato, (lista_letras)))

    respuesta7 = word_counts
    return respuesta7


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    numero = 0
    word_counts = []
    counts = []

    for n in archivo_eventos:
        op1 = int((n[1]))
        if op1 not in counts:
            counts.append(op1)

    counts = sorted(counts)
    #print(counts)

    for n in counts:
        dato = n
        variable = ""
        for n1 in archivo_eventos:
            if dato == int(n1[1]):
                if n1[0] not in variable:
                    if variable == "":
                        variable = n1[0]
                    else:
                        variable = variable + ',' + n1[0]

        lista_letras: str = variable.split(",")
        lista_letras = sorted(lista_letras)
        word_counts.append((dato, (lista_letras)))

    respuesta8 = word_counts

    return respuesta8


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    cadena = []  # Creamos una lista con los elementos de la columna 5

    # Recorremos cada lina del dataset
    for line in archivo_eventos:
        cadena.append(line[4].split(
            ','))  # Creamos sublistas con los elementos de la columna 5 y los almacenamos a la lista cadena

    # Creamos un diccionario vacío para almacenar la respuesta
    respuesta9 = {}

    # Iteramos a través de las sublistas en la lista cadena
    for sublista in cadena:
        for item in sublista:
            key, value = item.split(':')  # Por cada item en las sublistas separamos la llave y el valor
            # Si la llave ya existe, la sumamos, sino, asignamos el valor
            if key in respuesta9:
                respuesta9[key] += 1
            else:
                respuesta9[key] = 1

    # Ordenamos el diccionario alfabeticamente
    respuesta9 = sorted(respuesta9.items())
    respuesta9 = dict(respuesta9)
    return respuesta9


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    respuesta10 = []  # Creamos la lista que contendrá las tuplas

    # Recorreroms las sublistas del set de datos
    for sublista in archivo_eventos:
        item1 = sublista[0]  # Tomamos el elemento de la primera columna
        item2 = sublista[3].split(',')  # Creamos una sublista con los elementos de la columna 4
        contador_item2 = 0
        for element in item2:
            contador_item2 += 1  # Contamos el número de elementos que hay en la columna 4
            item3 = sublista[4].split(',')  # Creamos una sublista con los elementos de la columna 5
            contador_item3 = 0
            for element in item3:
                contador_item3 += 1  # Contamos el número de elementos que hay en la columna 5
        tupla = (item1, contador_item2, contador_item3)  # Creamos la tupla
        respuesta10.append(tupla)  # Almacenamos la tupla en la lista de respuesta

    return respuesta10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }
    

    """
    respuesta11 = {}  # Creamos el diccionario que contendrá la respuesta
    # Recorreroms las sublistas del set de datos
    for sublista in archivo_eventos:
        key_lista = sublista[3].split(',')  # Creamos una sublista de llaves con los elementos de la columna 4
        value = int(sublista[1])  # Tomamos el elemento de la columna 2 y lo convertimos a integer

        # Recorremos cada elemento de la sublista de lalves
        for key in key_lista:
            if key in respuesta11:
                respuesta11[key] += value
            else:
                respuesta11[key] = value

    # Ordenamos el diccionario alfabeticamente
    respuesta11 = sorted(respuesta11.items())
    respuesta11 = dict(respuesta11)


    return respuesta11


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    respuesta12 = {}  # Creamos el diccionario que contendrá la respuesta
    # Recorreroms las sublistas del set de datos
    for sublista in archivo_eventos:
        key = sublista[0]  # Tomamos el elemento de la primera columna como llave
        value_lista = sublista[4].split(',')  # Creamos una sublista con los elementos de la columna 5

        for item in value_lista:
            key1, value = item.split(':')  # Separamos el valor de las sublistas de la columna 5

            
            if key in respuesta12:
                respuesta12[key] += int(value)
            else:
                respuesta12[key] = int(value)

    # Ordenamos el diccionario alfabeticamente
    respuesta12 = sorted(respuesta12.items())
    respuesta12 = dict(respuesta12)

    return respuesta12
