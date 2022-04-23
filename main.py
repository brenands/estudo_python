url = "bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real"

#separa a base e os parametros
local_interrogacao = url.find('?')
url_base = url[:local_interrogacao]

#busca o valor de um parametro
url_parametros = url[local_interrogacao+1:]
print(url_parametros)
parametro_busca = 'moedaOrigem'
indice_parametro = url_parametros.find(parametro_busca)
print(indice_parametro)
valor_indice = indice_parametro + len(parametro_busca) + 1
valor = url_parametros[valor_indice:]

print(valor)