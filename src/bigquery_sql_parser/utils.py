import hashlib


def hash_string(string):
    return hashlib.md5(string.encode("utf")).hexdigest()
