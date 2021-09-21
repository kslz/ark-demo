import json

datas = [
    {
        'time': '123456',
        'name': 'lizi'
    },
    {
        'device': 'mac'
    }
]

jsonStr = json.dumps(datas,ensure_ascii=False)
print(jsonStr)
obj = json.loads(jsonStr)
print(type(obj))
print(obj)