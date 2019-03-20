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
                coeffs.append(float(coeff))
                coeff_counter += 1
            matrix.append(coeffs)

        counter += 1
        luDecomp(matrix, num_rows)

def luDecomp(matrix, num_rows):

    upper = [[0 for y in range(num_rows)] for x in range(num_rows)]
    lower = [[0 for y in range(num_rows)] for x in range(num_rows)]
    print(str(upper))

    row_counter = 0
    while row_counter < num_rows:
        upper_counter = row_counter
        while upper_counter < num_rows:
            column_counter = 0
            sum2 = 0
            while column_counter < num_rows:
                sum2 += (lower[row_counter][column_counter] * upper[column_counter][upper_counter])
                column_counter += 1
            upper[row_counter][upper_counter] = matrix[row_counter][upper_counter] - sum2
            upper_counter += 1

        lower_counter = row_counter
        while lower_counter < num_rows:
            if lower_counter == row_counter:
                lower[row_counter][row_counter] = 1

            else:

                sum2 = 0
                column_counter = 0
                while column_counter < num_rows:
                    sum2 += (lower[row_counter][column_counter] * upper[column_counter][lower_counter])
                    column_counter += 1
                lower[lower_counter][row_counter] = matrix[lower_counter][row_counter] - sum2 /upper[row_counter][row_counter]
                lower_counter += 1
        row_counter += 1



main()
