class Grammar:
    def __init__(self):
        self.productions = {}
        self.start_symbol = None
    
    def add_production(self, non_terminal, production):
        if non_terminal not in self.productions:
            self.productions[non_terminal] = []
        self.productions[non_terminal].append(production)

    def set_start_symbol(self, start_symbol):
        self.start_symbol = start_symbol

    def __str__(self):
        result = []
        for non_terminal, productions in self.productions.items():
            result.append(f"{non_terminal} -> {' | '.join(productions)}")
        return '\n'.join(result)

def remove_unreachable_symbols(grammar):
    reachable = set()
    new_reachable = set([grammar.start_symbol])
    
    while new_reachable:
        reachable.update(new_reachable)
        next_reachable = set()
        for symbol in new_reachable:
            if symbol in grammar.productions:
                for production in grammar.productions[symbol]:
                    for char in production:
                        if char.isupper() and char not in reachable:
                            next_reachable.add(char)
        new_reachable = next_reachable
    
    grammar.productions = {k: v for k, v in grammar.productions.items() if k in reachable}
    return grammar

def remove_unproductive_symbols(grammar):
    productive = set()
    new_productive = set([k for k, v in grammar.productions.items() if any(c.islower() for c in ''.join(v))])
    
    while new_productive:
        productive.update(new_productive)
        next_productive = set()
        for symbol, productions in grammar.productions.items():
            if symbol not in productive:
                if any(all(char in productive or char.islower() for char in production) for production in productions):
                    next_productive.add(symbol)
        new_productive = next_productive
    
    grammar.productions = {k: v for k, v in grammar.productions.items() if k in productive}
    return grammar

def remove_empty_productions(grammar):
    nullable = set()
    for non_terminal, productions in grammar.productions.items():
        for production in productions:
            if production == '&':
                nullable.add(non_terminal)
    
    new_productions = {}
    for non_terminal, productions in grammar.productions.items():
        new_productions[non_terminal] = []
        for production in productions:
            if production != '&':
                new_productions[non_terminal].append(production)
                for nullable_symbol in nullable:
                    if nullable_symbol in production:
                        new_productions[non_terminal].append(production.replace(nullable_symbol, ''))
    
    grammar.productions = new_productions
    return grammar

def substitute_productions(grammar):
    for non_terminal in grammar.productions:
        new_productions = []
        for production in grammar.productions[non_terminal]:
            if len(production) == 1 and production.isupper():
                new_productions.extend(grammar.productions[production])
            else:
                new_productions.append(production)
        grammar.productions[non_terminal] = new_productions
    return grammar

def read_grammar_from_file(file_path):
    grammar = Grammar()
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            non_terminal, productions = line.split(' -> ')
            productions = productions.split(' | ')
            for production in productions:
                grammar.add_production(non_terminal, production)
            if not grammar.start_symbol:
                grammar.set_start_symbol(non_terminal)
    return grammar

def write_grammar_to_file(grammar, file_path, header=None):
    with open(file_path, 'w') as file:
        if header:
            file.write(header + '\n')
        file.write(str(grammar))

# Exemplo de uso
grammar = read_grammar_from_file('entrada.txt')

print("Gramática original:")
print(grammar)

# Simplificação
grammar = remove_unreachable_symbols(grammar)
grammar = remove_unproductive_symbols(grammar)
grammar = remove_empty_productions(grammar)
grammar = substitute_productions(grammar)

print("\nGramática simplificada:")
print(grammar)

# Escrever a gramática simplificada no arquivo de saída
write_grammar_to_file(grammar, 'saida.txt', header="SIMPLIFICAÇÃO")
