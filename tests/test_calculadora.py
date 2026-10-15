from src.calculadora import sumar, dividir, raiz_cuadrada, minimo, promedio, calcular_area_rectangulo, restar, multiplicar
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