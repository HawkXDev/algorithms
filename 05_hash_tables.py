# example of hash tables number 1

voted = {}


def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


# example of hash tables number 2

cache = {}


def get_data_from_server(url):
    return [f'cached data from {url}']


def get_page(url):
    if cache.get(url):
        return cache[url]  # cached data is returned
    else:
        data = get_data_from_server(url)
        cache[url] = data  # the data is stored in the cache
        return data
