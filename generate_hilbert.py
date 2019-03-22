def main():
    N = 20

    matrix = [[0 for b in range(N)] for a in range(N)]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
                matrix[i - 1][j - 1] = 1/(i + j - 1)
    #print(matrix)

    #getting the values of b, given that x is always equal to 1
    x_vector = [1 for c in range(N)]

    row_counter = 0
    b_vector = []
    while row_counter < N:
        column_counter = 0
        summation = 0
        while column_counter < N:
            summation += matrix[row_counter][column_counter]
            column_counter += 1
        b_vector.append(summation)
        row_counter += 1
    #print(b_vector)
    file = open("hilbert3.txt", encoding='utf-8', mode='w')
    #creating input file_object

    file.write(str(N) + "\n")
    row_counter = 0

    while row_counter < N:
        column_counter = 0
        while column_counter < N:

            file.write(str(matrix[row_counter][column_counter]))
            file.write(", ")
            column_counter += 1
        file.write(str(b_vector[row_counter]))
        file.write('\n')
        row_counter += 1


main()
