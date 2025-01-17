# Abre o arquivo 'livros_novos.txt' no modo de escrita ('w') com codificação 'utf-8'
with open('livros_novos.txt', 'w', encoding='utf-8') as arquivo:
    # Escreve a string 'Criando um segundo cérebro' seguida de uma nova linha no arquivo
    arquivo.write('Criando um segundo cérebro\n')
    # Escreve a string 'Web scraping com Python' seguida de uma nova linha no arquivo
    arquivo.write('Web scraping com Python\n')
    # Escreve a string 'Inteligência Artificial' seguida de uma nova linha no arquivo
    arquivo.write('Inteligência Artificial\n')