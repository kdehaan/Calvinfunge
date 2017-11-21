


class Translator:

    stack = list()
    commands = dict()
    current_val = ''
    current_arg = 0

    def __init__(self):
        self.commands = {
            0: self.skip,
            1: self.push,
            2: self.pop,
            3: self.peek,
            4: self.skip,
            5: self.add,
            6: self.subtract,
            7: self.multiply,
            8: self.divide,
            9: self.mod,
            10: self.logical_not,
            11: self.greater_than,
            12: self.right,
            13: self.left,
            14: self.up,
            15: self.down,
            16: self.cond_right,
            17: self.cond_down,
            18: self.string_toggle,
            19: self.duplicate,
            20: self.swap,
            21: self.pop_ascii,
            22: self.bridge,
            23: self.bridge_num,
            24: self.put,
            25: self.get,
            26: self.ask_num,
            27: self.ask_ascii,
            28: self.end
        }



    def do(self, arg):
        self.current_arg = (self.current_arg + arg) % 28
        self.commands[self.current_arg]()


    def push(self):

    def pop(self):

    def peek(self):

    def skip(self):

    def add(self):

    def subtract(self):

    def multiply(self):

    def divide(self):

    def mod(self):

    def logical_not(self):

    def greater_than(self):

    def right(self):

    def left(self):

    def up(self):

    def down(self):

    def cond_right(self):

    def cond_down(self):

    def string_toggle(self):

    def duplicate(self):

    def swap(self):

    def pop_ascii(self):

    def bridge(self):

    def bridge_num(self):

    def put(self):

    def get(self):

    def ask_num(self):

    def ask_ascii(self):

    def end(self):



