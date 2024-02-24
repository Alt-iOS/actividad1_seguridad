import hashlib
from Crypto.Util.number import getPrime, inverse
import Crypto.Random


def read_last_bytes(filename, num_bytes):
    with open(filename, "rb") as f:
        f.seek(-num_bytes, 2)  # Seek to num_bytes before the end of the file
        return f.read(num_bytes)


# Generación de llaves para Alice
bits = 1024
pA = getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qA = getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
nA = pA * qA
phiA = (pA - 1) * (qA - 1)
e = 65537
dA = inverse(e, phiA)

# Firma digital de Alice
with open("NDA.pdf", "rb") as f:
    pdf_bytes = f.read()
    pdf_hash = int.from_bytes(hashlib.sha256(pdf_bytes).digest(), "big")
signature = pow(pdf_hash, dA, nA)

# Convertimes la firma a bytes
signature_bytes = signature.to_bytes((signature.bit_length() + 7) // 8, byteorder="big")

# lo agregamos al final del archivo
with open("NDA.pdf", "ab") as f:
    f.write(signature_bytes)

# restamos la firma del archivo
with open("NDA.pdf", "rb") as f:
    pdf_bytes = f.read()[:-256]

# checamos los ultimos 256 bytes
signature_bytes_from_pdf_AC = read_last_bytes("NDA.pdf", 256)
#los convertimos a int
signature_int_from_pdf_AC = int.from_bytes(signature_bytes_from_pdf_AC, byteorder='big')
# Verificación por AC con la publica de Alice
pdf_hash_verif = pow(signature_int_from_pdf_AC, e, nA)
print("Firma verificada por AC:", pdf_hash_verif == pdf_hash)

# Generación de llaves para AC
pAC = getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qAC = getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
nAC = pAC * qAC
phiAC = (pAC - 1) * (qAC - 1)
eAC = 65537
dAC = inverse(eAC, phiAC)

# Firma de AC con la publica de AC
signature_ac = pow(pdf_hash, dAC, nAC)

# Agregamos la firma de AC al final del archivo
signature_ac_bytes = signature_ac.to_bytes(
    (signature_ac.bit_length() + 7) // 8, byteorder="big"
)
with open("NDA.pdf", "ab") as f:
    f.write(signature_ac_bytes)

# Verificación por Bob
pdf_hash_verif_bob = pow(signature_ac, eAC, nAC)
print("Firma verificada por Bob:", pdf_hash_verif_bob == pdf_hash)
