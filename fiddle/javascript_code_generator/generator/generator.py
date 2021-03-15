# start with simple code
# abstract it more and more each time

def generate_function(name, args, code):
    arg = "("
    for i in args:
        arg += i
    arg += ")"
    return f"const {name} = {arg}  => {code}\n"


def log_var(varname):
    return f"console.log({varname})\n"


def generate_print_code(msg):
    return f"console.log('{msg}')"


def execute_function(fn, container=None):
    code = f"const {container} = " if container is not None else ""
    code += f"{fn}() "
    return code + "\n"


def generate_vars(kv_dict, is_const=True):
    keyword = "const" if is_const else "let"
    list = ""
    for varname in kv_dict:
        # booleans???
        list += f"{keyword} {varname} = {kv_dict[varname]}\n"

    return list


def generate_op(vars, opperation):
    code = ""
    for i in range(len(vars)):
        code += f"{vars[i]} "
        if i < len(vars) - 1:
            code += opperation
    return code


def generate_array(name, content, is_constant=True):
    code = f"const {name} =" if is_constant else f"let {name} ="
    return code.join(content)
