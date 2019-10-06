import requests

class game():
    def __init__(self, name, phone, price, postcode, long = ' ', lat = ' '):
        self.name = name
        self.phone = phone
        self.method = price
        self.postcode = postcode
        self.long = long
        self.lat = lat


    def long_lat(self):
        pc = self.postcode
        post_code = requests.get(f"http://api.postcodes.io/postcodes/{self.postcode}")
        post_code_dict = post_code.json()
        long1 = post_code_dict['result']['longitude']
        long2 = post_code_dict['result']['latitude']
        return long1, long2



