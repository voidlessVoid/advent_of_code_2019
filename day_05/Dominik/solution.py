def load_input_to_dict(path):
    with open(path, "r") as f:
        content = f.readline()
    lst = [int(x) for x in content.split(",")]
    return lst


def opt_code_interpreter(opt_code: int, function_dict: dict):
    opt_code = str(opt_code)[::-1]
    operator = int(opt_code[:2][::-1])
    parameter_mode_out = function_dict[operator][1].copy()
    for i, n in enumerate(opt_code[2:]):
        parameter_mode_out[i] = int(n)
    return operator, parameter_mode_out, len(function_dict[operator][1]) + 1


def interpreter(code, input_id=0):
    index = 0

    def set_pointer(lst, i, mode):
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

    def add(lst, i, mode, move_by):
        a, b, c = set_pointer(lst, i, mode)
        lst[c] = a + b
        return move_by

    def mul(lst, i, mode, move_by):
        a, b, c = set_pointer(lst, i, mode)
        lst[c] = a * b
        return move_by

    def store_input(lst, i, move_by, **kwargs):
        lst[lst[i + 1]] = input_id
        return move_by

    def output(lst, i, mode, move_by):
        a, _, _ = set_pointer(lst, i, mode)
        print(f"Code 4 at index {i}: Parameter Mode: {mode}; Output is {a}")
        return move_by

    def jump_if_true(lst, i, mode, move_by):
        a, b, _ = set_pointer(lst, i, mode)
        return b - i if a != 0 else move_by

    def jump_if_false(lst, i, mode, move_by):
        a, b, _ = set_pointer(lst, i, mode)
        return b - i if a == 0 else move_by

    def less_then(lst, i, mode, move_by):
        a, b, c = set_pointer(lst, i, mode)
        lst[c] = 1 if a < b else 0
        return move_by

    def equals(lst, i, mode, move_by):
        a, b, c = set_pointer(lst, i, mode)
        lst[c] = 1 if a == b else 0
        return move_by

    function_dict = {
        1:  (add, [0, 0, 0]),
        2:  (mul, [0, 0, 0]),
        3:  (store_input, [0]),
        4:  (output, [0]),
        5:  (jump_if_true, [0, 0]),
        6:  (jump_if_false, [0, 0]),
        7:  (less_then, [0, 0, 0]),
        8:  (equals, [0, 0, 0]),
        99: (None, [])
        }

    while code[index] != 99:
        op, param_mode, shift = opt_code_interpreter(code[index], function_dict)
        index += function_dict[op][0](lst=code, i=index, mode=param_mode, move_by=shift)


opt_full_code = load_input_to_dict("input.txt")
### part a ###
#interpreter(opt_full_code, input_id=1)
# correct answer: 9219874
### part b ###
interpreter(opt_full_code, input_id=5)
# correct answer: 5893654
