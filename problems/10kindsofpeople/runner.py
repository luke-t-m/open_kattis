import subprocess
import time

colour_codes = {"red": "91", "green": "92", "yellow": "93", "cyan": "96"}

def print_colour(string, colour):
    print(f"\033[{colour_codes[colour]}m{string}\033[0m")

def file_contents(filename):
    file = open(filename, "r")
    contents = file.read()
    file.close()
    return contents


def run_on_file(run, sample):
    start_time = time.time()
    print(f"NOW RUNNING: {' '.join(run)} {sample}")
    program = subprocess.Popen(run, stdin = subprocess.PIPE, stdout=subprocess.PIPE, encoding = "utf-8")
    sample = file_contents(sample)
    for line in sample.split("\n"):
       print(f"sending input: {line}")
       program.stdin.write(line + "\n")
    print_colour("OUTPUT:", "red")
    out, err = program.communicate()
    for line in out.strip().split("\n"):
        print(line)
    print_colour("END.", "red")
    print(f"time: {time.time() - start_time}\n")



run_on_file(["python3", "10kindsofpeople.py"], "sample1")
run_on_file(["python3", "10kindsofpeople.py"], "sample2")

subprocess.run(["gcc", "10kindsofpeople.c"])
run_on_file(["./a.out"], "sample1")
run_on_file(["./a.out"], "sample2")