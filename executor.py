import translator


class Executor:
    map = dict()

    def __init__(self, filename):
        self.translator = translator.Translator(filename)

        self.inputs = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15,
            "!": 16,
            "@": 17,
            "#": 18,
            "$": 19,
            "%": 20,
            "^": 21,
            "&": 22,
            "*": 23,
            "(": 24,
            ")": 25,
            "-": 26,
            "=": 27,
            "_": 28,
            "+": 29,
            "[": 30,
            "]": 31,
            "{": 32,
            "}": 33,
            ";": 34,
            ":": 35,
            ",": 36,
            ".": 37,
            "/": 38,
            "<": 39,
            ">": 40,
            "?": 41,
            "~": 42,
            "n": 43,
            "'": 44,
            "|": 45,
        }

        self.execute()

    def execute(self):
        while True:
            cursor = self.translator.current_val
            try:
                instruction = self.inputs[cursor]
            except KeyError:
                instruction = cursor
            cont = self.translator.do(instruction)
            self.translator.move_pointer()
            if not cont:
                break
