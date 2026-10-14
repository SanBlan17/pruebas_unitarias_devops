from src.descuentos import aplicar_descuento, calcular_precio_final
import pytest

def test_aplicar_descuento_valido():
    precio = 100
    porcentaje = 20
    resultado = aplicar_descuento(precio, porcentaje)
    assert resultado == 80

def test_calcular_precio_final_valido():
    precio = 100
    impuesto = 10
    descuento = 20
    resultado = calcular_precio_final(precio, impuesto, descuento)
    assert resultado == 88