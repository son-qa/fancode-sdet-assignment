import requests


def get(url, params=None):
    try:
        response = requests.get(url=url, params=params)
        return response
    except Exception as e:
        raise e
