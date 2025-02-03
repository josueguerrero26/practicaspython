#introduce una palabra 
val = True
while val:
   palabra = input("Introduce una palabra: ")
   

#inicializa la variable que contara las vocales
   print("La palabra tiene", len(palabra), "letras")
 
#condiciona si la palabra tiene 4 letras, si tiene mas o si yiene menos
   if len(palabra) == 4:
         print("La palabra es correcta")
         
   elif len(palabra) <4:
         print("La palabra es muy corta")
         
   elif len(palabra)>4:
         print("La palabra es muy larga")
         
   val = False 



