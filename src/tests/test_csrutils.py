import pytest
from csrtool import csrutils
from cryptography.hazmat.primitives.asymmetric import rsa

def test_private_key():
    private_key = csrutils.generate_private_key()
    assert isinstance(private_key, rsa.RSAPrivateKey)

def test_invalid_private_key_length():
    with pytest.raises(ValueError):
        private_key = csrutils.generate_private_key(key_size=-1)

def test_smallest_possible_private_key():
    private_key = csrutils.generate_private_key(key_size=1024)
    assert isinstance(private_key, rsa.RSAPrivateKey)

def test_too_small_private_key():
    
    with pytest.raises(ValueError):
        private_key = csrutils.generate_private_key(key_size=1023)