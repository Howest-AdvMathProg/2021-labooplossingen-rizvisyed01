
from generator.generator import *
from generator.fileHandler import *

fn = "hello"

vrs = {
    "msg": "'hello'",
    "num": 2,
    "num2": 3,
}

content = generate_vars(vrs) + generate_function("add", generate_op(["num", "num2"], "+")) + execute_function("add", "result") + log_var("result")

generate_file(fn, content)
execute_file(fn)

