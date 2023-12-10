url = "bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real"


#Sanitização da URL
url = url.strip()

#validacao de URL


#Separa base e parâmetros

url_parametros = url[indice_interrogacao+1:]
print(url_parametros)

# Busca valor de um parametro

print(valor)