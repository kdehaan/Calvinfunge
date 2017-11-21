

class Field:

    # 'sort-of' matrix notation, (0, 0) = top left, (3, 4) = 3 right and 4 down
    pointer_j = 0
    pointer_i = 0
    direction_j = 1
    direction_i = 0

    def __init__(self, filename):
