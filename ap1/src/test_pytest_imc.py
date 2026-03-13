import pytest
from imc import calcular_imc

def test_type_error():
    with pytest.raises(TypeError):
        calcular_imc("1.75", 70, "Maria")
        
    with pytest.raises(TypeError):
        calcular_imc(1.75, "70", "Maria")

def test_informando_dados_corretos():
    nome, classificacao = calcular_imc(1.60, 90, "Maria")
    
    assert nome == "Maria"
    assert classificacao == "Obesidade grau II"