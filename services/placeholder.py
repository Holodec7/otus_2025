import requests


class PlaceholderApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.url = 'https://jsonplaceholder.typicode.com'

    def get_posts(self):
        url = f"{self.url}/posts"
        response = self.session.get(url)
        return response

    def get_posts_with_id(self, id_post):
        url = f"{self.url}/posts/{id_post}"
        response = self.session.get(url)
        return response

    def get_albums(self):
        response = self.session.get(url=f"{self.url}/albums")
        return response

    def get_album(self, album_id):
        url = f"{self.url}/albums/{album_id}"
        response = self.session.get(url=url)
        return response

    def create_album(self, album):
        url = f"{self.url}/albums"
        response = self.session.post(url=url, json=album)
        return response


