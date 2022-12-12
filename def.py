def add(x: int, y: int) -> int:
    return x + y


def sub(x: int, y: int) -> int:
    return x - y


def mul(x: int, y: int) -> int:
    return x*y


def div(x: int, y: int) -> int:
    return x//y


print("Operands should be ints")
print("Operators can be +,-,* or /")
s = input("Please enter: operand Operator Operand")
s = s.split()
assert len(s) == 3
