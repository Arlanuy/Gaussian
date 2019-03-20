import ast

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
        else:
            array_of_coeffs = line.split(',' , num_rows + 1)
            array_of_coeffs[-1] = array_of_coeffs[-1][:-1]
            coeff_counter = 0
            coeffs = []
            for coeff in array_of_coeffs:
                coeffs.append(float(array_of_coeffs[coeff_counter]))
                coeff_counter += 1
                matrix.append(coeffs)
            print(str(coeffs)  + "\n")
        counter += 1
        #GaussianElim(matrix, num_rows)

def GaussianElim(matrix, num_rows):

    row_counter = 0
    while row_counter <= num_rows:
        column_counter  = 0
        while column_counter <= row_counter:
            matrix[row_counter]
            column_counter += 1
        row_counter += 1

main()
