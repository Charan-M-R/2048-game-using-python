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
        print('W is entered')
            
    if key=='A' or key=='a':
        key_operations_module.operation(mat, key)

    if key=='S' or key=='s':
        print('S is entered')

    if key=='D' or key=='d':
        key_operations_module.operation(mat, key)

def check_mat_full():
    #check for moves that still be performed
    mat_full = True

    for row in range(0,4):
        for col in range(0,4):
            if mat[row][col] == 0:
                mat_full = False
                break
        else:
            continue
        break

    return mat_full

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
    while(not check_mat_full()):
        key = input('\nEnter W,A,S,D: ')
        key_operations(key)        
        add_random_num()
        print_mat()

    print('Game over noob, you lost loser')