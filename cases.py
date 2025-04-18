import re

def no_punctuation(s):
    return re.sub(r'[^\w\s]', ' ', s)

cases = {
    'upper': lambda s: s.upper(),
    'lower': lambda s: s.lower(),
}
