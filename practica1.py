from Crypto.Util import number
import random

print(
    "Ejericio 1 - Obtener un número aleatorio de 256 bits \n",
    random.getrandbits(256),
)

i = 0
while True:
    i = i + 1
    j = random.getrandbits(1024)
    esPrimo = number.isPrime(j)
    if esPrimo:
        print("En la iteracion: ", i, " se encontro el primo", j, "\n")
        break


# Ejercicio 3
# Obteener inverso multiplicativo
def invero_multiplicativo(x, y):
    print(
        "Inverso multiplicativo de x:",
        x,
        "\n el numero y: ",
        y,
        "\n es: ",
        number.inverse(x, y),
    )


a = random.getrandbits(1024)
b = random.getrandbits(1024)

invero_multiplicativo(a, b)

# Ejercicio 4
# Potencia de un nunmero 2^(n) de 256b bits y "p" es primo de 1024 bits
a = 2
b = random.getrandbits(1024)
c = j


def potencia(x, y, z):
    print(
        "\n Ejercicio 4: la potencia de x: ",
        x,
        "y: ",
        y,
        "mod z: es:",
        z,
        "es: ",
        pow(x, y, z),
    )

    potencia(a, b, c)
