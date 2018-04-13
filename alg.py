import sys
import json
import hashlib

tmp = ""
for line in sys.stdin:
	tmp += line

filename = "/home/arias/diploma/datasets/" + str(hashlib.md5(tmp.encode("utf-8")).hexdigest())
f = open(filename, 'w')
f.write(tmp)
f.close()
print(filename, end='')