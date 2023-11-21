def imprimir_tablero(tablero):
    for i, fila in enumerate(tablero):
        print(" " + " | ".join(fila))
        if i < len(tablero) - 1:
            print("---|---|---")


def imprimir_jugada(jugada):

    print(f"It's {jugada} turn:")

    row = int(input('Insert the row of your play: '))
    column = int(input('Insert the column of your play: '))

    if tablero[row][column] == ' ':
        tablero[row][column] = jugada
        imprimir_tablero(tablero)
    else:
        print("square already occupied, try again:")
        imprimir_jugada(jugada)


def check_win(tablero):
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != ' ':
            return True

    for col in range(3):
        if tablero[0][col] == tablero[1][col]==tablero[2][col] != ' ':
            return True

    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return True
    if tablero[2][0] == tablero[1][1] == tablero[0][2] != ' ':
        return True

    return False


# Inicializar el tablero - Initializing Board
tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Imprimir el tablero - Printing the Board
imprimir_tablero(tablero)
print('--------------------------------------------------------')

# Game it's On
game_is_on = True
while game_is_on:
    imprimir_jugada('X')
    if check_win(tablero):
        print('X Wins')
        break
    imprimir_jugada('O')
    game_is_on = not(check_win(tablero))
