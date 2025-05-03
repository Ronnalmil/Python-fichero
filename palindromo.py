# Palindromo ABBA == ABBA 

texto=input("ingresa texto")

texto=texto.lower().replace(" ", "")

reversa=""

for letra in texto:
    reversa=letra + reversa
   
if texto == reversa 
   print("es palindromo")
else 
   print("no es palindromo)
