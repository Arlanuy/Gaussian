'''
Uy, Arlan Vincent
2015-09385
CS 131 THU

Juico, Jules Gerard E.
2014-40314
CS 131 THU
'''

'''
Input: "doolittle_input1.txt"
Method: Implements the file input system and the parsing of the matrix coefficients
We also built a list within a list matrix here and created two copies of it
'''
def main():
     file_object = open("doolittle_input0.txt", "r")

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

     b_vector = []
     lower_matrix = creatingLower(matrix, num_rows, orig_matrix, b_vector)
     #print("b_vector is " + str(b_vector))
     y_vector = findMyExesLower(lower_matrix, num_rows, b_vector)
     x_vector = findMyExesUpper(matrix, num_rows, y_vector)
    # print(str(y_vector))
     file = open("doolittle_output0.txt", encoding='utf-8', mode='w')
     file.write("Solution is: ")
     file.write(str(x_vector) + "\n")

'''
Input: matrix: the 2-dimensional created from main method
num_rows: the size of the matrix, the N from the N X N matrix
Method: Finds the solution set X, given the final matrix form of the GaussianElim method
'''
def findMyExesLower(matrix, num_rows, a_vector):
    row_counter = 0
    y_vector = []
    while row_counter < num_rows:
        column_counter = 0
        summation = a_vector[row_counter]
        if row_counter == 0:
            x_first = a_vector[row_counter]
            y_vector.insert(0, x_first)

        #print("x vector is " + str(x_vector))
        while column_counter < row_counter:

             if row_counter != 0:
                 index_x_vector = column_counter
                 #print("x vector is " + str(x_vector) + "\n")
                # print("index_x_vector and row_counter and column_counter are " + str(index_x_vector) + str(row_counter) + str(column_counter) + "\n")
                 summation = summation - y_vector[index_x_vector] * matrix[row_counter][column_counter]
                 #print("summation is " + str(summation) + "\n")
             column_counter += 1
        if row_counter != 0:
            #print("numerator is " + str(matrix[row_counter][column_counter]) + "\n" + " while summation is " + str(summation) + " while quotient is " +  str(matrix[row_counter][column_counter]/summation))
            y_vector.insert(0, summation/matrix[row_counter][column_counter])
        row_counter += 1
    return y_vector


'''
Input: matrix: the 2-dimensional created from main method
num_rows: the size of the matrix, the N from the N X N matrix
Method: Finds the solution set X, given the final matrix form of the method findMyExesLower
'''
def findMyExesUpper(matrix, num_rows, a_vector):
    row_counter = num_rows - 1
    x_vector = []
    while row_counter >= 0:
        column_counter = num_rows - 1
        summation = a_vector[row_counter]
        if row_counter == num_rows - 1:
            x_last = matrix[row_counter][num_rows]/matrix[row_counter][num_rows - 1]
            x_vector.insert(0, x_last)

        #print("x vector is " + str(x_vector))
        while column_counter > row_counter:

             if row_counter != num_rows - 1:
                 index_x_vector = -1 + (column_counter - num_rows + 1)
                 #print("x vector is " + str(x_vector) + "\n")
                # print("index_x_vector and row_counter and column_counter are " + str(index_x_vector) + str(row_counter) + str(column_counter) + "\n")
                 summation = summation - x_vector[index_x_vector] * matrix[row_counter][column_counter]
                 #print("summation is " + str(summation) + "\n")
             column_counter -= 1
        if row_counter != num_rows - 1:
            #print("numerator is " + str(matrix[row_counter][column_counter]) + "\n" + " while summation is " + str(summation) + " while quotient is " +  str(matrix[row_counter][column_counter]/summation))
            x_vector.insert(0, summation/matrix[row_counter][column_counter])
        row_counter -= 1
    return x_vector

#
'''
Input: matrix: is now the upper triangular matrix
num_rows: size of the original orig_matrix
orig_matrix: The original matrix before its reduction to lower triangular orig_matrix

Method: In here, we create the lower triangular matrix and print it accordingly
'''
def creatingLower(matrix, num_rows, orig_matrix, b_vector):
    row_counter = 0
    lower_matrix = [[0 for i in range(num_rows)] for j in range(num_rows)]
    GaussianElim(matrix, num_rows)
    #print("orig matrix is " + str(orig_matrix))
    j = 0
    for row in orig_matrix:
        i = 0
        while i <= num_rows:
            if i == num_rows:
                b_vector.append(matrix[j][i])
            i += 1
        j += 1

    print("upper matrix is " )
    j = 0
    for row in matrix:
        i = 0
        print("[ ", end = ' ')
        while i != num_rows:
            print(str(matrix[j][i]), end = ', ')
            if i == j:
                lower_matrix[j][i] = 1
            i += 1
        j += 1
        print("]", end = ' ')
    print("\n")
    while row_counter < num_rows:
        column_counter  = 0
        while column_counter < row_counter:

            k = 0
            summation = 0
            while k < column_counter:
                summation += matrix[k][column_counter] * lower_matrix[row_counter][k]
                #print("k is " + str(k) + " and cc is " + str(column_counter) + " and rc is " + str(row_counter) + "\n")
                #print("summation is " + str(summation) + " with 1st elem" + str(matrix[k][column_counter]) + " with 2nd elem " + str(lower_matrix[row_counter][k]) +"\n")
                k+= 1
            #print("minuend is " + str(orig_matrix[row_counter][column_counter]) + "\n")
            lower_matrix[row_counter][column_counter] = (orig_matrix[row_counter][column_counter] - summation)/matrix[column_counter][column_counter]

            #print("lower_matrix is " + str(lower_matrix[row_counter][column_counter]) + " calculating difference of " + str(orig_matrix[row_counter][column_counter]) + " and " + str(summation)  + "\n")
            column_counter += 1
        row_counter += 1
    print("lower matrix is \n" + str(lower_matrix))
    return lower_matrix

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
