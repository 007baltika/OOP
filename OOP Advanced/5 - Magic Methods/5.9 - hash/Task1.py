

def limited_hash(left, right, hash_function = hash):
    
    
    def new_function(obj):
        if hash_function(obj) % right == hash_function(obj) % right: 
            return hash_function(obj) % left
    
    return new_function

hash_function = limited_hash(10, 15)
print(hash_function(10))
print(hash_function(11))
print(hash_function(15))