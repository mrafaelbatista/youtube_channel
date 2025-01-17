with open('livros.txt', 'a', encoding='utf-8') as arquivo:
    """
    Este trecho de código abre o arquivo 'livros.txt' no modo de anexação ('a') com codificação UTF-8.
    Em seguida, escreve três títulos de livros no arquivo:
    1. 'Criando um segundo cérebro'
    2. 'Web scraping com Python'
    3. 'Inteligência Artificial'

    Se o arquivo 'livros.txt' não existir, ele será criado.
    Se o arquivo já existir, os títulos serão adicionados ao final do arquivo sem apagar o conteúdo existente.
    """
    arquivo.write('Criando um segundo cérebro\n')
    arquivo.write('Web scraping com Python\n')
    arquivo.write('Inteligência Artificial\n')