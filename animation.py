import os
import shutil
from imdb import IMDb
import time

def obter_genero_do_filme(file_path):
    ia = IMDb()
    filename, _ = os.path.splitext(os.path.basename(file_path))
    
    try:
        search_results = ia.search_movie(filename)
        if search_results:
            movie = ia.get_movie(search_results[0].movieID)
            genres = movie.get('genres', [])
            return 'Animation' in genres
    except Exception as e:
        print(f"Erro ao obter informações do filme {filename}: {e}")
    
    return False

def mover_para_pasta_animacao(file_path, pasta_destino):
    nome_arquivo, extensao = os.path.splitext(os.path.basename(file_path))
    destino = os.path.join(pasta_destino, f"{nome_arquivo}{extensao}")
    shutil.move(file_path, destino)
    print(f"Filme movido: {nome_arquivo} para {destino}")

def main():
    pasta_origem = "/data/media/FILMES"
    pasta_animacao = "/data/animacao"

    for filename in os.listdir(pasta_origem):
        if filename.endswith(('.mp4', '.avi', '.mkv')):  # Adicione outros formatos se necessário
            caminho_arquivo = os.path.join(pasta_origem, filename)
            
            try:
                if obter_genero_do_filme(caminho_arquivo):
                    mover_para_pasta_animacao(caminho_arquivo, pasta_animacao)
                else:
                    print(f"Filme não movido: {filename} - Gênero não é Animation")
            except Exception as e:
                print(f"Erro ao processar o filme {filename}: {e}")

            # Adiciona um pequeno atraso entre as requisições para evitar bloqueios
            time.sleep(1)

if __name__ == "__main__":
    main()
