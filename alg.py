import sys
import json
import hashlib

tmp = ""
for line in sys.stdin:
	tmp += line

f = open("/home/arias/diploma/datasets/" + str(hashlib.md5(tmp.encode("utf-8")).hexdigest()), 'w')
f.write(tmp)
f.close()
