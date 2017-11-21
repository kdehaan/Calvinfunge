

class Field:

    # matrix notation, (0, 0) = top left, (3, 4) = 3 down and 4 right
    pointer_i = 0
    pointer_j = 0
    momentum_i = 0
    momentum_j = 1
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
        return self.matrix[self.pointer_i][self.pointer_j]
        # print()

    def displace_pointer(self, i, j):
        self.pointer_i = (self.pointer_i + i) % self.max_i
        self.pointer_j = (self.pointer_j + j) % self.max_j

    def set_pointer(self, i, j):
        self.pointer_i = i % self.max_i
        self.pointer_j = j % self.max_j

    def set_momentum(self, i, j):
        self.momentum_i = i
        self.momentum_j = j

    def reflect_momentum(self):
        self.momentum_i = -self.momentum_i
        self.momentum_j = -self.momentum_j

    def sigmoid(self, value):
        if value > 1:
            value = 1
        if value < -1:
            value = -1
        return value



