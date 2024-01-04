import codecs
import re

# Substitua o nome ou local do arquivo sempre que for fazer outro/ Forma de colocar o caminho em PYTHON ('caminho/do/seu/arquivo.txt') 
original_path = 'inve0319.txt'
corrigido_path = 'Arquivo_Modificado_inve0319.txt'

# Processa e lê o arquivo com possível codificação incorreta
with codecs.open(original_path, 'r', 'iso-8859-1') as file:
    text = file.read()

# Alterações específicas para corrigir a codificação do arquivo INTEIRO txt (ADICIONE MAIS CASO ACHE EM ALGUM OUTRO CODIGO ERRADO NOS AQUIVO DE INVENTARIO)
substituicoes = {
    "\'e1": "á",
    "\'e2": "â",
    "\'e3": "ã",
    "\'e7": "ç",
    "\'e9": "é",
    "\'e": "í",
    "\'f3": "ó",
    "\'f4": "ô",
}

# Realiza as substituições no texto
for original, corrigido in substituicoes.items():
    text = text.replace(original, corrigido)

# Remove as linhas que começam com '\par' e não contêm um espaço e um número após (remove tudo que não tem \par e o NCM ao lado)
text = re.sub(r'\\par (?![0-9]).*\n', '', text)

# Remove todos os caracteres de barra invertida
text = text.replace('\\', '')

# Escreve o texto corrigido no novo arquivo
with codecs.open(corrigido_path, 'w', 'utf-8') as file:
    file.write(text)

print(f"Arquivo corrigido salvo como: {corrigido_path}")
