import sys

tmp = ""
for line in sys.stdin:
    tmp += line

print(tmp[:-1])
