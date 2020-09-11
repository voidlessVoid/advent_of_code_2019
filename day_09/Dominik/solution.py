def load_input_to_dict(path):
    with open(path, "r") as f:
        content = f.readline()
    lst = [int(x) for x in content.split(",")]
    return lst


class opt_code_computer():

    def __init__(self):
        self.input_index = None
        self.setting_index = 0
        self.index = 0
        self.show = True
        self.exit_code = None
        self.opt_code = load_input_to_dict("input.txt")
        self.rel_base = 0
        self.function_dict = {
            1:  (self.__add, [0, 0, 0]),
            2:  (self.__multiply, [0, 0, 0]),
            3:  (self.__store_input, [0]),
            4:  (self.__output, [0]),
            5:  (self.__jump_if_true, [0, 0]),
            6:  (self.__jump_if_false, [0, 0]),
            7:  (self.__less_then, [0, 0, 0]),
            8:  (self.__equals, [0, 0, 0]),
            9:  (self.__base, [0]),
            99: (None, [])
            }

    def setup(self, parameter):
        self.setting = parameter
        self.output_value = None

    def __memory_expansion(self, parameter, lst):
        for param in parameter:
            if param >= len(lst):
                lst.extend((param - len(lst) + 1) * [0])

    @staticmethod
    def __opt_code_interpreter(opt_code: int, function_dict: dict):
        opt_code = str(opt_code)[::-1]
        operator = int(opt_code[:2][::-1])
        parameter_mode_out = function_dict[operator][1].copy()
        for i, n in enumerate(opt_code[2:]):
            parameter_mode_out[i] = int(n)
        return operator, parameter_mode_out, len(function_dict[operator][1]) + 1

    def __set_pointer(self, lst, i, mode, param):
        a, b, c = None, None, None

        if "a" in param:
            a = lst[i + 1]  # mode 1
            if mode[0] == 0:  # mode 0
                a = lst[a]  # get value at index position mode
            elif mode[0] == 2:
                self.__memory_expansion([self.rel_base + a], lst)
                a = lst[self.rel_base + a]

        if "b" in param:
            b = lst[i + 2]  # mode 1
            if mode[1] == 0:  # mode 0
                b = lst[b]  # get value at index

            elif mode[1] == 2:
                self.__memory_expansion([self.rel_base + b], lst)
                b = lst[self.rel_base + b]

        if "c" in param:
            c = lst[i + 3]
            if mode[2] == 2:
                self.__memory_expansion([self.rel_base + c], lst)
                c = self.rel_base + c

        return a, b, c

    def __add(self, lst, i, mode, move_by):
        a, b, c = self.__set_pointer(lst, i, mode, ["a", "b", "c"])
        self.__memory_expansion([c], lst)
        lst[c] = a + b
        return move_by

    def __multiply(self, lst, i, mode, move_by):
        a, b, c = self.__set_pointer(lst, i, mode, ["a", "b", "c"])
        self.__memory_expansion([c], lst)
        lst[c] = a * b
        return move_by

    def __store_input(self, lst, i, mode, move_by):
        if mode[0] == 0:
            lst[lst[i + 1]] = self.setting[self.setting_index]
        elif mode[0] == 1:
            lst[i + 1] = self.setting[self.setting_index]
        elif mode[0] == 2:
            self.__memory_expansion([self.rel_base + lst[i + 1]], lst)
            lst[self.rel_base + lst[i + 1]] = self.setting[self.setting_index]

        self.setting_index = 1
        if self.setting_index == 1:
            self.input_index = i
        return move_by

    def __output(self, lst, i, mode, move_by):
        if mode[0] == 0:
            self.output_value = lst[lst[i + 1]]
        elif mode[0] == 1:
            self.output_value = lst[i + 1]
        elif mode[0] == 2:
            self.__memory_expansion([self.rel_base + lst[i + 1]], lst)
            self.output_value = lst[self.rel_base + lst[i + 1]]
        if self.show:
            print(f"Code 4 at index {i}: Parameter Mode: {mode}; Output is {self.output_value}")
        return move_by

    def __jump_if_true(self, lst, i, mode, move_by):
        a, b, _ = self.__set_pointer(lst, i, mode, ["a", "b"])
        return b - i if a != 0 else move_by

    def __jump_if_false(self, lst, i, mode, move_by):
        a, b, _ = self.__set_pointer(lst, i, mode, ["a", "b"])
        return b - i if a == 0 else move_by

    def __less_then(self, lst, i, mode, move_by):
        a, b, c = self.__set_pointer(lst, i, mode, ["a", "b", "c"])
        lst[c] = 1 if a < b else 0
        return move_by

    def __equals(self, lst, i, mode, move_by):
        a, b, c = self.__set_pointer(lst, i, mode, ["a", "b", "c"])
        lst[c] = 1 if a == b else 0
        return move_by

    def __base(self, lst, i, mode, move_by):
        if mode[0] == 0:
            self.rel_base += lst[lst[i + 1]]
        elif mode[0] == 1:
            self.rel_base += lst[i + 1]
        elif mode[0] == 2:
            self.__memory_expansion([self.rel_base + lst[i + 1]], lst)
            self.rel_base += lst[self.rel_base + lst[i + 1]]
        return move_by

    def run_interpreter(self, **kwargs):
        code = kwargs.pop("code", self.opt_code)
        index = self.index

        if self.input_index != None:
            self.__store_input(lst=code, i=self.input_index, move_by=0)

        while code[index] != 99:
            op, param_mode, shift = self.__opt_code_interpreter(code[index], self.function_dict)
            index += self.function_dict[op][0](lst=code, i=index, mode=param_mode, move_by=shift)
            self.exit_code = 0

            if self.output_value != None:
                self.index = index
                self.exit_code = 4
                # break

        if code[index] == 99:
            self.exit_code = 99


def part_a():
    OPT_instance = opt_code_computer()
    OPT_instance.setup(parameter=[1])
    OPT_instance.run_interpreter()


def part_b():
    OPT_instance = opt_code_computer()
    OPT_instance.setup(parameter=[2])
    OPT_instance.run_interpreter()


# part_a()
# correct answer 3241900951

part_b()
# correct answer 83089
