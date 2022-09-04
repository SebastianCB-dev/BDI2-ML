
def read_json(path: str):
  return open(path, 'r', encoding='utf8').read()

def read_txt(path: str):
  return open(path, 'r', encoding='utf8').readlines()
