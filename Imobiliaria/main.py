from casa import Casa
from cliente import Cliente


def inicia():
    casa_um = Casa(11, 3, 5, False, 1500.00)
    casa_dois = Casa(21, 4, 6, True, 2000.00)
    gustavo_161202 = Cliente('Gustavo', [casa_um, casa_dois])
    for casa in gustavo_161202.historico:
        print("Casa: ", casa.numero_casa)
        casa.diaria  = casa.diaria * 2
        print(casa.diaria)

    print(casa_um.distancia)
    print(casa_dois.distancia)

inicia()

