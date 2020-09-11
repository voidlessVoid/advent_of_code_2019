from itertools import permutations


def load_input_to_dict(path):
    with open(path, "r") as f:
        content = f.readline()
    lst = [int(x) for x in content.split(",")]
    return lst


class opt_code_computer():

    def __init__(self):
        self.input_index= None
        self.setting_index = 0
        self.index = 0
        self.show = True
        self.exit_code = None
        self.opt_code = load_input_to_dict("input.txt")
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

    def setup(self, parameter):
        self.setting = parameter
        self.output_value = None

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
        if self.setting_index== 1:
            self.input_index= i
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
        code = kwargs.pop("code", self.opt_code)
        index = self.index

        if self.input_index != None:
            self.__store_input(lst= code, i=self.input_index, move_by=0)

        while code[index] != 99:
            op, param_mode, shift = self.__opt_code_interpreter(code[index], self.function_dict)
            index += self.function_dict[op][0](lst=code, i=index, mode=param_mode, move_by=shift)
            self.exit_code = 0

            if self.output_value != None:
                self.index = index
                self.exit_code = 4
                break

        if code[index] == 99:
            self.exit_code = 99




def part_a():
    lst = []
    for n in permutations(range(5), 5):
        output = 0
        for i in n:
            value = []
            OPT_instance = opt_code_computer()
            OPT_instance.setup(parameter=[i, output])
            OPT_instance.show = False
            OPT_instance.run_interpreter()
            output = OPT_instance.output_value
            value.append(OPT_instance.output_value)
        lst.append(max(value))
    print(max(lst))


def part_b():
    lst = []
    for n in permutations(range(5, 10)[::-1], 5):
        print(f"Phase configuration {n}")
        amp_a = opt_code_computer()
        amp_b = opt_code_computer()
        amp_c = opt_code_computer()
        amp_d = opt_code_computer()
        amp_e = opt_code_computer()

        input_signal = 0
        counter=0

        while amp_e.exit_code != 99:
            amp_a.setup(parameter=[n[0], input_signal])
            amp_a.show = False
            amp_a.run_interpreter()

            amp_b.setup(parameter=[n[1], amp_a.output_value])
            amp_b.show = False
            amp_b.run_interpreter()

            amp_c.setup(parameter=[n[2], amp_b.output_value])
            amp_c.show = False
            amp_c.run_interpreter()

            amp_d.setup(parameter=[n[3], amp_c.output_value])
            amp_d.show = False
            amp_d.run_interpreter()

            amp_e.setup(parameter=[n[4], amp_d.output_value])
            amp_e.show = False
            amp_e.run_interpreter()

            # new input
            input_signal = amp_e.output_value
            counter+=1
            if not amp_e.output_value is None:
                lst.append(amp_e.output_value)

        print(f"Total number of iterations: {counter}, signal strength: {amp_e.output_value}")
    print(f"Max signal {max(lst)} at phase setting {n}")


#part_a()
# correct answer 101490

part_b()

# correct answer 61019896
