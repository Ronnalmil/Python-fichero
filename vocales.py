#

texto = input("ingrese el texto").lower()
vocales = "aeiou"
contador = 0

for letra in texto:
    for letra in vocales:
        contador += 1
print("el numero vocales", contador)
    