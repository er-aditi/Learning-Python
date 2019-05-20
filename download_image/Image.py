import random
import urllib.request


def download_image(url):
    name = random.randrange(1, 10000)
    full_name = str(name) + ".jpeg"
    urllib.request.urlretrieve(url, full_name)


download_image("https://images.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg")
