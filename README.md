# Python-fichero
https://chatgpt.com/share/680b6fe8-eb48-800c-b234-5c7ff610cf27
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
