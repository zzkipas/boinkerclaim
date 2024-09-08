import requests
import time

url = 'https://boink.astronomica.io/api/rewardedActions/getRewardedActionList?p=web&t=1725763608449'
CLAIM_URL = 'https://boink.astronomica.io/api/rewardedActions/claimRewardedAction/'
AUTH_KEY = input(str("AUTH KEY: "))

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': f'{AUTH_KEY}',
    'priority': 'u=1, i',
    'referer': 'https://boink.astronomica.io/earn',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
}

response = requests.get(url, headers=headers)
task = response.json()
for i in task:
    url_claim = f'https://boink.astronomica.io/api/rewardedActions/claimRewardedAction/{i["nameId"]}?p=web'
    url_click = f'https://boink.astronomica.io/api/rewardedActions/rewardedActionClicked/{i["nameId"]}?p=web'
    headers_claim = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': f'{AUTH_KEY}',
        'content-type': 'application/json',
        'origin': 'https://boink.astronomica.io',
        'priority': 'u=1, i',
        'referer': 'https://boink.astronomica.io/earn',
        'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Mobile Safari/537.36'
    }

    
    response_click = requests.post(url_click, headers=headers_claim, json={})
    print(response_click.text)
    time.sleep(10)
    response_claim = requests.post(url_claim, headers=headers_claim, json={})
    print(response_claim.text)
