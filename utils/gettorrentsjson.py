import requests, config


def returnResult(query):
    result = requests.get(
        f'{config.apiUrl}{query}{config.apiParams}')
    return result.json()['results']
