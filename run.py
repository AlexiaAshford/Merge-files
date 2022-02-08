import os
import re


def inputs() -> str:
    while True:
        info = input("输入文件夹名称：")
        if info != "" and info is not None:
            return info
        else:
            print("请输入文件夹名！")


def file_list(file_path: str) -> list:
    dir_list = os.listdir(file_path)
    return sorted(dir_list, key=lambda x: os.path.getmtime(os.path.join(file_path, x))) \
        if dir_list else []


def merge_file(files_name: str):
    file = open("out_file.txt", "a", encoding="utf-8")
    for file_name in file_list(files_name):
        with open(os.path.join(files_name, file_name), "r", encoding="utf-8", newline="") as f:
            content = ""
            for line in f.read().splitlines():
                line = line.replace("\u3000", "")
                if re.compile(r'\S').search(line) is not None:
                    content += re.sub(r"^(\s*)", "\n　　", line)
            file.write("\n\n\n\n" + file_name.replace(".txt", "\n") + content)
    file.close()


if __name__ == '__main__':
    merge_file(inputs())
