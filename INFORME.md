Para este proyecto se trabajo con tres modulos, dos obligatorios que son calculadora y descuentos y uno a eleccion que fue el de autenticacion, se eligio este ya que los modulos son numericos en cambio el de autenticacion ya eran pruebas con otros enfoques y podria aportar conocimiento en el planteamiento de estas pruebas.

En cada modulo se trato de priorizar las pruebas que pudieran dar errores y tambien de verificacion de resultados correctos, Sin Embargo hubo la necesidad de implementar pruebas que resultan ambiguas para cada funcion pero fueron necesarias para poder obtener la meta de la corbertura exigida para el trabajo. Mas abajo se puede apreciar que se trato de trabajar siempre las pruebas que tenian bugs para poder mejorar el nivel de las pruebas.


-----------------------------------------------------------------Primer Bug Encontrado-------------------------------------

    def test_raiz_cuadrada_negativo():
        a = -9
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

tests/test_calculadora.py:15: Failed



-------------------------------------------------------------------Segundo Bug Encontrado--------------------------------

    def test_minimo_lista_positiva():
        numeros = [5, 8, 2, 10, 4]
        resultado = minimo(numeros)
>       assert resultado == 2
E       assert 0 == 2

tests/test_calculadora.py:21: AssertionError

------------------------------------------------------------------Tercer Bug Encontrado------------------------------------------



    def test_calcular_precio_final_valido():
        precio = 100
        impuesto = 10
        descuento = 20
        resultado = calcular_precio_final(precio, impuesto, descuento)
>       assert resultado == 88
E       assert 90.0 == 88

tests\test_descuentos.py:15: AssertionError
================================================================== short test summary info ===================================================================
FAILED tests/test_descuentos.py::test_calcular_precio_final_valido - assert 90.0 == 88

--------------------------------------------------Cuarto Bug Encontrado--------------------------------------------------------
_________________________________________________________________ test_hash_contraseña_vacia _________________________________________________________________

    def test_hash_contraseña_vacia():
        contraseña = ""
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

tests\test_autenticacion.py:6: Failed
================================================================== short test summary info ===================================================================
FAILED tests/test_autenticacion.py::test_hash_contraseña_vacia - Failed: DID NOT RAISE <class 'ValueError'>
--------------------------------------------------------Quinto Bug Encontrado--------------------------------------------------
_______________________________________________________________ test_token_generado_difetente ________________________________________________________________

    def test_token_generado_difetente():
        token1 = generar_token("juan", 1000)
        token2 = generar_token("juan", 1000)
    
>       assert token1 != token2
E       AssertionError: assert '3d6f137cf78ba8b21c7821750b6803eb' != '3d6f137cf78ba8b21c7821750b6803eb'

tests\test_autenticacion.py:27: AssertionError
================================================================== short test summary info ===================================================================
FAILED tests/test_autenticacion.py::test_token_generado_difetente - AssertionError: assert '3d6f137cf78ba8b21c7821750b6803eb' != '3d6f137cf78ba8b21c7821750b6803eb'



--------------------------------------------------------------------Resultado Medicion de Cobertura------------------------------------------------------------------

collected 78 items                                                                                                                                            

tests\test_autenticacion.py ............................                                                                                                [ 35%]
tests\test_calculadora.py ..............................                                                                                                [ 74%]
tests\test_descuentos.py ....................                                                                                                           [100%]

---------- coverage: platform win32, python 3.14.0-final-0 -----------
Name                   Stmts   Miss  Cover   Missing
----------------------------------------------------
src\autenticacion.py      46      5    89%   55-56, 60-61, 73
src\calculadora.py        60      8    87%   15, 21, 27, 69, 80, 85-87
src\descuentos.py         54      8    85%   21, 24, 27, 51, 53, 57, 83, 92
----------------------------------------------------
TOTAL                    160     21    87%


===================================================================== 78 passed in 0.26s =====================================================================