import requests
import os

Done=1    
Error=1

def login_one():
    global username , current_password , get_session , get_csrftoken , Error , Done
    os.system('cls||clear')

    username = input("Enter your username: ")
    current_password = input("\nEnter your current password: ")

    url_login = 'https://www.instagram.com/accounts/login/ajax/'

    header_login = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,ar;q=0.8",
        "content-length": "320",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": "mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; ig_did=981DC62D-454E-4940-BA37-185B711E8296; ig_nrcb=1; csrftoken=iJaztfQIESi3hzeI0H2f2AMc56izmHst",
        "origin": "https://www.instagram.com",
        "referer": "https://www.instagram.com/",
        "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96',
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
        "x-asbd-id": "198387",
        "x-csrftoken": "iJaztfQIESi3hzeI0H2f2AMc56izmHst",
        "x-ig-app-id": "936619743392459",
        "x-instagram-ajax": "684510d5f3c6",
        "x-requested-with": "XMLHttpRequest"
        }

    data_login = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{current_password}',
        'queryParams': {},
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
        }

    req_login = requests.post(url_login,headers=header_login,data=data_login)

    if '"user":true,"authenticated":false' in req_login.text:
        print(f'\n{Error}. {username} Password Is Wrong !\nPlease Check On Your Password\n\n')
        Error+=1 

    elif '"checkpoint_url"' in req_login.text:
        input(f"{username} Is Secured !\nPlease Activate Your code To login\n\n")

    elif "checkpoint_challenge_required" in req_login.text:
        input(f"{username} has Two Factor authentication\nPlease Turn It Off And Try Again\n\n")

    elif '"authenticated":true' in req_login.text:
        print(f"\n{Done}. {username} logged in")
        Done+=1

        get_session = req_login.cookies['sessionid']
        get_csrftoken = req_login.cookies.get('csrftoken')
        change_password_one()
    
    else:
        print(f'\n{Error}. {username} {req_login.text}')
        Error+=1

def login_list():
    global usernames ,passwords, new_password , get_sessions , get_csrftokens , Error , Done
    os.system('cls||clear')

    print(f"\n\nYour File Must Be Like\nUsername:Password")

    file = input("\n\n[+] Enter Your File Name: ")
    counts_proxies = sum(1 for line in open(file))
    print(f"\n{counts_proxies} usernames are in your file\n\n")
    if os.stat(file).st_size == 0:
        print("file is empty")
        login_list()

    new_password = len(input("[+] Enter The New Password: "))
    if new_password <=6:
        print("new password is less than 6 password")
        login_list()
    open_file = open(file,"r").read().splitlines()

    for list in open_file:
        usernames = list.split(":")[0]
        passwords = list.split(":")[1]

        url_login = 'https://www.instagram.com/accounts/login/ajax/'

        header_login = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,ar;q=0.8",
            "content-length": "320",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "mid=Yo1OIAALAAHBL9tsvsYrM8DjDctR; ig_did=981DC62D-454E-4940-BA37-185B711E8296; ig_nrcb=1; csrftoken=iJaztfQIESi3hzeI0H2f2AMc56izmHst",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36",
            "x-asbd-id": "198387",
            "x-csrftoken": "iJaztfQIESi3hzeI0H2f2AMc56izmHst",
            "x-ig-app-id": "936619743392459",
            "x-instagram-ajax": "684510d5f3c6",
            "x-requested-with": "XMLHttpRequest"
            }

        data_login = {
            'username': usernames,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{passwords}',
            'queryParams': {},
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}'
            }

        req_login = requests.post(url_login,headers=header_login,data=data_login)

        if '"user":true,"authenticated":false' in req_login.text:
            print(f'\n{Error}. {usernames} Password Is Wrong !\nPlease Check On Your Password\n\n')
            Error+=1 

        elif '"checkpoint_url"' in req_login.text:
            input(f"{usernames} Is Secured !\nPlease Activate Your code To login\n\n")
    
        elif "checkpoint_challenge_required" in req_login.text:
            input(f"{usernames} has Two Factor authentication\nPlease Turn It Off And Try Again\n\n")
    
        elif '"authenticated":true' in req_login.text:
            print(f"\n{Done}. {usernames} logged in")
            Done+=1

            get_sessions = req_login.cookies['sessionid']
            get_csrftokens = req_login.cookies.get('csrftoken')
            change_password_list()
        
        else:
            print(f'\n{Error}. {usernames} {req_login.text}')
            Error+=1

