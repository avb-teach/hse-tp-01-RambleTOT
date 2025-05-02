import os
import sys

i, o, m = sys.argv[1:]
m = int(m)

def create_dir(path):
    global o
    new_dir = ""
    for el in path.split('/'):
        new_dir += el + "/"
        os.system(
            "mkdir -p $1".replace(
                "$1", o + "/" + new_dir
            )
        )

def copy_file(input_path, output_path):
    os.system(
        "cp $1 $2".replace(
            "$1", input_path
        ).replace(
            "$2", output_path
        )
    )

for el in os.walk(i):
    el_null = el[0].replace(i, '')
    path = el_null.split('/')
    for j in range(len(path) + 1 - m, len(path)):
        create_dir("".join(path[j:]))
    for j in el[2]:
        copy_file(el[0] + "/" + j,
                  o + "/" + "/".join(path[len(path) + 1 - m:]))


