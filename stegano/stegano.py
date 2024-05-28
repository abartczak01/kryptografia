# Agata Bartczak 285755
import sys
from algorithms import *

result = ""
with open("cover.html", "r+") as file:
    for line in file:
        if not line.isspace():
            result += line

    file.seek(0)
    file.write(result)

if sys.argv[1] == "-d":
    if sys.argv[2] == "-1":
        d1()
    elif sys.argv[2] == "-2":
        d2()
    elif sys.argv[2] == "-3":
        d3()
    elif sys.argv[2] == "-4":
        d4()
elif sys.argv[1] == "-e":
    if sys.argv[2] == "-1":
        e1()
    elif sys.argv[2] == "-2":
        e2()
    elif sys.argv[2] == "-3":
        e3()
    elif sys.argv[2] == "-4":
        e4()
