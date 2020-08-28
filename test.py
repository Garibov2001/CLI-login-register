s = input()
i = 0
try:
    while (True):
        i += 1
        s = input()
except EOFError:
    print(i)
    