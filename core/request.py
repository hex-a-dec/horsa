import requests
import base64
from urllib.parse import urlparse
from colorama import Fore


class Request():
    def __init__(self, url, ua, key, hash):
        self.url = url
        self.ua = ua
        parsed_url = urlparse(self.url)
        self.hash = "auth_token="+hash+"; path=/; domain="+parsed_url.netloc+"; secure; HttpOnly"
        self.key = key

    @staticmethod
    def encode_base64(data):
        if isinstance(data, str):
            data = data.encode() # handle both text and binary data
        return base64.b64encode(data).decode()

    @staticmethod
    def decode_base64(data):
        if isinstance(data, str):
            data = data.encode() # handle both text and binary data
        return base64.b64decode(data).decode()

    def xor_encrypt(self, data, key):
        encrypted_data = ""
        for i in range(len(data)):
            encrypted_data += chr(ord(data[i]) ^ ord(key[i % len(key)]))
        return encrypted_data

    def send_POST(self, command):
        headers = {'User-Agent': self.ua, 'Content-Type': 'application/x-www-form-urlencoded', 'Cookie': self.hash}
        data = {'data': self.encode_base64(self.xor_encrypt(command, self.key))}
        response = requests.post(self.url, headers=headers, data=data)
        if response.status_code == 403:
            print(Fore.RED + "[!]" + Fore.WHITE + " Wrong password. Check your authentication key")
            print(Fore.BLUE + "[+]" + Fore.WHITE +" Exiting now!")
            exit(0)
        else:
            return self.xor_encrypt(self.decode_base64(response.text), self.key)

    def get_status(self):
        response = requests.get(self.url, headers={'User-Agent': self.ua})
        return response.status_code

    
