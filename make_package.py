import os

dirs = os.listdir('.')
last_day = max(int(x.split('_')[1]) for x in dirs if "day_" in x)
day = last_day + 1

print("Welcome to day %s..."%day)

test_module = """from unittest import TestCase, mock
import day{day}

class TestDay{day}(TestCase):

    pass
""".format(day=day)

unix_commands = [
    "mkdir day_%s"%day, "touch day_%s/__init__.py"%day, "touch day_{day}/day{day}.py".format(day=day)
]
for c in unix_commands:
    os.system(c)

f = open("day_%s/tests.py"%day, "w")
f.write(test_module)
f.close()
