import field


class Translator:

    stack = list()
    commands = dict()
    current_val = ''
    current_arg = 0

    def __init__(self, filename):

        self.field = field.Field(filename)
        self.current_val = self.field.pointer_value()

        self.commands = {
            0: self.push0,
            1: self.push1,
            2: self.push2,
            3: self.push3,
            4: self.push4,
            5: self.push5,
            6: self.push6,
            7: self.push7,
            8: self.push8,
            9: self.push9,
            10: self.skip,
            11: self.reflect,
            12: self.discard,
            13: self.reverse,
            14: self.teleport,
            15: self.add,
            16: self.subtract,
            17: self.multiply,
            18: self.divide,
            19: self.mod,
            20: self.logical_not,
            21: self.greater_than,
            22: self.right,
            23: self.left,
            24: self.up,
            25: self.down,
            26: self.right_momentum,
            27: self.left_momentum,
            28: self.up_momentum,
            29: self.down_momentum,
            30: self.cond_right,
            31: self.cond_down,
            32: self.print_value,
            33: self.duplicate,
            34: self.swap,
            35: self.print_ascii,
            36: self.bridge,
            37: self.bridge_num,
            38: self.put,
            39: self.get,
            40: self.ask_num,
            41: self.ask_ascii,
            42: self.push_a,
            43: self.push_A,
            44: self.shift_arg,
            45: self.end
        }
        self.num_commands = len(self.commands)

    def get_pointer_value(self):
        return self.field.pointer_value()

    def move_pointer(self):
        self.field.advance_pointer(1)
        self.current_val = self.field.pointer_value()

    def do(self, arg):

        if arg == ' ':
            self.skip()
            return True

        self.current_arg = (self.current_arg + arg) % self.num_commands

        print("running: ")
        print(self.current_arg)

        self.commands[self.current_arg]()
        if self.current_arg == (self.num_commands + 1):
            return False

        return True

    def push0(self):
        self.stack.append(0)

    def push1(self):
        self.stack.append(1)

    def push2(self):
        self.stack.append(2)

    def push3(self):
        self.stack.append(3)

    def push4(self):
        self.stack.append(4)

    def push5(self):
        self.stack.append(5)

    def push6(self):
        self.stack.append(6)

    def push7(self):
        self.stack.append(7)

    def push8(self):
        self.stack.append(8)

    def push9(self):
        self.stack.append(9)

    def discard(self):
        self.stack.pop()

    def reverse(self):
        self.stack.reverse()

    def teleport(self):
        j = self.stack.pop()
        i = self.stack.pop()
        self.field.set_pointer(i-self.field.momentum_i, j-self.field.momentum_i)

    def skip(self):
        return

    def reflect(self):
        self.field.reflect_momentum()

    def add(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a + b)

    def subtract(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b - a)

    def multiply(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b * a)

    def divide(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b / a)

    def mod(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b % a)

    def logical_not(self):
        v = self.stack.pop()
        if v == 0:
            self.stack.append(1)
        else:
            self.stack.append(0)

    def greater_than(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b > a) #might not work

    def right(self):
        self.field.set_j_momentum(1)
        self.field.set_i_momentum(0)

    def left(self):
        self.field.set_j_momentum(-1)
        self.field.set_i_momentum(0)

    def up(self):
        self.field.set_j_momentum(0)
        self.field.set_i_momentum(-1)

    def down(self):
        self.field.set_j_momentum(0)
        self.field.set_i_momentum(1)

    def right_momentum(self):
        self.field.set_j_momentum(1)

    def left_momentum(self):
        self.field.set_j_momentum(-1)

    def up_momentum(self):
        self.field.set_i_momentum(-1)

    def down_momentum(self):
        self.field.set_i_momentum(1)

    def cond_right(self):
        v = self.stack.pop()
        if v == 0:
            self.left()
        else:
            self.right()

    def cond_down(self):
        v = self.stack.pop()
        if v == 0:
            self.up()
        else:
            self.down()

    def push_a(self):
        self.stack.append(97)

    def push_A(self):
        self.stack.append(65)

    def duplicate(self):
        self.stack.append(self.stack[-1])

    def swap(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a)
        self.stack.append(b)

    def print_value(self):
        v = self.stack.pop()
        print(v, end='')

    def print_ascii(self):
        v = self.stack.pop()
        print(chr(v), end='')

    def bridge(self):
        self.field.advance_pointer(1)

    def bridge_num(self):
        v = self.stack.pop()
        self.field.advance_pointer(v)

    def put(self):
        v = self.stack.pop()
        j = self.stack.pop()
        i = self.stack.pop()
        self.field.set_matrix(i, j, v)

    def get(self):
        j = self.stack.pop()
        i = self.stack.pop()
        v = self.field.get_matrix(i, j)
        self.stack.append(v)

    def ask_num(self):
        self.stack.append(input("Number: "))

    def ask_ascii(self):
        self.stack.append(input("Ascii: "))

    def shift_arg(self):
        v = self.stack.pop()
        self.current_arg = (self.current_arg + v) % self.num_commands

    def end(self):
        print("Ending")
        return
