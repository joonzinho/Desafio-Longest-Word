## Código para ser considerado válido é necessário ignorar qualquer tipo de pontuação/input não pode ser vazio

# Importação de bibliotecas necessárias
import re

# Função do LongestWord utilizando como parâmetro (sen)
def LongestWord(sen):
  count = 0
  # Retirar pontuação usando a bibioteca RE
  sen_tratada = re.sub(r'[^\w\s]','',sen)
  # Separa as palavras em "" que estão na frase - LISTA
  lista_de_palavras = sen_tratada.split()
  # Função para verificar qual a maior palavra da frase - LISTA
  for palavra in lista_de_palavras:
      if len(palavra) > count:
          count = len(palavra)
          palavra_maior = palavra
    # Retorna a maior palavra da frase
  return palavra_maior

# Deixar a função de chamada abaixo
print(LongestWord(input()))

#CÓDIGO FEITO PELO JOÃO VICTOR DA SILVA PINTO SANTOS
