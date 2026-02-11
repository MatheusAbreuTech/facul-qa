def soma(a,b):
    return a+b

try:
    resultado = soma(1,20)
    assert resultado == 30
    print("Soma correta")
except AssertionError:
    print("Soma errada")