import pytest
from codigo_pares import VerificadorExpressao 

# Renomeia a fixture para evitar conflito de nomes
@pytest.fixture
def verificador():
    return VerificadorExpressao()

# Testa expressões válidas
def test_expressao_valida(verificador):
    assert verificador.verificar_expressao("(a + b) * [c - d]") == True
    assert verificador.verificar_expressao("{[()]}") == True
    assert verificador.verificar_expressao("((2 + 3) * 5)") == True

# Testa expressões inválidas
def test_expressao_invalida(verificador):
    assert verificador.verificar_expressao("(a + b) * [c -d}") == False
    assert verificador.verificar_expressao("([)]") == False
    assert verificador.verificar_expressao("((2 + 3) * 5") == False
