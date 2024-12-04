import sys
sys.setrecursionlimit(15_000)
# input_stream = list(open("input.txt","r").read())
input_stream = list("mul(2,5)")
current, mults = [], []
build_number = lambda: int("".join(current.pop() for _ in range(len(current))))
check_ending = lambda ending: bool(input_stream[0] == ending) and bool(input_stream.pop(0))
find_number = lambda ending: (current.append(input_stream.pop(0)) and find_number(ending)) if input_stream[0].isdigit() else build_number() * int(check_ending(ending))
try_find_number = lambda ending: find_number(ending) or 0
find_in_brackets = lambda: (first := try_find_number(",")) and first and mults.append(first * try_find_number(")"))
find_mul = lambda: ([input_stream.pop(0) for _ in "mul("] and find_in_brackets()) if input_stream[:4] == list("mul(") else (input_stream.pop(0) and find_mul())
find_mul()
print(mults)
print(sum(mults))

input_stream = list("mul(2,5)")
input_stream = list(open("input.txt","r").read())
current, mults = [], []
def build_number():
    number = int("".join(current))
    current.clear()
    return number

def check_ending(ending):
    if input_stream[0] == ending:
        input_stream.pop(0)
        return True
    return False

def find_number(ending):
    if input_stream[0].isdigit():
        current.append(input_stream.pop(0))
        return find_number(ending)
    return build_number() * int(check_ending(ending))

def try_find_number(ending):
    return find_number(ending) or 0

def find_in_brackets():
    first = try_find_number(",")
    if first:
        mults.append(first * try_find_number(")"))

def find_mul():
    if input_stream[:4] == list("mul("):
        [input_stream.pop(0) for _ in "mul("]
        return find_in_brackets()
    input_stream.pop(0)
    return find_mul()

find_mul()
print(mults)
print(sum(mults))
