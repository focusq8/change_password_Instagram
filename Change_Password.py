import requests

def login():
    global file , password ,username , new_password , get_sessions , get_csrftoken , counter

    new_password = input("[+] Enter The New Password: ")
    open_file = open(file,"r").read().splitlines()

    for combo in open_file:
        username = combo.split(":")[0]
        password = combo.split(":")[1]

        url = 'https://www.instagram.com/accounts/login/ajax/'

        head = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9,ar;q=0.8",
            "content-length": "318",
            "content-type": "application/x-www-form-urlencoded",
            "cookie": "mid=YabB5gALAAFbVb5mBZr7GHIfpIvz; ig_did=582CE9B8-0009-4E09-BBB3-C3A2C07A97EC; ig_nrcb=1; csrftoken=MPouk3yseSDTnA4bNbCYoxQTl0JbqsYg",
            "origin": "https://www.instagram.com",
            "referer": "https://www.instagram.com/",
            "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96',
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "x-asbd-id": "198387",
            "x-csrftoken": "MPouk3yseSDTnA4bNbCYoxQTl0JbqsYg",
            "x-ig-app-id": "936619743392459",
            "x-ig-www-claim": "hmac.AR2k9EARzyegqtnhVjLH8VQJTV_MJZXhAEnGJkdqQcc5jNhK",
            "x-instagram-ajax": "1284f5c4fcfb",
            "x-requested-with": "XMLHttpRequest"
            }

        data = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
            'queryParams': {},
            'optIntoOneTap': 'false'
            }

        login = requests.post(url,headers=head,data=data)

        if '"authenticated":false' in login.text:
            input(f'\nUsername Or Password Is Wrong !\nPlease Check Your Username And Password\n\n')
            exit()

        elif '"checkpoint_url"' in login.text:
            input(f"username Is Secured !\nPlease Activate Your code To login\n\n")
            exit()
    
        elif "checkpoint_challenge_required" in login.text:
            input(f"has Has Two Factor authentication\nPlease Turn It Off And Try Again\n\n")
            exit()
    
        elif '"inactive user"' in login.text:
            input(f'username Banned Account\n\n')
            exit()

        elif '"authenticated":true' in login.text:
            print(f"[{counter}] log in")
            counter+=1

            get_sessions = login.cookies['sessionid']
            get_csrftoken = login.cookies.get_dict()['csrftoken']
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

    login_Change = requests.post(url2,headers=head2,data=data2).text

    if '"status":"ok"' in login_Change:
        with open("Accounts Changed.txt","a") as file:
            file.write(f"{username}:{new_password}\n")
            file.close

        print(f"[{counter}] Done Changed it")
        counter+=1
        
    else:
        input("Error")

def proxy():
    global file , counter
if __name__ == '__main__':

    file = input("[+] Enter Yout File Name: ")
    if '.txt' in file:
        pass
    else:
        files  = file + '.txt'
    counter=1
    login()
