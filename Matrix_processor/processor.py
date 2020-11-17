import numpy


class Processor:
    selection = None

    def main(self):
        choices = {'1.': 'Add Matrices',
                   '2.': 'Multiply matrix by a constant',
                   '3.': 'Multiply matrices',
                   '4.': 'Transpose matrix',
                   '5.': 'Calculate a determinant',
                   '6.': 'Inverse matrix',
                   '0.': 'Exit'}
        while True:
            for k, v in choices.items():
                print(k, v)

            Processor.selection = input('Your choice: ')
            try:
                Processor.selection = int(Processor.selection)
                if Processor.selection == 1:
                    self.addition()
                elif Processor.selection == 2:
                    self.multi_scal()
                elif Processor.selection == 3:
                    self.multi_mat()
                elif Processor.selection == 4:
                    self.trans_mat()
                elif Processor.selection == 5:
                    self.det_mat()
                elif Processor.selection == 6:
                    self.inv_mat()
                elif Processor.selection == 0:
                    print('Bye')
                    exit()
                else:
                    print('Invalid selection')
                    continue
            except ValueError:
                print('Invalid selection')
                continue

    def addition(self):
        a, b = map(int, input('Enter size of first matrix: ').split())
        A = Matrix(a, b)
        print('Enter first matrix')
        A.read_mat()
        a, b = map(int, input('Enter size of second matrix: ').split())
        B = Matrix(a, b)
        print('Enter second matrix')
        B.read_mat()
        Matrix.mat_add(A, B)

    def multi_scal(self):
        a, b = map(int, input('Enter size of matrix: ').split())
        A = Matrix(a, b)
        print('Enter matrix')
        A.read_mat()
        c = float(input('Enter constant: '))
        Matrix.mat_scal(A, c)

    def multi_mat(self):
        a, b = map(int, input('Enter size of first matrix: ').split())
        A = Matrix(a, b)
        print('Enter first matrix')
        A.read_mat()
        a, b = map(int, input('Enter size of second matrix: ').split())
        B = Matrix(a, b)
        print('Enter second matrix')
        B.read_mat()
        Matrix.mat_mat(A, B)

    def trans_mat(self):
        trans_choices = {'1.': 'Main diagonal',
                         '2.': 'Side diagonal',
                         '3.': 'Vertical line',
                         '4.': 'Horizontal line',
                         '0.': 'Return'}

        for k, v in trans_choices.items():
            print(k, v)
        trans_selection = int(input('Your choice: '))
        a, b = map(int, input('Enter size of matrix: ').split())
        A = Matrix(a, b)
        print('Enter matrix')
        A.read_mat()
        if trans_selection == 1:
            Matrix.m_diag_trans(A)
        elif trans_selection == 2:
            Matrix.s_diag_trans(A)
        elif trans_selection == 3:
            Matrix.v_line_trans(A)
        elif trans_selection == 4:
            Matrix.h_line_trans(A)
        else:
            print('Invalid selection')
            # continue

    def det_mat(self):
        a, b = map(int, input('Enter matrix size: ').split())
        A = Matrix(a, b)
        print('Enter matrix:')
        A.read_mat()
        print(determinant_recursive(A.matrix), '\n')

    def inv_mat(self):
        a, b = map(int, input('Enter matrix size: ').split())
        A = Matrix(a, b)
        INV = Matrix(a, b)
        print('Enter matrix:')
        A.read_mat()
        if not A.check_squareness() or determinant_recursive(A.matrix) == 0:
            print('Inverse matrix cannot be obtained')
            return
        Matrix.inversion(A)


def copy_matrix(A):
    return A


def determinant_recursive(A, total=0):
    # Section 1: store indices in list for row referencing
    indices = list(range(len(A)))
    if len(A) == 1:
        return A[0][0]
    # Section 2: when at 2x2 submatrices recursive calls end
    elif len(A) == 2 and len(A[0]) == 2:
        val = A[0][0] * A[1][1] - A[1][0] * A[0][1]
        return val

    for fc in indices:
        As = copy_matrix(A)
        As = As[1:]
        height = len(As)
        for i in range(height):
            As[i] = As[i][0:fc] + As[i][fc + 1:]
        sign = (-1) ** (fc % 2)  # F)
        # G) pass submatrix recursively
        sub_det = determinant_recursive(As)
        # H) total all returns from recursion
        total += sign * A[0][fc] * sub_det
    return total


class Matrix:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.matrix = []

    def read_mat(self):
        for i in range(self.row):
            a = list(map(float, input().split()))
            self.matrix.append(a)

    def print_mat(self):
        print('The result is:')
        for i in range(self.row):
            print(*self.matrix[i][:])
        print()

    def check_squareness(self):
        return True if self.row == self.column else False

    @staticmethod
    def mat_add(mat1, mat2):
        if (mat1.row != mat2.row) or (mat1.column != mat2.column):
            print('ERROR')
        else:
            result = Matrix(mat1.row, mat1.column)
            result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
            for i in range(result.row):
                for j in range(result.column):
                    result.matrix[i][j] = mat1.matrix[i][j] + mat2.matrix[i][j]
            result.print_mat()

    @staticmethod
    def mat_scal(mat1, scal):
        result = Matrix(mat1.row, mat1.column)
        result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
        for i in range(result.row):
            for j in range(result.column):
                result.matrix[i][j] = mat1.matrix[i][j] * scal
        result.print_mat()

    @staticmethod
    def mat_mat(mat1, mat2):
        if mat1.column != mat2.row:
            print('ERROR')
        else:
            result = Matrix(mat1.row, mat2.column)
            result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
            for i in range(mat1.row):
                for j in range(mat2.column):
                    for k in range(mat2.row):
                        result.matrix[i][j] += mat1.matrix[i][k] * mat2.matrix[k][j]
            result.print_mat()

    @staticmethod
    def m_diag_trans(mat1):
        result = Matrix(mat1.column, mat1.row)
        result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
        for i in range(result.row):
            for j in range(result.column):
                result.matrix[i][j] = mat1.matrix[j][i]
        result.print_mat()

    @staticmethod
    def s_diag_trans(mat1):
        result = Matrix(mat1.column, mat1.row)
        result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
        for i in range(result.row):
            for j in range(result.column):
                result.matrix[i][j] = mat1.matrix[-j - 1][-i - 1]
        result.print_mat()

    @staticmethod
    def v_line_trans(mat1):
        result = Matrix(mat1.row, mat1.column)
        result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
        for i in range(result.row):
            for j in range(result.column):
                result.matrix[i][j] = mat1.matrix[i][-j - 1]
        result.print_mat()

    @staticmethod
    def h_line_trans(mat1):
        result = Matrix(mat1.row, mat1.column)
        result.matrix = [[0 for i in range(result.column)] for j in range(result.row)]
        for i in range(result.row):
            for j in range(result.column):
                result.matrix[i][j] = mat1.matrix[-i - 1][j]
        result.print_mat()

    @staticmethod
    def inversion(mat1):
        inverted = numpy.linalg.inv(mat1.matrix)
        print('The result is:')
        for i in range(mat1.row):
            print(*inverted[i][:])
        print()


start = Processor()
start.main()
