def voltear_matriz_horizontal(matriz):
    # Aplicar la inversión horizontal a cada fila de la matriz
    matriz_volteada_horizontal = [fila[::-1] for fila in matriz]
    return matriz_volteada_horizontal

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

def suma_diagonal_principal(matriz):
    return sum(matriz[i][i] for i in range(len(matriz)))

def multiplicacion_diagonal_principal(matriz):
    result = 1
    for i in range(len(matriz)):
        result *= matriz[i][i]
    return result

def suma_contradiagonal(matriz):
    return sum(matriz[i][len(matriz)-1-i] for i in range(len(matriz)))

def multiplicacion_contradiagonal(matriz):
    result = 1
    for i in range(len(matriz)):
        result *= matriz[i][len(matriz)-1-i]
    return result

# Obtener la matriz volteada horizontalmente
matriz_volteada_horizontal = voltear_matriz_horizontal(matriz)

# Impresión de la matriz original y la matriz volteada horizontalmente
print("Matriz Original:")
for fila in matriz:
    print(fila)

print("\nMatriz Volteada Horizontalmente:")
for fila in matriz_volteada_horizontal:
    print(fila)

# Calcular y mostrar resultados para la matriz original
print("\nResultados para la Matriz Original:")
print("Suma Diagonal Principal:", suma_diagonal_principal(matriz))
print("Multiplicación Diagonal Principal:", multiplicacion_diagonal_principal(matriz))
print("Suma Contra Diagonal:", suma_contradiagonal(matriz))
print("Multiplicación Contra Diagonal:", multiplicacion_contradiagonal(matriz))

# Calcular y mostrar resultados para la matriz volteada horizontalmente
print("\nResultados para la Matriz Volteada Horizontalmente:")
print("Suma Diagonal Principal:", suma_diagonal_principal(matriz_volteada_horizontal))
print("Multiplicación Diagonal Principal:", multiplicacion_diagonal_principal(matriz_volteada_horizontal))
print("Suma Contra Diagonal:", suma_contradiagonal(matriz_volteada_horizontal))
print("Multiplicación Contra Diagonal:", multiplicacion_contradiagonal(matriz_volteada_horizontal))
