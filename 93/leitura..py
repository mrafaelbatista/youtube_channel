# Abre o arquivo 'livros.txt' no modo de leitura ('r') com codificação 'utf-8'
with open('livros.txt', 'r', encoding='utf-8') as arquivo:
    # Lê todo o conteúdo do arquivo e armazena na variável 'conteudo'
    conteudo = arquivo.read()
    # Imprime o conteúdo do arquivo no console
    print(conteudo)


# Abre o arquivo 'livros.txt' no modo de leitura ('r') com codificação 'utf-8'
with open('livros.txt', 'r', encoding='utf-8') as arquivo:
    # Itera sobre cada linha do arquivo
    for linha in arquivo:
        # Imprime a linha removendo o caractere de nova linha no final
        print(linha.rstrip())


# Abre o arquivo 'livros.txt' no modo de leitura ('r') com codificação 'utf-8'
with open('livros.txt', 'r', encoding='utf-8') as arquivo:
    # Lê todas as linhas do arquivo e armazena na lista 'linhas'
    linhas = arquivo.readlines()

# Itera sobre cada linha armazenada na lista 'linhas'
for l in linhas:
    # Imprime a linha removendo o caractere de nova linha no final
    print(l.rstrip())