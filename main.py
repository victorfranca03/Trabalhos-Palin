import codecs
import re
import os

# Substitua o nome ou local do arquivo sempre que for fazer outro/ Forma de colocar o caminho em PYTHON ('caminho/do/seu/arquivo.txt') 
original_path = 'inve0219.txt'
corrigido_path = 'Arquivo_Modificado_inve0219.txt'

# Verifica a existência do arquivo antes de tentar abri-lo
if os.path.exists(original_path):
    # Processa e lê o arquivo com possível codificação incorreta
    with codecs.open(original_path, 'r', 'iso-8859-1') as file:
        text = file.read()

    # Substituições específicas para corrigir a codificação do arquivo
    substituicoes = {
        "\'e1": "á",
        "\'e2": "â",
        "\'e3": "ã",
        "\'e7": "ç",
        "\'e9": "é",
        "\'e": "í",
        "\'f3": "ó",
        "\'f4": "ô",
        "Ã¡": "á",
        "Ã¢": "â",
        "Ã£": "ã",
        "Ã§": "ç",
        "Ã©": "é",
        "Ã­": "í",
        "Ã³": "ó",
        "Ã´": "ô",
        "Ãº": "ú",
        "Ã¼": "ü",
        "Ã‡": "Ç",
        "Ã‰": "É",
        "Ã“": "Ó",
        "Ã”": "Ô",
        "Ãš": "Ú",
        "Ãœ": "Ü",
    }

    # Realiza as substituições no texto
    
    for original, corrigido in substituicoes.items():
        text = text.replace(original, corrigido)

    # Remove as linhas que começam com \par e não têm um número a seguir
    
    text = re.sub(r'\\par (?![0-9]).*\n', '', text)

    # Remove as linhas que não começam com um número
    
    text = re.sub(r'^[^\d].*\n', '', text, flags=re.MULTILINE)

    # Remove todos os caracteres de barra invertida
    
    text = text.replace('\\', '')

    # Escreve o texto corrigido no novo arquivo
    
    with codecs.open(corrigido_path, 'w', 'utf-8') as file:
        file.write(text)

    print(f"Arquivo corrigido salvo como: {corrigido_path}")
else:
    print(f'O arquivo {original_path} não foi encontrado.')
