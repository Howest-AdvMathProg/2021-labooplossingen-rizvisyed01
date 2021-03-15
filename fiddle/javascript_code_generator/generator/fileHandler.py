import os

def generate_file(fn, content):
    f = open(f"{fn}.js", "w")
    f.write(content)
    f.close()


def append_file(fn, content):
    f = open(f"{fn}.js", "a")
    f.write(content)
    f.close()


def execute_file(fn):
    print("executing command:")
    print("------------------")
    os.system(f"node {fn}")
    print("------------------")
    print("Command done!")
