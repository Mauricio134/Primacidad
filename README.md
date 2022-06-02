# Primacidad
1) Objetivo:
Se creó un algoritmo con el propósito de poder obtener todos los primos de 3, 4 y 5 cifras. Verificando que todo esto se 
ejecute en un tiempo aceptable. Del mismo modo, se tendrá en consideración el rango de números que nos permitirá verificar
si un número es primo o compuesto.

2) Función Fermat:
Esta función recursiva nos permite resolver códigos de estructura (a^x) mod n de manera más eficiente y reduciendo la 
cantidad de exponenciaciones que se realice para resolver el problema.

	a) Primero definimos la función con sus parámetros específicos (a: base, x: exponente, n: módulo):
	
		def Fermat(a, x, n): (line 3)

	b) Dentro de la función se definen las condicionales para la recursividad respectiva:
	b.1) Primero se determina un if con el resultado base de la función recursiva, con el objetivo de saber en que punto, la
	función recursiva termina su recursión y brinda un valor exacto (el exponente es cero -> el resultado da 1):
	
		if x == 0:
    		    return 1;(lines 4,5)
	b.2) Después se determina un elif con el caso de un exponente par. Donde la recursión devuelve una llamada a la misma 
	función, pero ahora se brinda el cambio del valor x (exponente), el cual se colocará x/2, mientras que los demás valores 
	siguen constantes:
	
		elif x%2 == 0:
    		    t = Fermat(a, x/2, n);
    		    return (t*t)%n; (lines 6, 7, 8)
	b.3) Por último, se coloca un else, para el caso de ingresar un exponente impar. Por tanto, con esto la función realizaría 
	un nuevo llamado a la misma función pero ahora con el exponente reducido en uno, para asi poder volverlo par y ahora se 
	opere con el elif que está especificado para exponentes pares:
	
		else:
    		    t = Fermat(a, x-1, n);
    		    c = a%n;
    		    return (t*c)%n; (lines 9, 10, 11)
Si notamos, cada return de las condicionales da diferentes valores. Por ejemplo en el if  nos retorna 1 ya que es el caso 
base, en el caso del elif retorna la operación de una exponenciación par ((t*t)%n) y en el else retorna la operación de 
una exponenciación impar ((t*c)%n).

