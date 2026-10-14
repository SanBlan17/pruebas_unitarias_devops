from src.autenticacion import hash_contraseña, validar_usuario
import pytest
import hashlib

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