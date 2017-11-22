import translator


class Executor:
    map = dict()

    def __init__(self, filename):
        self.translator = translator.Translator(filename)

        self.execute()

    def execute(self):
        while True:
            cursor = self.translator.current_val
            cont = self.translator.do(cursor)
            self.translator.move_pointer()
            if not cont:
                break

