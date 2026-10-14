from src.calculadora import sumar, dividir, raiz_cuadrada
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
