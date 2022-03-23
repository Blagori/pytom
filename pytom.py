import requests
import time


class downlaod():
    def img(img_url, name):
        r = requests.get(img_url)
        with open(f'{name}.jpg', 'wb') as f:
            f.write(r.content)

    def muisic(muisic_url, name):
        r = requests.get(muisic_url)
        with open(f'{name}.wav', 'wb') as f:
            f.write((r.content))


class time():
    def s(s):
        int(s)
        time.sleep(s)

    def h(h):
        int(h)
