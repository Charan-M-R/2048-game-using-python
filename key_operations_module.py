def operation(mat, key):
    for row in range(0,4):
        updated_row = []
        
        for col in range(0,4):
            if mat[row][col] != 0:
                updated_row.append(mat[row][col])

        key_merge_numbers(updated_row)
        updated_row += [0]*(4 - len(updated_row))
        mat[row] = updated_row



def key_merge_numbers(mat_list):
    index = 0

    while index<len(mat_list)-1:
        if mat_list[index] == mat_list[index+1]:
            mat_list[index] *= 2
            mat_list.pop(index+1)
        index += 1