from src.descuentos import aplicar_descuento, calcular_precio_final, descuento_apilado, descuento_cumulativo, descuento_por_volumen
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

def test_descuento_apilado_valido():
    precio = 100
    descuentos = [10, 20, 30]
    resultado = descuento_apilado(precio, descuentos)
    assert resultado == 40

def test_descuento_cumulativo_descuento_excede_100():
    precio = 100
    descuentos = [50, 100, 30]  # Total descuento = 110%
    with pytest.raises(ValueError):
        descuento_cumulativo(precio, descuentos)

def test_descuento_cumulativo_valido():
    precio = 100
    descuentos = [10, 20, 30]  # Total descuento = 60%
    resultado = descuento_cumulativo(precio, descuentos)
    assert resultado == 50.4

def test_descuento_por_volumen_valido():
    cantidad = 25
    precio_unitario = 10
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    assert resultado == 225 

def test_aplicar_descuento_porcentaje_negativo():
    precio = 100
    porcentaje = -10
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)

def test_descuento_del_100_por_ciento():
    precio = 200
    porcentaje = 100
    resultado = aplicar_descuento(precio, porcentaje)
    assert resultado == 0

def test_precio_negativo_aplicar_descuento():
    precio = -50
    porcentaje = 10
    with pytest.raises(ValueError):
        aplicar_descuento(precio, porcentaje)

def test_descuento_con_decimales():
    precio = 99.99
    porcentaje = 15.5
    resultado = aplicar_descuento(precio, porcentaje)
    assert resultado == pytest.approx(84.49, 0.01)

def test_precio_final_sin_descuento_ni_impuesto():
    precio = 100
    impuesto = 0
    descuento = 0
    resultado = calcular_precio_final(precio, impuesto, descuento)
    assert resultado == 100

def test_precio_final_solo_impuesto():
    precio = 100
    impuesto = 15
    descuento = 0
    resultado = calcular_precio_final(precio, impuesto, descuento)
    assert resultado == 115

def test_descuento_por_volumen_sin_descuento():
    cantidad = 5
    precio_unitario = 10
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    assert resultado == 50

def test_descuento_por_volumen_con_cantidad_cero():
    cantidad = 0
    precio_unitario = 10
    resultado = descuento_por_volumen(cantidad, precio_unitario)
    assert resultado == 0

def test_descuento_por_volumen_con_cantidad_negativa():
    cantidad = -5
    precio_unitario = 10
    with pytest.raises(ValueError):
        descuento_por_volumen(cantidad, precio_unitario)