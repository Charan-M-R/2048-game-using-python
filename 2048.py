import random
import key_operations_module
import matrix_operations

mat = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

def key_operations(key):
    if key=='W' or key=='w':
        matrix_operations.rotate_matrix_anti_clockwise(mat)
        key_operations_module.operation(mat, key)
        matrix_operations.rotate_matrix_clockwise(mat)
            
    if key=='A' or key=='a':
        key_operations_module.operation(mat, key)

    if key=='S' or key=='s':
        matrix_operations.rotate_matrix_clockwise(mat)
        key_operations_module.operation(mat, key)
        matrix_operations.rotate_matrix_anti_clockwise(mat)

    if key=='D' or key=='d':
        matrix_operations.rotate_matrix_clockwise(mat)
        matrix_operations.rotate_matrix_clockwise(mat)
        key_operations_module.operation(mat, key)
        matrix_operations.rotate_matrix_clockwise(mat)
        matrix_operations.rotate_matrix_clockwise(mat)

def add_random_num():
    row = random.randint(0,3)
    col = random.randint(0,3)

    while mat[row][col] != 0:
        row = random.randint(0,3)
        col = random.randint(0,3)

    mat[row][col] = random.choice([2,2,2,4])

def print_mat():
    for row in range(0,4):
        for col in range(0,4):
            print(mat[row][col], end=' ')
        print()

def check_game_over(mat):
    if not matrix_operations.check_mat_full(mat):
        return []
        
    forbidden_operations = ['w','a','s','d']
    for i in range(0,4):
        if mat[i][0] == mat[i][1] or mat[i][1] == mat[i][2] or mat[i][2] == mat[i][3]:
            forbidden_operations.remove('a')
            forbidden_operations.remove('d')
            break
    for i in range(0,4):
        if mat[0][i] == mat[1][i] or mat[1][i] == mat[2][i] or mat[2][i] == mat[3][i]:
            forbidden_operations.remove('s')
            forbidden_operations.remove('w')
            break

    return forbidden_operations

if __name__ == "__main__":
    forbidden_operations = []
    while forbidden_operations != ['w','a','s','d']:
        key = input('\nEnter W,A,S,D: ')

        if key.lower() in forbidden_operations:
            print('Please enter another key\n')
            continue

        if key.lower() not in ['w','a','s','d']:
            print('Please enter a valid key\n')
            continue

        key_operations(key)        
        add_random_num()
        print_mat()
        forbidden_operations = check_game_over(mat)
    print('Game over, your score is:', max(max(mat[0]), max(mat[1]), max(mat[2]), max(mat[3])) )