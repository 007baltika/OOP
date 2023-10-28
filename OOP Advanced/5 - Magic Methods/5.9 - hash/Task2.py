

def hash_function(obj):
    obj = str(obj)
    #reduce
    if len(obj) % 2 == 0: return ord(obj[0]) * (ord(obj[-i]) + ord(obj[i]) for i in range(1, len(obj) // 2))
    else: return ord(obj[0]) * (ord(obj[-i]) + ord(obj[i]) for i in range(1, len(obj) // 2)) + 