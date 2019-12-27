#
#
# Matrix Operations  
#
# 

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Enter a new matrix')
    print('(1) Negate the matrix')
    print('(2) Multiply a row by a constant')
    print('(3) Add one row to another')
    print('(4) Add a multiple of one row to another')
    print('(5) Transpose the matrix')
    print('(6) Quit')
    print()

def print_matrix(matrix):
    """ prints the specified matrix in rectangular form.
        input: matrix is a rectangular 2-D list numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print('%6.2f' % matrix[r][c], end=' ')
        print()
       
def get_matrix():
    """ gets a new matrix from the user and returns it
    """
    matrix = eval(input('Enter a new 2-D list of numbers: '))
    return matrix

def negate_matrix(matrix):
    """ negates all of the elements in the specified matrix
        inputs: matrix is a rectangular 2-D list of numbers
    """
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            matrix[r][c] *= -1
    # We don't need to return the matrix!
    # All changes to the matrix will still be there when the
    # function returns, because we received a copy of the
    # *reference* to the matrix used by main().

### Add your functions for options 2-5 here. ###

def mult_row(matrix, r, m):
    """Input a matrix, a row number r, and a mutlipier m. The function will return the matrix
       with its row number r mutlpied by m"""
    for i in range(len(matrix[r])):
        matrix[r][i] *= m 

def add_row_into(matrix, source, dest):
    """Input a matrix, a source row, and a destination row. Then, the function takes the
       matrix adds each element of the row with the source row to the corresponding element
       of the row with the destination row."""
    for i in range(len(matrix[0])):
        matrix[dest][i] += matrix[source][i]

def add_mult_row_into(matrix, m, source, dest):
    for i in range(len(matrix[0])):
        m_row = matrix[source][i] * m
        matrix[dest][i] += m_row

def transpose(matrix):
    m = len(matrix)
    n = len(matrix[0])
    if n > m:
        new_matrix2 = [0]
        new_matrix2 *= m
        new_matrix = [new_matrix2]
        for i in range((n - 1)):
            new_matrix2 = new_matrix2[:]
            new_matrix += [new_matrix2]
        for j in range(len(new_matrix)):
                     for k in range(len(new_matrix[0])):
                                  new_matrix[j][k] = matrix[k][j]
    if n < m:
        new_matrix2 = [0]
        new_matrix2 *= m
        new_matrix = [new_matrix2]
        for i in range((n - 1)):
            new_matrix2 = new_matrix2[:]
            new_matrix += [new_matrix2]
        for j in range(len(new_matrix[0])):
            for k in range(len(new_matrix)):
                         new_matrix[k][j] = matrix[j][k]
    if n == m:
        new_matrix2 = [0]
        new_matrix2 *= m
        new_matrix = [new_matrix2]
        for i in range((n - 1)):
            new_matrix2 = new_matrix2[:]
            new_matrix += [new_matrix2]
        for j in range(len(matrix)):
            for k in range(len(matrix[0])):
                         new_matrix[k][j] = matrix[j][k]
    return new_matrix
                                  
    
    
    

def main():
    """ the main user-interaction loop
    """
    ## The default starting matrix.
    ## DO NOT CHANGE THESE LINES.
    matrix = [[ 1,  2,  3,  4],
              [ 5,  6,  7,  8],
              [ 9, 10, 11, 12]]

    while True:
        print()
        print_matrix(matrix)
        display_menu()
        choice = int(input('Enter your choice: '))

        if choice == 0:
            matrix = get_matrix()
        elif choice == 1:
            negate_matrix(matrix)
        elif choice == 2:
            row = int(input('Index of row: '))
            mut = (input('Multiplier: '))
            if '.' in mut:
                mut = float(mut)
            else:
                mut = int(mut)
            mult_row(matrix, row, mut)
        elif choice == 3:
            source_row = int(input('Index of source row: '))
            destination_row = int(input('Index of destination row: '))
            add_row_into(matrix, source_row, destination_row)
        elif choice == 4:
            source_row = int(input('Index of source row: '))
            destination_row = int(input('Index of destination row: '))
            multiplier = (input('Multiplier: '))
            if '.' in multiplier:
                multiplier = float(multiplier)
            else:
                multiplier = int(multiplier)
            add_mult_row_into(matrix, multiplier, source_row, destination_row)
        elif choice == 5:
            matrix = transpose(matrix)
        elif choice == 6:
            break
        else:
            print('Invalid choice. Try again.')
