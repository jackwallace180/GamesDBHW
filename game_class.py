import requests

class Game():
    def __init__(self, name, phone, price, postcode, long = ' ', lat = ' '):
        self.name = name
        self.phone = phone
        self.price = price
        self.postcode = postcode
        self.long = long
        self.lat = lat


    def long_find(self):
        pc = self.postcode
        post_code = requests.get(f"http://api.postcodes.io/postcodes/{self.postcode}")
        post_code_dict = post_code.json()
        long1 = post_code_dict['result']['longitude']
        return long1


    def lat_find(self):
        pc = self.postcode
        post_code = requests.get(f"http://api.postcodes.io/postcodes/{self.postcode}")
        post_code_dict = post_code.json()
        long1 = post_code_dict['result']['latitude']
        return long1





