from src.descuentos import aplicar_descuento, calcular_precio_final
import pytest

def test_aplicar_descuento_valido():
    precio = 100
    porcentaje = 20
    resultado = aplicar_descuento(precio, porcentaje)
    assert resultado == 80

