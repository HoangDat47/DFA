code = '''
void main() {
    int sum = 0;
    for(int j = 0; j < 10; j = j + 1) {
        sum = sum + j + 10.43 + 34.E4 + 45.34E-4 + E43 + .34;
    }
}
'''

keywords = {'void', 'int', 'for'}
operators = {'=', '+', '<'}
separators = {'(', ')', '{', '}', ';'}

def tokenize(code):
    tokens = []
    current_token = ''
    i = 0
    while i < len(code):
        char = code[i]
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ''
        elif char in operators or char in separators:
            if current_token:
                tokens.append(current_token)
                current_token = ''
            tokens.append(char)
        else:
            current_token += char
        i += 1
    if current_token:
        tokens.append(current_token)
    return tokens

tokens = tokenize(code)
for token in tokens:
    if token in keywords:
        print(f"keyword : {token}")
    elif token in operators:
        print(f"{token} : {token}")
    elif token in separators:
        print(f"{token} : {token}")
    elif token.replace('.', '', 1).isdigit() or (token.replace('.', '', 1).replace('E', '', 1).replace('-', '', 1).isdigit() and 'E' in token):
        if '.' in token and 'E' in token:
            parts = token.split('E')
            if len(parts) == 2 and parts[0].replace('.', '', 1).isdigit() and parts[1].replace('-', '', 1).isdigit():
                print(f"num : {token}")
            else:
                print(f"Error: {token}")
        elif '.' in token and token.startswith('.'):
            if token[1:].isdigit():
                print(f"Error: .")
                print(f"num : {token[1:]}")
            else:
                print(f"Error: {token}")
        else:
            print(f"num : {token}")
    elif token.isidentifier():
        print(f"identifier : {token}")
    else:
        print(f"Error: {token}")