import re

def no_punctuation(s):
    return re.sub(r'[^\w\s]', ' ', s)

def folder_cases(s):
    reaplced_and = re.sub(r'[&]', 'and', s)
    remove_cases = re.sub(r'[^\w\s\(\)\-\&]', '', reaplced_and)
    return remove_cases.lower()


cases = {
    'upper': lambda s: s.upper(),
    'lower': lambda s: s.lower(),
    'folder': lambda s: folder_cases(s),
    'pun': lambda s: no_punctuation(s),
}
