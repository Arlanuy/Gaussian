
'''
Arlan Vincent Uy
2015-09385
CS 131 THU
'''

'''
Input: "doolittle_input1.txt"
Method: Implements the file input system and the parsing of the matrix coefficients
We also built a list within a list matrix here and created two copies of it
'''
def main():
     file_object = open("doolittle_input1.txt", "r")

     counter = 0
     num_rows = 0
     matrix = []
     orig_matrix = []
     for line in file_object:
        line_counter = 0
        if counter == 0:
            while line[line_counter] != '\n':
                num_rows = num_rows + (ord(line[line_counter]) - ord('0'))
                num_rows *= 10
                line_counter += 1
            num_rows /= 10
            num_rows = int(num_rows)
        else:
            array_of_coeffs = line.split(',' , num_rows + 1)
            array_of_coeffs[-1] = array_of_coeffs[-1][:-1]
            coeff_counter = 0
            coeffs = []
            orig_coeffs = []
            for coeff in array_of_coeffs:
                coeffs.append(float(coeff))
                orig_coeffs.append(float(coeff))
                coeff_counter += 1
            matrix.append(coeffs)
            orig_matrix.append(orig_coeffs)

        counter += 1

     creatingLower(matrix, num_rows, orig_matrix)

#
'''
Input: matrix: is now the upper triangular matrix
num_rows: size of the original orig_matrix
orig_matrix: The original matrix before its reduction to lower triangular orig_matrix

Method: In here, we create the lower triangular matrix and print it accordingly
'''
def creatingLower(matrix, num_rows, orig_matrix):
    row_counter = 0
    lower_matrix = [[0 for i in range(num_rows)] for j in range(num_rows)]
    GaussianElim(matrix, num_rows)
    #print("orig matrix is " + str(orig_matrix))
    print("upper matrix is " )
    j = 0
    for row in matrix:
        i = 0
        print("[ ", end = ' ')
        while i != num_rows:
            print(str(matrix[j][i]), end = ', ')
            i += 1
        j += 1
        print("]", end = ' ')
    print("\n")
    while row_counter < num_rows:
        column_counter  = 0
        while column_counter < num_rows:
            if row_counter == column_counter:
                lower_matrix[row_counter][column_counter] = 1

            else:
                k = 0
                summation = 0
                while k < column_counter:
                    summation += matrix[k][column_counter] * lower_matrix[row_counter][k]
                    #print("k is " + str(k) + " and cc is " + str(column_counter) + " and rc is " + str(row_counter) + "\n")
                #    print("summation is " + str(summation) + " with 1st elem" + str(matrix[k][column_counter]) + " with 2nd elem " + str(lower_matrix[row_counter][k]) +"\n")
                    k+= 1
                lower_matrix[row_counter][column_counter] = orig_matrix[row_counter][column_counter] - summation
                #print("lower_matrix is " + str(lower_matrix[row_counter][column_counter]) + " calculating difference of " + str(orig_matrix[row_counter][column_counter]) + " and " + str(summation)  + "\n")
            column_counter += 1
        row_counter += 1
    print("lower matrix is \n" + str(lower_matrix))

'''
Input: matrix: the matrix from the GaussianElim method
row: the current row to be scaled
pivot_index: the row index associated with the pivot being used at the moment
multiplier: The number that will be multiplied on all of the coefficients in the current row
num_rows: size of matrix
Method: Scales the current row in order to zero out an element in the current row
'''
def scaleRow(matrix, row, pivot_index, multiplier, num_rows):
    counter = pivot_index
    while counter <= num_rows:
        row[counter] = (row[counter] * multiplier) + matrix[pivot_index][counter]
        counter += 1

'''
Input: matrix from the main method
num_rows: size of the matrix
Method: Uses all of the steps associated with the Gaussian Elimination method
'''
def GaussianElim(matrix, num_rows):

    row_counter = 0
    while row_counter < num_rows:
        column_counter  = 0
        while column_counter < row_counter:
            pivot = matrix[column_counter][column_counter]
            current = matrix[row_counter][column_counter]
            if current != 0:
                multiplier = (pivot / current) * -1
                scaleRow(matrix, matrix[row_counter], column_counter, multiplier, num_rows)
            column_counter += 1
        row_counter += 1
main()
