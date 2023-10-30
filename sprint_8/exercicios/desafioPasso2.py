"""
Complementando com mais dados utilizando a api do TMDB

"""

# Movies

import requests
import boto3
import json

# detalhes do filme com base no id do filme
def get_movie_details(movie_id, api_key):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        movie_data = response.json()
        return movie_data
    else:
        return None

# detalhes do elenco do filme com base no id do filme
def get_cast_details(movie_id, api_key):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        cast_data = response.json()
        return cast_data
    else:
        return None

# informações dos filmes dos gêneros "War" e "Crime"
def get_movies_info_by_genre(api_key, genre_ids):

    # correspondência entre ids e nomes dos gêneros
    genre_names = {10752: 'War', 80: 'Crime'}

    base_url ='https://api.themoviedb.org/3/discover/movie'
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

                    # detalhes do filme
                    movie_details = get_movie_details(movie_id, api_key)
                    if movie_details is None:
                        continue

                    # detalhes do elenco
                    cast_details = get_cast_details(movie_id, api_key)
                    if cast_details is None:
                        continue

                    # informações
                    movie_info = {
                        'id': movie_details.get('id'),
                        'titulo': movie_details.get('title'),
                        'anoLancamento': movie_details.get('release_date'),
                        'tempoMinutos': movie_details.get('runtime'),
                        'genero': genre_names.get(genre_id),  # substituição do id pelo nome do genero
                        'notaMedia': movie_details.get('vote_average'),
                        'numeroVotos': movie_details.get('vote_count')
                    }

                    # informações do artista principal
                    if cast_details.get('cast'):
                        main_actor = next((actor for actor in cast_details.get('cast') if actor.get('order') == 0), None)
                        if main_actor:
                            movie_info['nomeArtista'] = main_actor.get('name')

                    all_movies_info.append(movie_info)

    return all_movies_info

# chave de api do tmdb
api_key = ''

# ids de gênero: 10752 eh o id de gênero para 'War' e 80 para 'Crime'
genre_ids = [10752, 80]

movies_info = get_movies_info_by_genre(api_key, genre_ids)

lista = [movies_info[i:i+100] for i in range(0, len(movies_info), 100)]

s3_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

# enviando os dados para o bucket
for i, conteudo in enumerate(lista):
    s3_path = f'Raw/TMDB/JSON/Movies/2023/10/27/arquivo_{i}.json'
    s3_client.put_object(Body=json.dumps(conteudo), Bucket='dados-desafio', Key=s3_path)
    print(f'Arquivo {i} enviado para o S3: {s3_path}')

# Series

import requests
import boto3
import json

def get_tv_details(tv_id, api_key):
    url = f'https://api.themoviedb.org/3/tv/{tv_id}?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        tv_data = response.json()
        return tv_data
    else:
        return None

def get_tv_cast_details(tv_id, api_key):
    url = f'https://api.themoviedb.org/3/tv/{tv_id}/credits?api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        cast_data = response.json()
        return cast_data
    else:
        return None

def get_tv_series_info_by_genre(api_key, genre_ids):

    genre_names = {10765: 'War', 80: 'Crime'}

    base_url = 'https://api.themoviedb.org/3/discover/tv'
    all_tv_series_info = []

    for genre_id in genre_ids:
        for page in range(1, 51):
            params = {
                'api_key': api_key,
                'with_genres': genre_id,
                'page': page 
            }

            response = requests.get(base_url, params=params)

            if response.status_code == 200:
                tv_series = response.json().get('results', [])
                for tv in tv_series:
                    tv_id = tv.get('id')

                    tv_details = get_tv_details(tv_id, api_key)
                    if tv_details is None:
                        continue

                    cast_details = get_tv_cast_details(tv_id, api_key)
                    if cast_details is None:
                        continue

                    tv_info = {
                        'id': tv_details.get('id'),
                        'titulo': tv_details.get('name'),
                        'anoLancamento': tv_details.get('first_air_date'),
                        'tempoMinutos': tv_details.get('runtime'),
                        'genero': genre_names.get(genre_id),
                        'notaMedia': tv_details.get('vote_average'),
                        'numeroVotos': tv_details.get('vote_count')
                    }

                    if cast_details.get('cast'):
                        main_actor = next((actor for actor in cast_details.get('cast') if actor.get('order') == 0), None)
                        if main_actor:
                            tv_info['nomeArtista'] = main_actor.get('name')

                    all_tv_series_info.append(tv_info)

    return all_tv_series_info

api_key = ''

genre_ids = [10765, 80]

tv_series_info = get_tv_series_info_by_genre(api_key, genre_ids)

lista = [tv_series_info[i:i+100] for i in range(0, len(tv_series_info), 100)]

s3_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

for i, conteudo in enumerate(lista):
    s3_path = f'Raw/TMDB/JSON/Series/2023/10/27/arquivo_{i}.json'
    s3_client.put_object(Body=json.dumps(conteudo), Bucket='dados-desafio', Key=s3_path)
    print(f'Arquivo {i} de séries de TV enviado para o S3: {s3_path}')
