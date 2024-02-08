import random
import hashlib

# Paso 1: Definir los parámetros
g = 2  # generador
p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A63A3620FFFFFFFFFFFFFFFF  # un primo grande en hexadecimal

# Paso 2: Generar las llaves privadas de Alice y Bob
a = random.getrandbits(256)  # clave privada de Alice
b = random.getrandbits(256)  # clave privada de Bob
e = random.getrandbits(256)  # clave privada de Eve

# Paso 3: Simular el intercambio de números entre Alice y Bob
A = pow(g, a, p)  # Alice calcula A
E = pow(g, e, p)  # Eve calcula C
B = pow(g, b, p)  # Bob calcula B

# Paso 4: Calcular la clave secretas
s_alice_eve = pow(E, a, p)  # Alice calcula la clave secreta
s_eve_alice = pow(A, e, p)  # Eve calcula la clave secretas
s_bob_eve = pow(E, b, p)  # Bob calcula la clave secreta
s_eve_bob = pow(B, e, p)  # Eve clave secreta

# Paso 5: Verificar que las claves secretas sean iguales
hash_s_alice_eve = hashlib.sha256(str(s_alice_eve).encode()).hexdigest()
hash_s_eve_alice = hashlib.sha256(str(s_eve_alice).encode()).hexdigest()
hash_s_bob_eve = hashlib.sha256(str(s_bob_eve).encode()).hexdigest()
hash_s_eve_bob = hashlib.sha256(str(s_eve_bob).encode()).hexdigest()

if hash_s_alice_eve == hash_s_eve_alice:
    print("Las claves secretas entre eve y alice son iguales y válidas.")
    print("Clave secreta generada:", hash_s_alice_eve)
else:
    print("Las claves secretas no coinciden entre eve y alice.")

if hash_s_bob_eve == hash_s_eve_bob:
    print("Las claves secretas entre eve y bob son iguales y válidas.")
    print("Clave secreta generada:", hash_s_bob_eve)
else:
    print("Las claves secretas no coinciden entre eve y bob.")
