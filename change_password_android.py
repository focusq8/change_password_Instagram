import requests
from  uuid import uuid4
import os

Done=1    
Error=1

def login_one():
    global authorization , current_password , Done , Error ,username
    os.system('cls||clear')

    username = input("Enter your username: ")
    current_password = input("\nEnter your current password: ")
    
    url_login = 'https://i.instagram.com/api/v1/accounts/login/'

    header_login = {
        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        'Accept-Encoding': 'gzip, deflate'
        }
    data_login = {
        
        "phone_id":uuid4(),
        "enc_password":f"#PWD_INSTAGRAM:0:&:{current_password}",
        "username":username,
        "adid":uuid4(),
        "guid":uuid4(),
        "device_id":uuid4(),
        "google_tokens":"[]",
        "login_attempt_count":"0"
        }
    req_login = requests.post(url=url_login,headers=header_login,data=data_login)
    if 'logged_in_user' in req_login.text:
        print(f"\n{Done}. {username} Logged in")
        Done+=1

        authorization = req_login.headers.get('ig-set-authorization')
        change_password_one()

    elif "The password you entered is incorrect" in req_login.text:
        print(f"\n{Error}. {username} The password you entered is incorrect")
        Error+=1

    else:
        print(f'\n{Error}. {username} {req_login.text}')
        Error+=1

def login_list():
    global authorizations , new_password , Done , Error ,usernames , passwords
    os.system('cls||clear')

    file = input("[+] Enter Your File Name: ")
    counts_proxies = sum(1 for line in open(file))
    print(f"\n{counts_proxies} usernames are in your file\n\n")
    if os.stat(file).st_size == 0:
        print("file is empty")
        login_list()

    new_password = len(input("\n[+] Enter The New Password: "))
    if new_password <=6:
        print("new password is less than 6 password")
        login_list()
    open_file = open(file,"r").read().splitlines()

    for list in open_file:
        usernames = list.split(":")[0]
        passwords = list.split(":")[1]

        url_login = 'https://i.instagram.com/api/v1/accounts/login/'

        header_login = {
            'X-Ig-Www-Claim': '0',
            'X-Ig-Connection-Type': 'WIFI',
            'X-Ig-Capabilities': '3brTv10=',
            'X-Ig-App-Id': '567067343352427',
            'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
            'Accept-Language': 'en-US',
            'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Content-Length': '674',
            'Accept-Encoding': 'gzip, deflate'
            }
        data_login = {
            
            "phone_id":uuid4(),
            "enc_password":f"#PWD_INSTAGRAM:0:&:{passwords}",
            "username":usernames,
            "adid":uuid4(),
            "guid":uuid4(),
            "device_id":uuid4(),
            "google_tokens":"[]",
            "login_attempt_count":"0"
            }
        req_login = requests.post(url=url_login,headers=header_login,data=data_login)
        if 'logged_in_user' in req_login.text:
            print(f"\n{Done}. {usernames} Logged in")
            Done+=1

            authorizations = req_login.headers.get('ig-set-authorization')
            change_password_list()
        elif "The password you entered is incorrect" in req_login.text:
            print(f"\n{Error}. {usernames} The password you entered is incorrect")
            Error+=1

        else:
            print(f'\n{Error}. {usernames} {req_login.text}')
            Error+=1

def change_password_one():
    global Done , Error
    os.system('cls||clear')

    password_one = input("\n\nEnter your new password: ")
    url_change_password='https://i.instagram.com/api/v1/accounts/change_password/'
    header_change_password = {

        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        "Authorization":authorization,
        'Accept-Encoding': 'gzip, deflate'
        }

    data_change_password = {
        "_uid":uuid4(),
        "_uuid":uuid4(),
        "enc_old_password":f"#PWD_INSTAGRAM:0:&:{current_password}",
        "enc_new_password1":f"#PWD_INSTAGRAM:0:&:{password_one}",
        "enc_new_password2":f"#PWD_INSTAGRAM:0:&:{password_one}"
        }
    req_change_password = requests.post(url=url_change_password,headers=header_change_password,data=data_change_password)
    if '"status":"ok"' in req_change_password.text:
        with open("Accounts Changed.txt","a") as file:
            file.write(f"{username}:{new_password}\n")
            file.close
        print(f"{Done}. {username} Has Changed Password")
        Done+=1
    
    elif "Create a new password you haven't used before." in req_change_password.text:
        print("Create a new password you haven't used before.")
        Error+=1

    else:
        print(f'\n{Error}. {username} {req_change_password.text}')
        Error+=1

def change_password_list():
    global Done , Error
    os.system('cls||clear')

    passwords = input("\n\nEnter your new password: ")
    url_change_password='https://i.instagram.com/api/v1/accounts/change_password/'
    header_change_password = {

        'X-Ig-Www-Claim': '0',
        'X-Ig-Connection-Type': 'WIFI',
        'X-Ig-Capabilities': '3brTv10=',
        'X-Ig-App-Id': '567067343352427',
        'User-Agent': 'Instagram 219.0.0.12.117 Android (25/7.1.2; 240dpi; 1280x720; samsung; SM-G977N; beyond1q; qcom; en_US; 346138365)',
        'Accept-Language': 'en-US',
        'X-Mid': 'YjKpKwABAAEBChfhQ0jDY79zjPt4',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Content-Length': '674',
        "Authorization":authorizations,
        'Accept-Encoding': 'gzip, deflate'
        }

    data_change_password = {
        "_uid":uuid4(),
        "_uuid":uuid4(),
        "enc_old_password":f"#PWD_INSTAGRAM:0:&:{new_password}",
        "enc_new_password1":f"#PWD_INSTAGRAM:0:&:{passwords}",
        "enc_new_password2":f"#PWD_INSTAGRAM:0:&:{passwords}"
        }
    req_change_password = requests.post(url=url_change_password,headers=header_change_password,data=data_change_password)
    if '"status":"ok"' in req_change_password.text:
        with open("Accounts Changed.txt","a") as file:
            file.write(f"{usernames}:{passwords}\n")
            file.close
        print(f"{Done}. {usernames} Has Changed Password")
        Done+=1
    
    elif "Create a new password you haven't used before." in req_change_password.text:
        print(f"{usernames} Create a new password you haven't used before.")
        Error+=1

    else:
        print(f'\n{Error}. {usernames} {req_change_password.text}')
        Error+=1
if __name__ == '__main__':
    choose = input("""

1. Change paswword one username 

2. Change paswword list usernames



Please choose one of them: """)
    if choose == "1":
        login_one()
    elif choose == "2":
        login_list()
    else:
        os.system('cls||clear')
        choose <="3"
        input("Choose 1 or 2 Please")