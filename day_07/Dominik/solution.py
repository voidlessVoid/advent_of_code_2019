def load_input_to_dict(path):
    with open(path, "r") as f:
        content = f.readline()
    lst = [int(x) for x in content.split(",")]
    return lst


class opt_code_computer():

    def __init__(self, parameter):
        self.show = True
        self.setting_index = 0
        self.setting = parameter
        self.output_value = None
        self.opt_full_code = load_input_to_dict("input.txt")
        self.function_dict = {
            1:  (self.__add, [0, 0, 0]),
            2:  (self.__multiply, [0, 0, 0]),
            3:  (self.__store_input, [0]),
            4:  (self.__output, [0]),
            5:  (self.__jump_if_true, [0, 0]),
            6:  (self.__jump_if_false, [0, 0]),
            7:  (self.__less_then, [0, 0, 0]),
            8:  (self.__equals, [0, 0, 0]),
            99: (None, [])
            }

    @staticmethod
    def __opt_code_interpreter(opt_code: int, function_dict: dict):
        opt_code = str(opt_code)[::-1]
        operator = int(opt_code[:2][::-1])
        parameter_mode_out = function_dict[operator][1].copy()
        for i, n in enumerate(opt_code[2:]):
            parameter_mode_out[i] = int(n)
        return operator, parameter_mode_out, len(function_dict[operator][1]) + 1

    @staticmethod
    def __set_pointer(lst, i, mode):
        try:
            a = lst[i + 1]  # get value
            if not mode[0]:  # if mode 0
                a = lst[a]  # get value at index
        except IndexError:
            a = None

        try:
            b = lst[i + 2]  # get value
            if not mode[1]:  # if mode 0
                b = lst[b]  # get value at index
        except IndexError:
            b = None

        try:
            c = lst[i + 3]
        except IndexError:
            c = None

        return a, b, c

    def __add(self, lst, i, mode, move_by):
        a, b, c = self.__set_pointer(lst, i, mode)
        lst[c] = a + b
        return move_by

    def __multiply(self, lst, i, mode, move_by):
        a, b, c = self.__set_pointer(lst, i, mode)
        lst[c] = a * b
        return move_by

    def __store_input(self, lst, i, move_by, **kwargs):
        lst[lst[i + 1]] = self.setting[self.setting_index]
        self.setting_index = 1
        return move_by

    def __output(self, lst, i, mode, move_by):
        a, _, _ = self.__set_pointer(lst, i, mode)
        if self.show:
            print(f"Code 4 at index {i}: Parameter Mode: {mode}; Output is {a}")
        self.output_value = a
        return move_by

    def __jump_if_true(self, lst, i, mode, move_by):
        a, b, _ = self.__set_pointer(lst, i, mode)
        return b - i if a != 0 else move_by

    def __jump_if_false(self, lst, i, mode, move_by):
        a, b, _ = self.__set_pointer(lst, i, mode)
        return b - i if a == 0 else move_by

    def __less_then(self, lst, i, mode, move_by):
        a, b, c = self.__set_pointer(lst, i, mode)
        lst[c] = 1 if a < b else 0
        return move_by

    def __equals(self, lst, i, mode, move_by):
        a, b, c = self.__set_pointer(lst, i, mode)
        lst[c] = 1 if a == b else 0
        return move_by

    def run_interpreter(self, **kwargs):
        code = kwargs.pop("code", self.opt_full_code)
        index = 0
        while code[index] != 99:
            op, param_mode, shift = self.__opt_code_interpreter(code[index], self.function_dict)
            index += self.function_dict[op][0](lst=code, i=index, mode=param_mode, move_by=shift)


def part_a():
    from itertools import permutations

    lst = []
    for n in permutations(range(5), 5):
        output = 0
        for i in n:
            value = []
            OPT_instance = opt_code_computer(parameter=[i, output])
            OPT_instance.show = False
            OPT_instance.run_interpreter()
            output = OPT_instance.output_value
            value.append(OPT_instance.output_value)
        lst.append(max(value))
    print(max(lst))

#part_a()
# correct answer 101490

