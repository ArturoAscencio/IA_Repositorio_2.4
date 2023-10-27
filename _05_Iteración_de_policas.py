# _*_ coding: utf-8 _*_
#!/usr/bin/env python
# _*_ coding: cp1252 _*_
# _*_ cdoing: 850 _*_

# Definici�n del MDP (recompensas y transiciones)
# El MDP es una cuadr�cula de 3x3 con un estado objetivo (+1), un estado de trampa (-1) y estados normales (0).

mdp = [
    [0, 0, 0],
    [0, 1, -1],
    [0, 0, 0]
]

# Tama�o del MDP
num_rows = len(mdp)
num_cols = len(mdp[0])

# Pol�tica inicial (arriba, abajo, izquierda, derecha)
policy = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

# Par�metro de descuento (gamma)
gamma = 0.9

# Funci�n para calcular el valor de un estado dada la pol�tica actual
def calculate_state_value(row, col):
    action = policy[row][col]
    if action == 0:  # Arriba
        next_row = max(row - 1, 0)
        next_col = col
    elif action == 1:  # Abajo
        next_row = min(row + 1, num_rows - 1)
        next_col = col
    elif action == 2:  # Izquierda
        next_row = row
        next_col = max(col - 1, 0)
    else:  # Derecha
        next_row = row
        next_col = min(col + 1, num_cols - 1)
    return mdp[row][col] + gamma * state_values[next_row][next_col]

# Iteraci�n de pol�ticas
num_iterations = 100
for _ in range(num_iterations):
    state_values = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
    for row in range(num_rows):
        for col in range(num_cols):
            state_values[row][col] = calculate_state_value(row, col)

# Imprimir los valores de estado resultantes
for row in state_values:
    print(row)
