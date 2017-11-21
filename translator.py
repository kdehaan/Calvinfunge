import field


class Translator:

    stack = list()
    commands = dict()
    current_val = ''
    current_arg = 0
    string_mode = 0
    location = field.Field()

    def __init__(self):
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
            14: self.skip,
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
            26: self.right_momemtum,
            27: self.left_momemtum,
            28: self.up_momemtum,
            29: self.down_momemtum,
            30: self.cond_right,
            31: self.cond_down,
            32: self.string_toggle,
            33: self.duplicate,
            34: self.swap,
            35: self.pop_ascii,
            36: self.bridge,
            37: self.bridge_num,
            38: self.put,
            39: self.get,
            40: self.ask_num,
            41: self.ask_ascii,
            42: self.end
        }



    def do(self, arg):
        if not self.string_mode:
            self.current_arg = (self.current_arg + arg) % len(self.commands)
            self.commands[self.current_arg]()
            if arg == 0:
                self.current_arg = (self.current_arg + 9) % 28
        else:
            print(arg)

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

    def skip(self):

    def reflect(self):

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
        a = self.stack.pop()
        if a == 0:
            self.stack.append(1)
        else:
            self.stack.append(0)

    def greater_than(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(b > a) #might not work

    def right(self):

    def left(self):

    def up(self):

    def down(self):

    def right_momentum(self):

    def left_momentum(self):

    def up_momentum(self):

    def down_momentum(self):

    def cond_right(self):

    def cond_down(self):

    def string_toggle(self):
        self.string_mode = (self.string_mode + 1) % 2

    def duplicate(self):
        self.stack.append(self.stack[-1])

    def swap(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a)
        self.stack.append(b)

    def pop_ascii(self):
        a = self.stack.pop()
        print(a)

    def bridge(self):

    def bridge_num(self):

    def put(self):

    def get(self):

    def ask_num(self):
        self.stack.push(input("Number: "))

    def ask_ascii(self):
        self.stack.push(input("Ascii: "))

    def end(self):



