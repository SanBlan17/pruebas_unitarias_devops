from src.calculadora import sumar, dividir, raiz_cuadrada, minimo, promedio
import pytest

def test_sumar_positivos():
    a, b = 7, 5
    resultado = sumar(a, b)
    assert rsultado == 12

def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_raiz_cuadrada_negativo():
    a = -9
    with pytest.raises(ValueError):
        raiz_cuadrada(a)

def test_minimo_lista_positiva():
    numeros = [5, 8, 2, 10,4]
    resultado = minimo(numeros)
    assert resultado == 2

def test_promedio_lista_vacia():
    lista=[]
    with pytest.raises(ValueError):
        promedio(lista)
