import hashlib

def generate_controll_summ(string):
    hash_object = hashlib.sha256(string)
    hex_dig = hash_object.hexdigest()
    return hex_dig

