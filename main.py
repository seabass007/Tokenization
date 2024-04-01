import io
import tokenize

keywords = []
operators = []
identifiers = []
delimiters = []
literals = []


def fix_keywords():
    keywords_list = ['and', 'add', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
                     'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
                     'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'print', 'raise', 'return', 'True', 'try',
                     'while', 'with', 'yield']

    for word in keywords:
        if word.string not in keywords_list:
            identifiers.append(word)

    for word in identifiers:
        if word in keywords:
            keywords.remove(word)


def fix_operators():
    delimiters_list = ['(', ')', '{', '}', '[', ']', ',', ';', ':']

    for op in operators:
        if op.string in delimiters_list:
            delimiters.append(op)

    for item in delimiters:
        if item in operators:
            operators.remove(item)


def main():
    token_list = []

    try:
        with open('text.txt', 'r') as file:
            text = file.read()
            tokens = tokenize.tokenize(io.BytesIO(text.encode('utf-8')).readline)
            for token in tokens:
                token_list.append(token)
    except FileNotFoundError:
        print('File not found.')

    # Moves tokens to individual arrays (Some tokens are not recognized correctly)
    keywordsv = 0
    operatorsv = 0
    literalsv = 0
    for t in token_list:
        match t.type:
            case 1:
                keywords.append(t)
                keywordsv += 1
            case 54:
                operators.append(t)
                operatorsv += 1
            case 2:
                literals.append(t)
                literalsv += 1
            case 3:
                literals.append(t)

    fix_operators()
    fix_keywords()

    print(identifiers)
    print(f"Keyword = {keywordsv}, Operators = {operatorsv}, Literals = {literalsv}")


main()
