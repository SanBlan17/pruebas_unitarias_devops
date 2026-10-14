from src.autenticacion import hash_contraseña, validar_usuario, generar_token
import pytest


def test_hash_contraseña_vacia():
    contraseña = ""
    with pytest.raises(ValueError):
            hash_contraseña(contraseña)

def test_hash_contraseña_valida():
    contraseña = "contrasena"
    esperado = "cdcb7422ca0fe077931b84e6fb7e6dfb7d6678dc7e9ae9c4335e98edc7d5761a"
    assert hash_contraseña(contraseña) == esperado

def test_validar_usuario_valido():
    usuario = "Juan_Perez123"
    assert validar_usuario(usuario) == True

def test_validar_usuario_invalido():
    usuario = "Juan@Perez!"
    assert validar_usuario(usuario) == False

def test_token_generado_difetente():
    token1 = generar_token("juan", 1000)
    token2 = generar_token("juan", 1000)
    assert token1 != token2

def test_token_generado_valido():
    token = generar_token("juan", 1000)
    assert len(token) == 32

def test_validat_usuario_vacio():
    usuario = ""
    assert validar_usuario(usuario) == False