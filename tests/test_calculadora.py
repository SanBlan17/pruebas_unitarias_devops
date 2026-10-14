from src.calculadora import sumar, dividir
import pytest

def test_sumar_positivos():
    a, b = 7, 5
    resultado = sumar(a, b)
    assert rsultado == 12
