import tokenize

keywords = []
operators = []
identifiers = []
delimiters = []
literals = []

def fixKeywords():
    keywordsList = ['and', 'add', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else',
                    'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is',
                    'lambda', 'None', 'nonlocal', 'not', 'or', 'pass', 'print', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield']
    
    for word in keywords:
        if(word.string not in keywordsList):
            identifiers.append(word)

    for word in identifiers:
        if(word in keywords):
            keywords.remove(word)

def fixOperators():
    delimitersList = ['(', ')', '{', '}', '[', ']', ',', ';', ':']

    for op in operators:
        if(op.string in delimitersList):
            delimiters.append(op)

    for item in delimiters:
        if(item in operators):
            operators.remove(item)


def main():

    tokenList = []
    with open('text.txt', 'rb') as f:
        tokens = tokenize.tokenize(f.readline)
        for token in tokens:
            tokenList.append(token)
    
    # Moves tokens to individual arrays (Some tokens are not recognized correctly)
    for t in tokenList:
        match t.type:
            case 1: keywords.append(t)
            case 54: operators.append(t)
            case 2: literals.append(t)
            case 3: literals.append(t)

    fixOperators()
    fixKeywords()

    for x in identifiers:
        print(x)

main()
