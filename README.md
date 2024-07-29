# Simplificação e Normalização de Gramáticas Livres de Contexto

Este repositório contém um programa em Python para simplificação e normalização de gramáticas livres de contexto. Ele lê uma gramática a partir de um arquivo de entrada, aplica simplificações e normalizações, e gera as gramáticas resultantes em arquivos de saída.

## Estrutura dos Arquivos

- `entrada.txt`: Contém a gramática original.
- `saida.txt`: Contém a gramática simplificada.
- `main.py`: Código Python para simplificação e normalização da gramática.
- `README.md`: Este documento.

## Conteúdo do Arquivo `entrada.txt`

O arquivo `entrada.txt` contém a gramática original com as produções conforme o formato:

```txt
S -> AB | Bc | aB | ε
A -> aA | B | ε
B -> b | ε
C -> cC | D
D -> d
```
o arquivo `saida.txt` contém a saída gerada pelo programa que no primeiro caso é:

```txt
SIMPLIFICAÇÃO
S -> aAa | aa | bBb | b
A -> a | aA | a
E -> b