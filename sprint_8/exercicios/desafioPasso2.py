"""
Complementando com mais dados utilizando a api do TMDB

"""

# MOVIES

import requests
import boto3
import json

# Detalhes do filme com base no ID do filme
def get_movie_details(movie_id, api_key):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    else:
        return None

# Detalhes do elenco do filme com base no ID do filme
def get_cast_details(movie_id, api_key):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        cast_data = response.json()
        return cast_data
    else:
        return None

# Informações dos filmes dos gêneros "War" e "Crime"
def get_movies_info_by_genre(api_key, genre_ids):

    # Correspondência entre IDs e nomes dos gêneros
    genre_names = {10752: 'War', 80: 'Crime'}

    base_url = 'https://api.themoviedb.org/3/discover/movie'
    all_movies_info = []

    for genre_id in genre_ids:
        for page in range(1, 51):
            params = {
                'api_key': api_key,
                'with_genres': genre_id,
                'page': page
            }

            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                movies = response.json().get('results', [])
                for movie in movies:
                    movie_id = movie.get('id')

                    # Detalhes do filme
                    movie_details = get_movie_details(movie_id, api_key)
                    if movie_details is None:
                        continue

                    # Detalhes do elenco
                    cast_details = get_cast_details(movie_id, api_key)
                    if cast_details is None:
                        continue

                    # Informações
                    movie_info = {
                        'id': movie_details.get('id'),
                        'titulo': movie_details.get('title'),
                        'anoLancamento': movie_details.get('release_date')[:4],  # Apenas o ano de lançamento
                        'tempoMinutos': movie_details.get('runtime'),
                        'genero': genre_names.get(genre_id),  # Substituição do ID pelo nome do gênero
                        'notaMedia': movie_details.get('vote_average'),
                        'numeroVotos': movie_details.get('vote_count')
                    }

                    # Informações do elenco principal
                    if cast_details.get('cast'):

                        main_actor = next((actor for actor in cast_details.get('cast') if actor.get('order') == 0), None)
                        
                        if main_actor:
                            movie_info['generoArtista'] = 'actress' if main_actor.get('gender') == 1 else 'actor'
                            movie_info['personagem'] = main_actor.get('character')
                            movie_info['nomeArtista'] = main_actor.get('name')
                            movie_info['anoNascimento'] = main_actor.get('birthday')
                            movie_info['anoFalecimento'] = main_actor.get('deathday')
                            movie_info['profissao'] = main_actor.get('known_for_department')

                            # Busca por títulos mais conhecidos do artista
                            known_for = main_actor.get('known_for')
                            if known_for:
                                known_titles = []
                                for known in known_for:
                                    if known.get('title'):
                                        known_titles.append(known.get('title'))
                                    elif known.get('name'):
                                        known_titles.append(known.get('name'))
                                movie_info['titulosMaisConhecidos'] = known_titles

                    all_movies_info.append(movie_info)

    return all_movies_info

# Chave de API do TMDb
api_key = ''

# IDs de gênero: 10752 é o ID de gênero para 'War' e 80 para 'Crime'
genre_ids = [10752, 80]

movies_info = get_movies_info_by_genre(api_key, genre_ids)

# Dividir os dados em lotes de 100 filmes por arquivo
chunks = [movies_info[i:i+100] for i in range(0, len(movies_info), 100)]

# Conexão com o cliente do S3
s3_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

# Enviando os dados para o bucket
for i, chunk in enumerate(chunks):
    s3_path = f'Raw/TMDB/JSON/Movies/2023/10/27/arquivo_{i}.json'
    s3_client.put_object(Body=json.dumps(chunk), Bucket='', Key=s3_path)
    print(f'Arquivo {i} de filmes enviado para o S3: {s3_path}')


# SERIES

import requests
import boto3
import json

# Detalhes da série com base no ID da série
def get_serie_details(serie_id, api_key):
    url = f'https://api.themoviedb.org/3/tv/{serie_id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        serie_data = response.json()
        return serie_data
    else:
        return None

# Detalhes do elenco da série com base no ID da série
def get_cast_details(serie_id, api_key):
    url = f'https://api.themoviedb.org/3/tv/{serie_id}/credits?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        cast_data = response.json()
        return cast_data
    else:
        return None

# Informações das séries dos gêneros "War" e "Crime"
def get_series_info_by_genre(api_key, genre_ids):
    genre_names = {10768: 'War', 80: 'Crime'}  # Correspondência entre IDs e nomes dos gêneros

    base_url = 'https://api.themoviedb.org/3/discover/tv'
    all_series_info = []

    for genre_id in genre_ids:
        for page in range(1, 51):
            params = {
                'api_key': api_key,
                'with_genres': genre_id,
                'page': page
            }

            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                series = response.json().get('results', [])
                for serie in series:
                    serie_id = serie.get('id')

                    serie_details = get_serie_details(serie_id, api_key)
                    if serie_details is None:
                        continue

                    cast_details = get_cast_details(serie_id, api_key)
                    if cast_details is None:
                        continue

                    serie_info = {
                        'id': serie_details.get('id'),
                        'titulo': serie_details.get('name'),
                        'anoLancamento': serie_details.get('first_air_date')[:4],  # Apenas o ano de lançamento
                        'genero': genre_names.get(genre_id),  # Substituição do ID pelo nome do gênero
                        'notaMedia': serie_details.get('vote_average'),
                        'numeroVotos': serie_details.get('vote_count')
                    }

                    if cast_details.get('cast'):
                        main_actor = next((actor for actor in cast_details.get('cast') if actor.get('order') == 0), None)
                        
                        if main_actor:
                            serie_info['generoArtista'] = 'actress' if main_actor.get('gender') == 1 else 'actor'
                            serie_info['personagem'] = main_actor.get('character')
                            serie_info['nomeArtista'] = main_actor.get('name')
                            serie_info['anoNascimento'] = main_actor.get('birthday')
                            serie_info['anoFalecimento'] = main_actor.get('deathday')
                            serie_info['profissao'] = main_actor.get('known_for_department')
                            
                            known_for = main_actor.get('known_for')
                            if known_for:
                                known_titles = []
                                for known in known_for:
                                    if known.get('title'):
                                        known_titles.append(known.get('title'))
                                    elif known.get('name'):
                                        known_titles.append(known.get('name'))
                                serie_info['titulosMaisConhecidos'] = known_titles

                    all_series_info.append(serie_info)

    return all_series_info

api_key = ''  # Insira sua chave de API do TMDB

# IDs de gênero para séries
genre_ids = [10768, 80]  # ID dos gêneros: 10768 para 'War' e 80 para 'Crime'

series_info = get_series_info_by_genre(api_key, genre_ids)

# Dividir os dados em lotes de 100 séries por arquivo
chunks = [series_info[i:i+100] for i in range(0, len(series_info), 100)]

# Conexão com o cliente do S3
s3_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

# Enviando os dados para o bucket
for i, chunk in enumerate(chunks):
    s3_path = f'Raw/TMDB/JSON/Series/2023/10/27/arquivo_{i}.json'
    s3_client.put_object(Body=json.dumps(chunk), Bucket='', Key=s3_path)
    print(f'Arquivo {i} de séries enviado para o S3: {s3_path}')
