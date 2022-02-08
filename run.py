import os
import re


def inputs():
    while True:
        _ = input("输入文件夹名称：")
        if _ != "":
            return _


def file_list(file_path):
    dir_list = os.listdir(file_path)
    return sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x))) if dir_list else dir_list


files_name = inputs()
for file_name in file_list(files_name):
    with open(files_name + "/" + file_name, "r", encoding="utf-8", newline="") as f:
        content = ""
        for line in f.read().splitlines():
            line = line.replace("\u3000", "")
            if re.compile(r'\S').search(line) is not None:
                content += re.sub(r"^(\s*)", "\n　　", line)
        file = open("all.txt", "a", encoding="utf-8")
        file.write("\n\n\n\n" + file_name.replace(".txt", "\n") + content)
        file.close()
