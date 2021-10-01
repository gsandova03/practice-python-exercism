class Matrix:
    def __init__(self, matrix_string):
        self.Matrix = [[int(i) for i in e.split()]for e in matrix_string.split("\n")]
 
    def row(self, index):
        return self.Matrix[ index - 1 ]

    def column(self, index):
        column = []
        for row in self.Matrix:
            column.append( row[index-1] )
        return column
