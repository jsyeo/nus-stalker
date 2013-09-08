import ldap
import json
import sys

USER = "nusstu\\"
PW = ""

def read_config():
    f = open("config.json", "r")
    data = f.read()
    config = json.loads(data)
    username = config.get('username', "")
    password = config.get('password', "")
    if username == "nusstu\\" or password == "":
        print("Please enter your NUSNET credentials in the config.json file")
        sys.exit(1)
    return (username, password)


def main():
    user, pw = read_config()
    return

if __name__ == "__main__":
    main()
