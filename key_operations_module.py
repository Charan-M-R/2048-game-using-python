def operation(mat, key):
    for row in range(0,4):
        updated_row = []
        
        for col in range(0,4):
            if mat[row][col] != 0:
                updated_row.append(mat[row][col])

        key_merge_numbers(updated_row)
        updated_row += [0]*(4 - len(updated_row))
        mat[row] = updated_row

def check_mat_full(mat):
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

def key_merge_numbers(mat_list):
    index = 0

    while index<len(mat_list)-1:
        if mat_list[index] == mat_list[index+1]:
            mat_list[index] *= 2
            mat_list.pop(index+1)
        index += 1

def rotate_matrix_clockwise(mat):
    #rotate outer row
    mat[0][0], mat[0][3], mat[3][3], mat[3][0] = mat[3][0], mat[0][0], mat[0][3], mat[3][3]
    mat[0][1], mat[1][3], mat[3][2], mat[2][0] = mat[2][0], mat[0][1], mat[1][3], mat[3][2] 
    mat[0][2], mat[2][3], mat[3][1], mat[1][0] = mat[1][0], mat[0][2], mat[2][3], mat[3][1]

    #rotate inner row
    mat[1][1], mat[1][2], mat[2][2], mat[2][1] = mat[2][1], mat[1][1], mat[1][2], mat[2][2]

def rotate_matrix_anti_clockwise(mat):
    #rotate outer row
    mat[0][0], mat[0][3], mat[3][3], mat[3][0] = mat[0][3], mat[3][3], mat[3][0], mat[0][0]
    mat[0][1], mat[1][3], mat[3][2], mat[2][0] = mat[1][3], mat[3][2], mat[2][0], mat[0][1]
    mat[0][2], mat[2][3], mat[3][1], mat[1][0] = mat[2][3], mat[3][1], mat[1][0], mat[0][2]

    #rotate inner row
    mat[1][1], mat[1][2], mat[2][2], mat[2][1] = mat[1][2], mat[2][2], mat[2][1], mat[1][1]