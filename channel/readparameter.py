# -*- coding:UTF-8 -*-
import sys
import re

para_list = list()


def readparameter(input_parameter):
    with open(input_parameter, "r") as f:
        for line in f.readlines():
            line = line.strip()
            para_list.append(line)
        print(para_list[0])
        print(para_list[1])
        print(para_list[2])
        print(para_list[3])
        print(para_list)

if __name__ == "__main__":
    readparameter(sys.argv[1])
