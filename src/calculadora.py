"""
Módulo de calculadora con funciones matemáticas básicas.
ATENCIÓN: Hay 2 bugs ocultos en este archivo.
"""

def sumar(a, b):
    """Suma dos números."""
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError("No se puede sumar un número con una cadena de texto")
    return a + b

def restar(a, b):
    """Resta dos números."""
    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("No se puede sumar un número con una cadena de texto")
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("No se puede sumar un número con una cadena de texto")
    return a * b

def dividir(a, b):
    """Divide dos números."""
    if isinstance(a, str) or isinstance(b, str):
            raise ValueError("No se puede sumar un número con una cadena de texto")
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return round(a / b, 1)

def potencia(base, exponente):
    """Calcula la potencia de un número."""
    if isinstance(base, str) or isinstance(exponente, str):
            raise ValueError("No se puede sumar un número con una cadena de texto")
    return base ** exponente

def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número."""
    if isinstance(numero, str):
        raise ValueError("No se puede hallar raiz, ya que es un numero negativo")
    if numero < 0:
        raise ValueError("No se puede hallar raiz, ya que es un numero negativo")
    return numero ** 0.5

def promedio(lista):
    """Calcula el promedio de una lista de números."""
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return sum(lista) / len(lista)

def maximo(lista):
    """Encuentra el número máximo de una lista."""
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    if not all(isinstance(n, (int, float)) and not isinstance(n, bool) for n in lista):
        raise ValueError("Todos los elementos deben ser números")
    max_val = lista[0]
    for num in lista:
        if num > max_val:
            max_val = num
    return max_val

def minimo(lista):
    """Encuentra el número mínimo de una lista."""
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    # BUG 2: No maneja correctamente la comparación inicial
    min_val = lista[0]
    for num in lista:
        if num < min_val:
            min_val = num
    return min_val

def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo."""
    if base < 0 or altura < 0:
        raise ValueError("La base y altura deben ser positivas")
    return base * altura

def calcular_perimetro_rectangulo(base, altura):
    """Calcula el perímetro de un rectángulo."""
    if base < 0 or altura < 0:
        raise ValueError("La base y altura deben ser positivas")
    return 2 * (base + altura)


