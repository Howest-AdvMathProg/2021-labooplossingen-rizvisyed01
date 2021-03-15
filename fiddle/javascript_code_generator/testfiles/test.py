from generator.generator import *
from generator.fileHandler import *

filename = "hello"
funcname = "hello"

content = generate_function(funcname, generate_print_code("hello world"))
content += f"{funcname}()"

generate_file(filename, content)
execute_file(filename)
