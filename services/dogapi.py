import requests


class DogsApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers = {"Content-Type": "application/json"}
        self.url = "https://dog.ceo/api"

    def get_all_breeds_list(self):
        url = f"{self.url}/breeds/list/all"
        response = self.session.get(url=url)
        return response

    def get_rand_images(self, count):
        url = f"{self.url}/breeds/image/random"
        if count > 1:
            url = f"{url}/{count}"
        response = self.session.get(url)
        return response

    def get_breed_images_list(self, breed):
        """Returns an array of all the images from a breed"""
        url = f"{self.url}/breed/{breed}/images"
        response = self.session.get(url)
        return response

    def get_rand_breed_image(self, breed, count):
        """Returns a random dog image from a breed, e.g. hound"""
        url = f"{self.url}/breed/{breed}/images/random"
        if count > 1:
            url = f"{self.url}/breed/{breed}/images/random/{count}"
        response = self.session.get(url)
        return response

    def get_sub_breads_list(self, breed):
        """Returns an array of all the sub-breeds from a breed"""
        url = f"{self.url}/breed/{breed}/list"
        response = self.session.get(url)
        return response

    def get_sub_breed_all_images(self, breed, sub):
        url = f"{self.url}/breed/{breed}/{sub}/images"
        response = self.session.get(url)
        return response

    def get_sub_bread_rand_images(self, breed, sub, count):
        url = f"{self.url}/breed/{breed}/{sub}/images/random"
        if count > 1:
            url = f"{url}/{count}"
        response = self.session.get(url)
        return response
