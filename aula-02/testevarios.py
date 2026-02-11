def soma(a,b):
    return a + b

# ct01
try:
    resultado = soma(10, 20)
    assert resultado == 30
    print ('Soma Correta')

except AssertionError:
    print('Soma Errada!')

# ct02
try:
    resultado = soma(10, 225)
    assert resultado == 30
    print ('Soma Correta')

except AssertionError:
    print('Soma Errada!')