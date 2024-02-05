# Lê as listas de filmes dos arquivos
with open('g2-movies.txt', 'r') as file1:
    lista1 = set(file1.read().splitlines())

with open('phantom-movies.txt', 'r') as file2:
    lista2 = set(file2.read().splitlines())

# Encontra os filmes duplicados
filmes_duplicados = lista1.intersection(lista2)

# Escreve os filmes duplicados em um arquivo de saída
with open('filmes_duplicados.txt', 'w') as output_file:
    for filme in filmes_duplicados:
        output_file.write("%s\n" % filme)

print("Filmes duplicados foram salvos em filmes_duplicados.txt")
