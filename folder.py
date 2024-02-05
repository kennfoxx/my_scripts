import os

root_directory = '/data4/'

# Função para renomear as pastas
def rename_folders(path):
    for folder in os.listdir(path):
        folder_path = os.path.join(path, folder)

        # Verifica se é um diretório
        if os.path.isdir(folder_path):
            # Verifica se o nome da pasta começa com "Season " seguido por um número de 1 a 9
            if folder.startswith('Season ') and folder[7:].isdigit() and 1 <= int(folder[7:]) <= 9:
                # Formata o novo nome com zero à esquerda se necessário
                new_name = f'Season {int(folder[7:]):02d}'
                new_folder_path = os.path.join(path, new_name)

                # Verifica se a nova pasta já existe, se não, renomeia
                if not os.path.exists(new_folder_path):
                    os.rename(folder_path, new_folder_path)
                    print(f'Renomeado: {folder} para {new_name}')
                else:
                    print(f'Pasta já existe: {new_name}')
            else:
                # Se não atender aos critérios, continua recursivamente para subdiretórios
                rename_folders(folder_path)

# Chama a função com o diretório raiz
rename_folders(root_directory)
