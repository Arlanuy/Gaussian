
'''
Arlan Vincent Uy
2015-09385
CS 131 THU
'''

#Can only solve n x n matrix and matrix who doesn't need pivoting
'''
Input: "gauss_input1.txt"
Method: Implements the file input system and the parsing of the matrix coefficients
We also built a list within a list matrix here
'''

def main():
     file_object = open("gauss_input1.txt", "r")

     counter = 0
     num_rows = 0
     matrix = []

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
            for coeff in array_of_coeffs:
                coeffs.append(float(coeff))
                coeff_counter += 1
            matrix.append(coeffs)

        counter += 1
     GaussianElim(matrix, num_rows)

     findMyExes(matrix, num_rows)
'''
Input: matrix: the 2-dimensional created from main method
num_rows: the size of the matrix, the N from the N X N matrix
Method: Finds the solution set X, given the final output of the GaussianElim method
'''
def findMyExes(matrix, num_rows):
    x_vector = []
    row_counter = num_rows - 1

    while row_counter >= 0:
        column_counter = num_rows - 1
        summation = matrix[row_counter][num_rows]
        if row_counter == num_rows - 1:
            x_last = matrix[row_counter][num_rows]/matrix[row_counter][num_rows - 1]
            x_vector.insert(0, x_last)

        #print("x vector is " + str(x_vector))
        while column_counter > row_counter:

             if row_counter != num_rows - 1:
                 index_x_vector = -1 + (column_counter - num_rows + 1)
                 #print("x vector is " + str(x_vector) + "\n")
                # print("index_x_vector and row_counter and column_counter are " + str(index_x_vector) + str(row_counter) + str(column_counter) + "\n")
                 summation -= x_vector[index_x_vector] * matrix[row_counter][column_counter]
                 #print("summation is " + str(summation) + "\n")
             column_counter -= 1
        if row_counter != num_rows - 1:
            #print("numerator is " + str(matrix[row_counter][column_counter]) + "\n" + " while summation is " + str(summation) + " while quotient is " +  str(matrix[row_counter][column_counter]/summation))
            x_vector.insert(0, summation/matrix[row_counter][column_counter])
        row_counter -= 1
    file = open("gaussian_output.txt", encoding='utf-8', mode='w')
    file.write("The solution is " + str(x_vector))
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
