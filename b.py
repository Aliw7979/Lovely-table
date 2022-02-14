n = int(input())
selected_cells_in_row = [0 for i in range(n)]
selected_cells_in_col = [0 for i in range(n)]

number_of_empty_rows_cols = 2 * n
number_of_full_rows_cols = 0

for step in range(n * n):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    selected_cells_in_row[i] += 1
    selected_cells_in_col[j] += 1
    if(selected_cells_in_row[i] == 1):
        number_of_empty_rows_cols -= 1
    if(selected_cells_in_row[i] == n):
        number_of_full_rows_cols += 1
    if(selected_cells_in_col[j] == 1):
        number_of_empty_rows_cols -= 1
    if(selected_cells_in_col[j] == n):
        number_of_full_rows_cols += 1
    
    if(number_of_full_rows_cols == 0 and number_of_empty_rows_cols == 0):
        print("LOVELY")
    else:
        print("HIDEOUS")
