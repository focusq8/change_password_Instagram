import requests
import os

def login():
    global password ,username , new_password , get_sessions , get_csrftoken , counter

    file = input("\n\n[+] Enter Your File Name: ")
    counts_proxies = sum(1 for line in open(file))
    print(f"\n{counts_proxies} usernames\n\n")
    if os.stat(file).st_size == 0:
        print("file is empty")
        login()

    new_password = len(input("[+] Enter The New Password: "))
    if new_password <=6:
        print("new password is less than 6 password")
        login()
    open_file = open(file,"r").read().splitlines()

    for list in open_file:
        username = list.split(":")[0]
        password = list.split(":")[1]

        url = 'https://www.instagram.com/accounts/login/ajax/'

        head = {
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

        data = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false',
            'trustedDeviceRecords': '{}'
            }

        req_login = requests.post(url,headers=head,data=data)

        if '"authenticated":false' in req_login.text:
            input(f'\nUsername Or Password Is Wrong !\nPlease Check Your Username And Password\n\n')
            exit()

        elif '"checkpoint_url"' in req_login.text:
            input(f"username Is Secured !\nPlease Activate Your code To login\n\n")
            exit()
    
        elif "checkpoint_challenge_required" in req_login.text:
            input(f"has Has Two Factor authentication\nPlease Turn It Off And Try Again\n\n")
            exit()
    
        elif '"inactive user"' in req_login.text:
            input(f'username Banned Account\n\n')
            exit()

        elif '"authenticated":true' in req_login.text:
            print(f"[{counter}] log in")
            counter+=1

            get_sessions = req_login.cookies['sessionid']
            get_csrftoken = req_login.cookies.get_dict()['csrftoken']
            change()
        
        else:
            input(f"\n\nCheck On Your File Please\nUsername And Password Must Be Like\nsalem:salem" )
            exit()

def change():
    global counter
     
    url2 = 'https://www.instagram.com/accounts/password/change/'
    head2 = {
            'accept':'*/*',
            'accept-encoding':'gzip,deflate,br',
            'accept-language':'en-US,en;q=0.9,ar;q=0.8',
            'content-length':'672',
            'content-type':'application/x-www-form-urlencoded',
            'cookie': f"csrftoken={get_csrftoken}; sessionid={get_sessions}",
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

    data2 = {
            "enc_old_password": f"#PWD_INSTAGRAM_BROWSER:0:&:{password}",
            "enc_new_password1": f"#PWD_INSTAGRAM_BROWSER:0:&:{new_password}",
            "enc_new_password2": f"#PWD_INSTAGRAM_BROWSER:0:&:{new_password}"
            }

    login_Change = requests.post(url2,headers=head2,data=data2)

    if '"status":"ok"' in login_Change.text:
        with open("Accounts Changed.txt","a") as file:
            file.write(f"{username}:{new_password}\n")
            file.close

        print(f"[{counter}] Done Changed it")
        counter+=1
    elif "This password is too easy to guess. Please create a new one." in login_Change.text:
        print("This password is too easy to guess. Please create a new one.") 
        change()
    
    elif "Your old password was entered incorrectly" in login_Change.text:
        print("Your old password was entered incorrectly")

    else:
        input(login_Change.text)

def starter():
    global counter
if __name__ == '__main__':
    counter=1    
    login()
