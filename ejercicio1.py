#concatenas es sumar
#añadi '='
# se guardan los .txt en donde esta este. py.
# añadi un if if 1 <= n <=10:
# colocar los ':'
# (1,10) en lugar de (1..10)  

n=int(input("introduce un numero entre 1 y 10:"))
if 1 <= n <=10:
   nombre_fichero='tabla' + str(n)+'.txt'
   fichero=open(nombre_fichero, 'w')

   for i in range (1,10):
     fichero.write(str(i)+'x'+str(n)+ '=' + str(i*n)+ '\n') 
   fichero.close()
------------------- 
n=int(input("ingrese un numero 1-10"))

if n<1 or n>10: 
     print ("error")
else
---‐----------------------------------

chatgpt 2 ejercicio
ejercicio
calculadora