def change_password_one():
    global Done , Error
    os.system('cls||clear')
    password_one = input("\n[+] Enter The New Password: ")
    if password_one <=6:
        print("new password is less than 6 password")
        change_password_one()

    url_change_password = 'https://www.instagram.com/accounts/password/change/'
    header_change_password = {

        'accept':'*/*',
        'accept-encoding':'gzip,deflate,br',
        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
        'content-length':'672',
        'content-type':'application/x-www-form-urlencoded',
        'cookie': f"csrftoken={get_csrftoken}; sessionid={get_session}",
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/accounts/password/change/',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "x-asbd-id": "198387" ,
        'x-csrftoken':get_csrftoken,
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'hmac.AR2k9EARzyegqtnhVjLH8VQJTV_MJZXhAEnGJkdqQcc5jNhK',
        'x-instagram-ajax':'1284f5c4fcfb',
        'x-requested-with':'XMLHttpRequest'
        }

    data_change_password = {

        "enc_old_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{current_password}",
        "enc_new_password1": f"#PWD_INSTAGRAM_BROWSER:0:&:{password_one}",
        "enc_new_password2": f"#PWD_INSTAGRAM_BROWSER:0:&:{password_one}"
        }

    req_change_password = requests.post(url_change_password,headers=header_change_password,data=data_change_password)

    if '"status":"ok"' in req_change_password.text:
        with open("Accounts Changed.txt","a") as file:
            file.write(f"{username}:{password_one}\n")
            file.close
        print(f"{Done}. {username} Has Changed Password")
        Done+=1

    elif "This password is too easy to guess. Please create a new one." in req_change_password.text:
        print("This password is too easy to guess. Please create a new one.") 
    

    elif "Create a password at least 6 characters long." in req_change_password.text:
        print(f"{username} Create a new password you haven't used before.")

    else:
        print(f'\n{Error}. {username} {req_change_password.text}')
        Error+=1

def change_password_list():
    global Done , Error
    os.system('cls||clear')

    url_change_password = 'https://www.instagram.com/accounts/password/change/'
    header_change_password = {

        'accept':'*/*',
        'accept-encoding':'gzip,deflate,br',
        'accept-language':'en-US,en;q=0.9,ar;q=0.8',
        'content-length':'672',
        'content-type':'application/x-www-form-urlencoded',
        'cookie': f"csrftoken={get_csrftokens}; sessionid={get_sessions}",
        'origin':'https://www.instagram.com',
        'referer':'https://www.instagram.com/accounts/password/change/',
        'sec-fetch-dest':'empty',
        'sec-fetch-mode':'cors',
        'sec-fetch-site':'same-origin',
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        "x-asbd-id": "198387" ,
        'x-csrftoken':get_csrftokens,
        'x-ig-app-id':'936619743392459',
        'x-ig-www-claim':'hmac.AR2k9EARzyegqtnhVjLH8VQJTV_MJZXhAEnGJkdqQcc5jNhK',
        'x-instagram-ajax':'1284f5c4fcfb',
        'x-requested-with':'XMLHttpRequest'
        }

    data_change_password = {

        "enc_old_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{passwords}",
        "enc_new_password1": f"#PWD_INSTAGRAM_BROWSER:0:&:{new_password}",
        "enc_new_password2": f"#PWD_INSTAGRAM_BROWSER:0:&:{new_password}"
        }

    req_change_password = requests.post(url_change_password,headers=header_change_password,data=data_change_password)

    if '"status":"ok"' in req_change_password.text:
        with open("Accounts Changed.txt","a") as file:
            file.write(f"{usernames}:{new_password}\n")
            file.close
        print(f"{Done}. {usernames} Has Changed Password")
        Done+=1

    elif "This password is too easy to guess. Please create a new one." in req_change_password.text:
        print("This password is too easy to guess. Please create a new one.") 
    

    elif "Create a password at least 6 characters long." in req_change_password.text:
        print(f"{usernames} Create a new password you haven't used before.")

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
