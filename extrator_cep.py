import re
endereco = 'Baltazar Nunes, 355, apartamento 51, Vila Carmosina, São Paulo, SP, 08290-220'


padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco)
if busca:
    cep = busca.group()
    print(cep)
