

class Field:

    # matrix notation, (0, 0) = top left, (3, 4) = 3 down and 4 right
    pointer_i = 0
    pointer_j = 0
    direction_i = 1
    direction_j = 0
    max_i = 0
    max_j = 0
    matrix = list()

    def __init__(self, filename):
        f = open(filename, 'r')

        for line in f:
            line = line.rstrip()
            line = list(line)

            if len(line) > self.max_j:
                self.max_j = len(line)

            self.matrix.append(line)
            self.max_i += 1
        print("I, J")
        print(self.max_i, self.max_j)

        for line in self.matrix:
            while len(line) < self.max_j:
                line.append(" ")


    def print_matrix(self):
        for line in self.matrix:
            print(line)

    def pointer_value(self):
        print(self.matrix[self.pointer_i][self.pointer_j])




