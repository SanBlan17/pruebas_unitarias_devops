from src.calculadora import sumar, dividir
import pytest

def test_sumar_positivos():
    a, b = 7, 5
    resultado = sumar(a, b)
    assert rsultado == 12

def test_dividir_por_cero_lanza_error():
    with pytest.raises(ValueError):
        dividir(10, 0)
