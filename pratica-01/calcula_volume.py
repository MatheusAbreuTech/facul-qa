def calcula_volume(comprimento, largura, altura):
    return comprimento * largura * altura

try:
    resultado = calcula_volume(1,1,1)
    assert resultado == 1
    print('Volume 1 Correto')

    resultado = calcula_volume(2,4,3)
    assert resultado == 24
    print('Volume 2 Correto')

    resultado = calcula_volume(5,5,2)
    assert resultado == 100
    print('Volume 3 Correto')
except AssertionError:
    print('Volume Errado')