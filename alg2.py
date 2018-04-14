import json

data = input()
data = json.loads(data)
data['task1'] = 'update'
print(json.dumps(data), end='')