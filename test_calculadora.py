import pytest
from calculadora import Calculadora

def test_soma():
    c = Calculadora()
    assert c.soma(2, 2) == 4

def test_subtracao():
    c = Calculadora()
    assert c.subtracao(10, 5) == 5

def test_multiplicacao():
    c = Calculadora()
    assert c.multiplicacao(3, 4) == 12

def test_divisao():
    c = Calculadora()
    assert c.divisao(20, 2) == 10

def test_varias_operacoes():
    c = Calculadora()
    
    resultado1 = c.soma(10, 5)
    resultado_final = c.multiplicacao(resultado1, 2)
    assert resultado_final == 30

def test_divisao_por_zero():
    c = Calculadora()
   
    with pytest.raises(ValueError):
        c.divisao(10, 0)

def test_potenciacao():
    c = Calculadora()
    assert c.potenciacao(2, 3) == 8
