print(f"""
+=====================================================================+
| * Escribe un programa que muestre por consola (con un print) los    |
| * números de 1 a 100 (ambos incluidos y con un salto de línea entre |
| * cada impresión), sustituyendo los siguientes:                     |
| * - Múltiplos de 3 por la palabra "fizz".                           |
| * - Múltiplos de 5 por la palabra "buzz".                           |
| * - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".       |
+=====================================================================+
      """)

for i in range(1,101,1):
  if type(i) is float:
    print(f"{i} es  un nuemro decimal(float).\nEl nuemro debe ser un entero(int).")
    break
  else:
    if i % 3 == 0 and i % 5 == 0:
      print("fizzbuzz\n")
    elif i % 3 == 0:
      print(f"Fizz\n")
    elif i % 5 == 0:
      print("Buzz\n")
    else:
      print(f"{i}\n")
  