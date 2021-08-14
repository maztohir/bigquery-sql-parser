import hashlib


def hash_string(string):
    return hashlib.md5(string.encode("utf")).hexdigest()

def read_file(file_path, allow_error=False):
  try:
    with open(file_path, 'r') as myfile:
      return myfile.read()
  except Exception as e:
    if not allow_error:
      raise Exception(str(e))
    return None
