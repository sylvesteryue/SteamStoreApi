from bs4 import BeautifulSoup
import requests

URL = 'https://store.steampowered.com/'


def get_games(params):
    page = get_html(URL + 'search/' , params)

    soup = BeautifulSoup(page, 'html.parser')

    games = {}

    for a in soup.find_all(name="a", attrs={"class": "search_result_row"}):
        game_data = [format_entry(data) for data in a.find_all(name="div", attrs={"col"})]
        #print(game_data)
        id = a.get('data-ds-appid')
        games[id] = get_game(game_data)
        games[id]['id'] = id

    return games

def get_tags():
    page = get_html(URL + 'tag/browse', {})

    soup = BeautifulSoup(page, 'html.parser')

    tags = {}

    for tag_div in soup.find_all(name="div", attrs={'class': 'tag_browse_tag'}):
        id = tag_div.get('data-tagid')
        tags[id] = tag_div.text

    return tags

def get_genres():
    page = get_html(URL + 'tag/browse', {})

    soup = BeautifulSoup(page, 'html.parser')

    genres = {}
    genres['genres'] = []
    for genre_div in soup.find_all(name="div", attrs={'id': 'footer_genre_dropdown'}):
        for genre_a in genre_div.find_all(name="a"):
            genres['genres'].append(genre_a.text.strip())

    
    return genres


def get_game(game_data):
    title = game_data[1]
    release_date = game_data[2]
    price = game_data[4]

    game = {
        'title': title,
        'release_data': release_date,
        'price': price
    }

    return game

def format_entry(entry):
    if entry.find(attrs={"class": "search_price"}):
        temp = format_price(entry)
        #print(temp)
        return temp
    else:
        return entry.text.strip()


def format_price(div):
    if(div.find(name="strike")):
        og_price = div.find(name="strike").text.strip()
        current_price = ''.join(div.find(name="br").next_siblings).strip()
        return {"original": og_price, "discounted": current_price}
    else:
        return div.text.strip()



def get_html(url, params):
    with requests.get(url, params=params) as response:
        return response.text


if __name__ == '__main__':
    tags = get_tags()