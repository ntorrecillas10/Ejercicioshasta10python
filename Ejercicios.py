
def ej1obtener_maximo():

    lista_numeros = [3, 5, 2, 9, 1]

    maximo = lista_numeros[0]
    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero
    print(maximo)

def ej2obtener_sumatoria():
    lista_numeros = [3, 5, 2, 9, 1]
    suma = 0
    for numero in lista_numeros:
        suma += numero
    print(suma)

def ej3millas_a_kilometros(millas):
    kilometros = millas * 1.6
    print(kilometros)

def ej4es_vocal(letra):

    vocales = ["a","e","i","o","u","A","E","I","O","U"]
    if letra in vocales:
        print(f"{letra} es una vocal")
    else:
        print(f"{letra} no es una vocal")

def ej5contar_pares():
    lista_numeros = [3, 5, 2, 9, 1, 2]
    cantidad_pares = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cantidad_pares += 1
    print(cantidad_pares)

def ej6contar_multiplos(numero):
    cantidad = 0
    for i in range(1, 11):
        if i % numero == 0:
            cantidad += 1
    print(cantidad)

def ej7es_triangulo_rectangulo(a, b, c):
    lados = sorted([a, b, c])
    if lados[2]**2 == lados[0]**2 + lados[1]**2:
        print("El triángulo es rectángulo")
    else:
        print("El triángulo no es rectángulo")


def ej8mcd(a, b):
    while b != 0:
        a, b = b, a % b
    print(f"El máximo común divisor es {a}")

def ej9imprimir_mosaicos(n):
    for i in range(1, n + 1):
        print(str(i) * i)


def ej10imprimir_mosaico_rombo(filas):
    for i in range(1, filas // 2 + 2):
        print(' ' * (filas // 2 + 1 - i) + '*' * (2 * i - 1))
    for i in range(filas // 2, 0, -1):
        print(' ' * (filas // 2 + 1 - i) + '*' * (2 * i - 1))











