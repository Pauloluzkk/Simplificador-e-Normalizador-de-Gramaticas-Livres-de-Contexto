# Simplificação e Normalização de Gramáticas Livres de Contexto

Este repositório contém um programa em Python para simplificação e normalização de gramáticas livres de contexto. Ele lê uma gramática a partir de um arquivo de entrada, aplica simplificações e normalizações, e gera as gramáticas resultantes em arquivos de saída.

## Estrutura dos Arquivos

- `entrada.txt`: Contém a gramática original.
- `saida_simplificada.txt`: Contém a gramática simplificada.
- `saida_chomsky.txt`: Contém a gramática na forma normal de Chomsky.
- `saida_greibach.txt`: Contém a gramática na forma normal de Greibach.
- `saida_left_factoring.txt`: Contém a gramática após fatoração à esquerda.
- `saida_no_left_recursion.txt`: Contém a gramática após remoção de recursão à esquerda.
- `simplificacao_gramatica.py`: Código Python para simplificação e normalização da gramática.
- `README.md`: Este documento.

## Conteúdo do Arquivo `entrada.txt`

O arquivo `entrada.txt` contém a gramática original com as produções conforme o formato:

```txt
S -> AB | Bc | aB | ε
A -> aA | B | ε
B -> b | ε
C -> cC | D
D -> d
