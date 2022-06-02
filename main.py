import random

def Fermat(a, x, n):
  if x == 0:
    return 1;
  elif x%2 == 0:
    t = Fermat(a, x/2, n);
    return (t*t)%n;
  else:
    t = Fermat(a, x-1, n);
    c = a%n;
    return (t*c)%n;

def Es_Compuesto(a, n, t, x):
  x0 = Fermat(a, x, n)
  if x0 == 1 or x0 == n-1:
    return False;
  for i in range(t):
    x0 = Fermat(x0, 2, n)
    if x0==n-1:
      return False
  return True

def Miller(n,s):
  t = 0
  u = n-1
  while u%2==0:
    u = u/2
    t = t+1
  for j in range(s):
    a = random.randint(2,n-1)
    if Es_Compuesto(a,n,t,u):
      return False
  return True

#print("Nùmeros primos de 3 cifras:")
#for n in range(101, 998):
#  if n%2 != 0:
#    if Miller(n, 5):
#      print(n,",", end = " ")

#print("Nùmeros primos de 4 cifras:")
#for n in range(1001, 9998):
#  if n%2 != 0:
#    if Miller(n, 8):
#      print(n,",", end = " ")

#print("Nùmeros primos de 5 cifras:")
#for n in range(10001, 99998):
#  if n%2 != 0:
#    if Miller(n, 96):
#      print(n,",", end = " ")

def Randombits(b):
  po = 2**b
  pos = 2**(b-1)
  n = random.randint(0,po-1)
  m = pos + 1
  n = n | m
  return n

def Randomgen(b):
  n = Randombits(b)
  while Miller(n,10) == False:
    n = n+2
  return n

#b=16
#for i in range(10):
#  print(Randomgen(b), end=" ")

#b=32
#for i in range(10):
#  print(Randomgen(b), end=" ")

#b=64
#for i in range(10):
#  print(Randomgen(b), end=" ")
