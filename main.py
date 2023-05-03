Exercises = int(input("Ingrese el numero de la operacion que desea realizar"))
if Exercises == 1:
  base = int(input("Ingrese la base del triángulo: "))
  altura = int(input("ingrese la altura del triángulo: "))
  area = (base * altura) / 2
  print("El area del triangulo es: ", area)
if Exercises == 2: 
  number1 = int(input("Ingrese el primer número que desea sumar: "))
  number2 = int(input("ingrese el segundo número que desea sumar: "))
  result = (number1 + number2)   
  print("la suma total de los números ingresados es de: ", resultado)
if Exercises == 3: 
  NumberE = int(input("introducir un numero: "))
  result = (NumberE * NumberE)
  print("El numero", NumberE , "elevado al cuadrado es: ", result)
if Exercises == 4:
  Addition1 = 1234
  Addition2 = 532
  Result = (Addition1 + Addition2)
  print("la suma de 1234 mas 532 es igual a ", Result)
if Exercises == 5:
  subtraction1 = 1234
  subtraction2 = 532
  Result = (subtraction1 - subtraction2)
  print("la resta de 1234 mas 532 es igual a ", Result)
if Exercises == 6:
  multiplication1 = 1234
  multiplication2 = 532
  Result = (multiplication1 * multiplication2)
  print("la multiplicacion de 1234 por 532 es igual a ", Result)
if Exercises == 7:
  division1 = 1234
  division2 = 532
  Result = (division1 / division2)
  print("la division de 1234 entre 532 es igual a ", Result)
if Exercises == 8:
  mod1 = 1234
  mod2 = 532
  Result = (mod1 % mod2)
  print("El módulo 1234 entre 532 es igual a ", Result)
if Exercises == 9:
  EUR = int(input("ingrese la cantidad de euros  para convertir a dolares"))
  USD = (EUR * 1.09)
  print(" ingreso un valor de " , EUR , "Euros esto equivale a " , USD , "dolares")
if Exercises == 10:
  altura = int(input("ingrese la altura del rectángulo"))
  ancho = int(input("ingrese el ancho del rectángulo"))
  Area = (altura * ancho)
  print(" el area del rectángulo es de ", Area , "centímetros")
if Exercises == 11:
  Lado = int(input("escriba el lado del cuadrado"))
  Area = (Lado * Lado)  
  Perimetro = (Lado *4)
  print("El area es igual a ", Area , " y el perímetro es igual a ", Perimetro)
if Exercises == 12:
  radio = int(input("ingrese el valor del radio"))
  h = int(input("ingrese el valor de la altura "))
  pI = 3.1416
  Area = (2 * pI * radio * (radio + h ))
  Volumen = pI*radio * radio * h
  print("El volumen es" ,Volumen, "y el area es"    , Area)
if Exercises ==13:
  R = int(input("Escriba el valor del radio"))
  L = (2 * 3.1416 * R )
  A = ( 3.1416 * (R * R ))     
  print(" La longitud del circuito es" ,L, "El area es igual a: ", A )

if Exercises == 14:
  prom1 = int(input("Ingrese un valor"))
  prom2 = int(input("ingrese un valor"))
  prom3 = int(input("ingrese un valor"))
  result_prom = (prom1 + prom2 + prom3) / 3
  print(" El promedio de la operación es: " , result_prom)