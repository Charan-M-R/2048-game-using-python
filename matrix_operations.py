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