import string

ALPHABET = string.ascii_uppercase

ROTOR_I = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
ROTOR_II = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
ROTOR_III = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

NOTCH_I = "Q"
NOTCH_II = "E"
NOTCH_III = "V"

REFLECTOR_B = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

plugboard = {}

pasangan = [
    ("J", "X"),
    ("A", "D"),
    ("G", "W")
]

for a, b in pasangan:
    plugboard[a] = b
    plugboard[b] = a


def plug(c):
    if c in plugboard:
        return plugboard[c]
    return c

def inverse(wiring):
    hasil = [""] * 26

    for i in range(26):
        hasil[ord(wiring[i]) - ord("A")] = chr(ord("A") + i)

    return "".join(hasil)

def rotor_maju(c, wiring, posisi, ring):
    index = (ord(c) - ord("A") + posisi - ring) % 26

    hasil = wiring[index]

    index_hasil = (ord(hasil) - ord("A") - posisi + ring) % 26

    return chr(ord("A") + index_hasil)

def rotor_mundur(c, wiring, posisi, ring):
    wiring_inverse = inverse(wiring)

    index = (ord(c) - ord("A") + posisi - ring) % 26

    hasil = wiring_inverse[index]

    index_hasil = (ord(hasil) - ord("A") - posisi + ring) % 26

    return chr(ord("A") + index_hasil)

rotor_kiri   = ROTOR_I
rotor_tengah = ROTOR_III
rotor_kanan  = ROTOR_II

ring_kiri   = ord("L") - ord("A")
ring_tengah = ord("A") - ord("A")
ring_kanan  = ord("V") - ord("A")

posisi_kiri   = ord("N") - ord("A")
posisi_tengah = ord("O") - ord("A")
posisi_kanan  = ord("M") - ord("A")

notch_kiri   = ord(NOTCH_I) - ord("A")
notch_tengah = ord(NOTCH_III) - ord("A")
notch_kanan  = ord(NOTCH_II) - ord("A")

ciphertext = "EYCJDIQQWLQGQUPHNFWUKHWPNXQWBNVORXIULWXVF"

plaintext = ""

for karakter in ciphertext:

    if posisi_tengah == notch_tengah:

        posisi_kiri = (posisi_kiri + 1) % 26
        posisi_tengah = (posisi_tengah + 1) % 26

    elif posisi_kanan == notch_kanan:

        posisi_tengah = (posisi_tengah + 1) % 26

    posisi_kanan = (posisi_kanan + 1) % 26

    karakter = plug(karakter)

    karakter = rotor_maju(
        karakter,
        rotor_kanan,
        posisi_kanan,
        ring_kanan
    )

    karakter = rotor_maju(
        karakter,
        rotor_tengah,
        posisi_tengah,
        ring_tengah
    )

    karakter = rotor_maju(
        karakter,
        rotor_kiri,
        posisi_kiri,
        ring_kiri
    )

    karakter = REFLECTOR_B[
        ord(karakter) - ord("A")
    ]

    karakter = rotor_mundur(
        karakter,
        rotor_kiri,
        posisi_kiri,
        ring_kiri
    )

    karakter = rotor_mundur(
        karakter,
        rotor_tengah,
        posisi_tengah,
        ring_tengah
    )

    karakter = rotor_mundur(
        karakter,
        rotor_kanan,
        posisi_kanan,
        ring_kanan
    )

    karakter = plug(karakter)

    plaintext += karakter

print("Ciphertext :", ciphertext)
print("Plaintext  :", plaintext)