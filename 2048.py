import random
import key_operations_module

mat = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
]

def key_operations(key):
    if key=='W' or key=='w':
        key_operations_module.rotate_matrix_anti_clockwise(mat)
        key_operations_module.operation(mat, key)
        key_operations_module.rotate_matrix_clockwise(mat)
            
    if key=='A' or key=='a':
        key_operations_module.operation(mat, key)

    if key=='S' or key=='s':
        key_operations_module.rotate_matrix_clockwise(mat)
        key_operations_module.operation(mat, key)
        key_operations_module.rotate_matrix_anti_clockwise(mat)

    if key=='D' or key=='d':
        key_operations_module.rotate_matrix_clockwise(mat)
        key_operations_module.rotate_matrix_clockwise(mat)
        key_operations_module.operation(mat, key)
        key_operations_module.rotate_matrix_clockwise(mat)
        key_operations_module.rotate_matrix_clockwise(mat)

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

if __name__ == "__main__":
    while(not key_operations_module.check_mat_full(mat)):
        key = input('\nEnter W,A,S,D: ')
        key_operations(key)        
        add_random_num()
        print_mat()
    print('Game over noob, you lost loser')