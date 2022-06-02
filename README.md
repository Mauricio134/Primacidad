# Primacidad
1) Objetivo:
Se creó un algoritmo con el propósito de poder obtener todos los primos de 3, 4 y 5 cifras. Verificando que todo esto se 
ejecute en un tiempo aceptable. Del mismo modo, se tendrá en consideración el rango de números que nos permitirá verificar
si un número es primo o compuesto.

2) Función Fermat:
Esta función recursiva nos permite resolver códigos de estructura (a^x) mod n de manera más eficiente y reduciendo la 
cantidad de exponenciaciones que se realice para resolver el problema.

	a) Primero definimos la función con sus parámetros específicos (a: base, x: exponente, n: módulo):
	``` python
	def Fermat(a, x, n): (line 3)
	```
	b) Dentro de la función se definen las condicionales para la recursividad respectiva:
	b.1) Primero se determina un if con el resultado base de la función recursiva, con el objetivo de saber en que punto, la
	función recursiva termina su recursión y brinda un valor exacto (el exponente es cero -> el resultado da 1):
	``` python
	if x == 0: return 1;
	```
	b.2) Después se determina un elif con el caso de un exponente par. Donde la recursión devuelve una llamada a la misma 
	función, pero ahora se brinda el cambio del valor x (exponente), el cual se colocará x/2, mientras que los demás valores 
	siguen constantes:
	``` python
	elif x%2 == 0:
	    t = Fermat(a, x/2, n);
	    return (t*t)%n;
	```
	b.3) Por último, se coloca un else, para el caso de ingresar un exponente impar. Por tanto, con esto la función realizaría 
	un nuevo llamado a la misma función pero ahora con el exponente reducido en uno, para asi poder volverlo par y ahora se 
	opere con el elif que está especificado para exponentes pares:
	``` python
	else:
	    t = Fermat(a, x-1, n);
	    c = a%n;
	    return (t*c)%n;
	```
Si notamos, cada return de las condicionales da diferentes valores. Por ejemplo en el if  nos retorna 1 ya que es el caso 
base, en el caso del elif retorna la operación de una exponenciación par `(t*t)%n` y en el else retorna la operación de 
una exponenciación impar `(t*c)%n`.

3) Función Es_Compuesto:
La Función permite la determinación de un número como compuesto ```false``` o primo ```true```.
	a) Primero definimos la función con sus parámetros específicos (a: base, x: exponente, n: módulo, t: limite de i):
	``` python
	def Es_Compuesto(a, n, t, x):
	```
	b) Luego, realizamos el uso de la función Fermat para poder encontrar si el número a especificar si es primo o no, no cae en
	los casos de pseudoprimos.
	``` python
	x0 = Fermat(a, x, n)
	  if x0 == 1 or x0 == n-1:
	    return False;
	```
	c) Por último, se debe realizar un for para poder determinar cuantas veces elevar al cuadrado la base x0 y obtener todos los valores
	posibles para determinar si el número es pseudoprimo o primo o compuesto.
	``` python
	for i in range(t):
	    x0 = Fermat(x0, 2, n)
	    if x0==n-1:
	      return False
	return True
	```
Dependiendo de la salida ```return``` se dirá si el número es primo ```True```o si es compuesto o pseudoprimo ```False```.

4) Función Miller (linea24):
Esta función pone en practica el Test de primalidad de Miller Rabin para ello recibe 2 argumentos, siendo el “n” el número que se debe 
determinar si es primo o no, mientras que “s” es el número de bases para las cuales se va a probar el “n”. Una vez ejecutada, la función 
nos va a retornar como resultado un booleano.

	a) El resultado de Miller será True si el número no es compuesto mientras que para un primo nos retornará False, así que para 
	determinar el return se emplea un bucle for en la línea 30 que se ejecutará “s” veces y probará con un “a” random  
	entre 2 y n-1 (la base) la función Es_compuesto.
	

	``` python
	for j in range(s):
	    a = random.randint(2,n-1)
	    if Es_Compuesto(a,n,t,u):
	      return False
	return True
	```


	b) las variables "t" y "u" son obtenidas desde la línea 27 hasta la 29 con un bucle while 
	   que va comprobando que “u” sea divisible entre dos, para así igualar u como u/2  y sumando 1 a “t” mientras que se cumpla 
	   la condición, hallando u-1 = 2^t u.
	   
	``` python
	t = 0
	u = n-1
	while u%2==0:
	   u = u/2
	   t = t+1
	```

5) Impresiones:

	a) Se emplea un buble for que se ejecuta la cantidad de números que hay entre el menor número de “x cifras” pues se pone el segmento que 
	  parte desde el menor número primo hasta el mayor par que cumpla con dicha extensión de cifras. Por ejemplo: 
			
		for n in range(1001, 9998)


	b) Luego se coloca el condicional if (líneas 38, 44, 50) para verificar que el número de “x cifras” no sea par y así evitar ejecuciones innecesarias. 
	  Entonces verificamos  que el resultado de la función Miller sea verdadero (líneas 39, 45, 50) para así imprimir dicho número primo. Ejemplo:

		if n%2 != 0:
			if Miller(n, 8):

	c) Finalmente, para poder encontrar las “s” correctas para probar en cada test de Miller correspondiente a las diferentes extensiones de cifras, hemos probado 
	  con varios números, encontrado que para 3 cifras el “s” adecuado es 5 (línea 39, segundo argumento de Miller); para 4 cifras el “s” 
	  adecuado es 8 (línea 45, segundo argumento de Miller); para 5 cifras el “s” adecuado es 96 (línea 50, segundo argumento de Miller).


