from src.autenticacion import hash_contraseña
import pytest

def test_hash_contraseña_vacia():
    contraseña = ""
    with pytest.raises(ValueError):
            hash_contraseña(contraseña)

