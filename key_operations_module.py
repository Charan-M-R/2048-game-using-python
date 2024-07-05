def operation(mat, key):
    for row in range(0,4):
        updated_row = []

        for col in range(0,4):
            if mat[row][col] != 0:
                updated_row.append(mat[row][col])

        if key.lower() == 'a':
            key_merge_numbers(updated_row)
            updated_row += [0]*(4 - len(updated_row))
        if key.lower() == 'd':
            updated_row.reverse()
            key_merge_numbers(updated_row)
            updated_row.reverse()
            updated_row = [0]*(4 - len(updated_row)) + updated_row
        mat[row] = updated_row

def key_merge_numbers(mat_list):
    index = 0

    while index<len(mat_list)-1:
        if mat_list[index] == mat_list[index+1]:
            mat_list[index] *= 2
            mat_list.pop(index+1)
        index += 1













def a_key_operation(mat):
    for row in range(0,4):
        updated_row = []

        for col in range(0,4):
            if mat[row][col] != 0:
                updated_row.append(mat[row][col])

        a_key_merge_numbers(updated_row)
        updated_row += [0]*(4 - len(updated_row))
        mat[row] = updated_row

def a_key_merge_numbers(mat_list):
    index = 0

    while index<len(mat_list)-1:
        if mat_list[index] == mat_list[index+1]:
            mat_list[index] *= 2
            mat_list.pop(index+1)
        index += 1

def d_key_operation(mat):
    for row in range(0,4):
        updated_row = []

        for col in range(0,4):
            if mat[row][col] != 0:
                updated_row.append(mat[row][col])

        d_key_merge_numbers(updated_row)
        updated_row = [0]*(4 - len(updated_row)) + updated_row
        mat[row] = updated_row

def d_key_merge_numbers(mat_list):
    mat_list.reverse()
    a_key_merge_numbers(mat_list)
    mat_list.reverse()

