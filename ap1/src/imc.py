def calcular_imc(altura, peso, nome):
    if not isinstance(altura, (int, float)) or not isinstance(peso, (int, float)):
        raise TypeError("Altura e peso devem ser do tipo float ou int.")
    
    if altura == 0:
        raise ValueError("A altura não pode ser zero.")

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25.0: 
        classificacao = "Peso normal"
    elif imc < 30.0: 
        classificacao = "Sobrepeso"
    elif imc < 35.0: 
        classificacao = "Obesidade grau I"
    elif imc < 40.0:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return nome, classificacao
    