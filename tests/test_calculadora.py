from src.calculadora import sumar, dividir, raiz_cuadrada, minimo, promedio, calcular_area_rectangulo, restar, multiplicar, potencia, maximo
import pytest

def test_sumar_positivos():
    a, b = 7, 5
    resultado = sumar(a, b)
    assert resultado == 12

def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_raiz_cuadrada_negativo():
    a = -9
    with pytest.raises(ValueError):
        raiz_cuadrada(a)

def test_minimo_lista_positiva():
    numeros = [5, 8, 2, 10, 4]
    resultado = minimo(numeros)
    assert resultado == 2

def test_promedio_lista_vacia():
    lista=[]
    with pytest.raises(ValueError):
        promedio(lista)

def test_calcular_area_rectangulo():
    base = 6
    altura = 9
    resultado = calcular_area_rectangulo(base, altura)
    assert resultado == 54

def test_suma_positivos_negativos():
    a, b = 10, -3
    resultado = sumar(a, b)
    assert resultado == 7

def test_suma_negativos():
    a, b = -4, -6
    resultado = sumar(a, b)
    assert resultado == -10

def test_suma_string():
    a, b = 9, "Mundo"
    with pytest.raises(ValueError):
        sumar(a, b)

def test_resta_positivos_negativos():
    a, b = 10, -3
    resultado = restar(a, b)
    assert resultado == 13

def test_suma_flotantes():
    a, b = 5.5, 2.3
    resultado = sumar(a, b)
    assert resultado == pytest.approx(7.8)

def test_multiplicacion_positivos():
    a, b = 4, 5
    resultado = multiplicar(a, b)
    assert resultado == 20

def test_multiplicacion_negativos():
    a, b = -4, -6
    resultado = multiplicar(a, b)
    assert resultado == 24

def test_multiplicacion_con_cero():
    a, b = 7, 0
    resultado = multiplicar(a, b)
    assert resultado == 0

def test_multiplicacion_positivo_negativo():
    a, b = 4, -3
    resultado = multiplicar(a, b)
    assert resultado == -12

def test_division_positivos():
    a, b = 20, 4
    resultado = dividir(a, b)
    assert resultado == 5

def test_division_negativos():
    a, b = -20, -4
    resultado = dividir(a, b)
    assert resultado == 5

def test_division_entero_con_flotante():
    a, b = 7, 2.5
    resultado = dividir(a, b)
    assert resultado == 2.8

def test_potencia_exponente_cero():
    base, exponente = 5, 0
    resultado = potencia(base, exponente)
    assert resultado == 1

def test_potencia_con_string():
    base, exponente = 5, "2"
    with pytest.raises(ValueError):
        potencia(base, exponente)

def test_raiz_cuadrada_cero():
    numero = 0
    resultado = raiz_cuadrada(numero)
    assert resultado == 0

def test_raiz_cuadrada_string():
    numero = "16"
    with pytest.raises(ValueError):
        raiz_cuadrada(numero)

def test_promedio_lista_positiva():
    lista = [10, 20, 30, 40]
    resultado = promedio(lista)
    assert resultado == 25

def test_promedio_lista_con_negativos():
    lista = [10, -20, 30, -40]
    resultado = promedio(lista)
    assert resultado == -5

def test_maximo_lista_positiva():
    lista = [3, 7, 2, 9, 5]
    resultado = maximo(lista)
    assert resultado == 9

def test_maximo_lista_negativa():
    lista = [-3, -7, -2, -9, -5]
    resultado = maximo(lista)
    assert resultado == -2

def test_maximo_lista_vacia():
    lista = []
    with pytest.raises(ValueError):
        maximo(lista)

def test_maximo_lista_con_string():
    lista = [3, 7, "2", 9, 5]
    with pytest.raises(ValueError):
        maximo(lista)