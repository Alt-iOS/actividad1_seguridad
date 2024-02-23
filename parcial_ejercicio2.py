import hashlib
from Crypto.Util.number import getPrime, inverse
import Crypto.Random

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


# Verificación por AC
pdf_hash_verif = pow(signature, e, nA)
print("Firma verificada por AC:", pdf_hash_verif == pdf_hash)

# Generación de llaves para AC
pAC = getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
qAC = getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
nAC = pAC * qAC
phiAC = (pAC - 1) * (qAC - 1)
eAC = 65537
dAC = inverse(eAC, phiAC)

# Firma de AC
signature_ac = pow(pdf_hash, dAC, nAC)

# Verificación por Bob
pdf_hash_verif = pow(signature_ac, eAC, nAC)
print("Firma verificada por Bob:", pdf_hash_verif == pdf_hash)
