#Sudoku simplificado (4x4)
#Generar un tablero 4x4 con números del 1 al 4 (pueden estar repetidos).
#Escribir una función que valide si una fila tiene todos los números distintos.
#Escribir otra que valide una columna.
#(Extra) Validar que cada subcuadro 2x2 también cumpla la condición.
#👉 Aplican listas anidadas, bucles y slicing.
import random
sudoku = [random.sample(range(1, 5), 4)]
print(sudoku)
tablero_completo = False
while not tablero_completo:
    fila = int(random.randint(0,3))
    columna = random.randint(0,3)
    valor = random.randint(1, 4)
    for i in range(4):
        if sudoku[fila][i] == valor:
            print("El valor ya existe en la fila")
            break
        elif sudoku[i][columna] == valor:
            print("El valor ya existe en la columna")
            break
        else:
            sudoku[fila][columna] = valor
            print(sudoku)
            tablero_completo = True
            break

    

