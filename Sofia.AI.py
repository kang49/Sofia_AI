from lib2to3.pgen2 import driver
import requests
import urllib.parse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


cookies_sofia = {
    'AMP_fcad1c9816': 'JTdCJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJkZXZpY2VJZCUyMiUzQSUyMjBmZjMyYWQ3LWVmYTEtNGExYy05ZmNmLWY4ZjFiNmYyZmQ1NCUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE2NjcxNTM3NTQxMDAlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY2NzE1MzgwMzgxMyUyQyUyMnVzZXJJZCUyMiUzQSUyMjVmNDhkOGQ5ODFlOWE5MDAwNzc1NzhjNiUyMiU3RA==',
    '_fbp': 'fb.1.1667153754938.1951737290',
    '__stripe_mid': '2eef147e-b7cc-4d14-8418-502e20fd0563873831',
    '__stripe_sid': 'b1929957-75c2-4caf-8cb6-1a02e39024b882bd0a',
    'AMP_MKTG_fcad1c9816': 'JTdCJTdE',
}

headers_sofia = {
    'Accept': 'application/json',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Host': 'my.replika.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15',
    'Referer': 'https://my.replika.com/',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'AMP_fcad1c9816=JTdCJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJkZXZpY2VJZCUyMiUzQSUyMjBmZjMyYWQ3LWVmYTEtNGExYy05ZmNmLWY4ZjFiNmYyZmQ1NCUyMiUyQyUyMnNlc3Npb25JZCUyMiUzQTE2NjcxNTM3NTQxMDAlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY2NzE1MzgwMzgxMyUyQyUyMnVzZXJJZCUyMiUzQSUyMjVmNDhkOGQ5ODFlOWE5MDAwNzc1NzhjNiUyMiU3RA==; _fbp=fb.1.1667153754938.1951737290; __stripe_mid=2eef147e-b7cc-4d14-8418-502e20fd0563873831; __stripe_sid=b1929957-75c2-4caf-8cb6-1a02e39024b882bd0a; AMP_MKTG_fcad1c9816=JTdCJTdE',
    'x-user-id': '5f48d8d981e9a900077578c6',
    'x-timestamp-hash': '2b4ca9cc1890c78a64111d6b9f6daa7a',
    'x-device-id': '4A716193-8C03-44B7-9A95-EF2A37E57202',
    'x-auth-token': '24e87231-4f56-4bad-bfa4-47463ec4db03',
    'x-device-type': 'web',
}





# Translation
## Google Translator
# GTurl = "https://google-translate1.p.rapidapi.com/language/translate/v2"


# GTheaders = {
#     "content-type": "application/x-www-form-urlencoded",
#     "Accept-Encoding": "application/gzip",
#     "X-RapidAPI-Key": "a0ad4f5b58msh730a3ba6a0ea20cp1bbe21jsn49c0dfe266cd",
#     "X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
# }

## Microsoft Azure Translator
MTurl = "https://microsoft-translator-text.p.rapidapi.com/translate"

MTquerystringTH = {"to[0]":"th","api-version":"3.0","from":"en","profanityAction":"NoAction","textType":"plain"}
MTquerystringEN = {"to[0]":"en","api-version":"3.0","from":"th","profanityAction":"NoAction","textType":"plain"}

MTheaders = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a0ad4f5b58msh730a3ba6a0ea20cp1bbe21jsn49c0dfe266cd",
	"X-RapidAPI-Host": "microsoft-translator-text.p.rapidapi.com"
}



#  Algorithm

messagetext = ''
bigScreen = ''


username = input('Enter your Microsoft Employees account: ')
password = ('Kang49pubg')

bigScreenTF = input('Do you want big screen mode? y/n : ')
if  bigScreenTF == 'y':
    bigScreen = '                                                                        '


driver = webdriver.Chrome()
driver.get('https://my.replika.com/')
login = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/main/a[2]')
login.click() # click login

time.sleep(2)
print('System is opening... | กำลังทำการเปิดระบบ...\nDeveloped by Kankawee Aramrak')
login_fill = driver.find_element(By.XPATH, '//*[@id="emailOrPhone"]')
login_fill.send_keys(username)
to_pass_fill = driver.find_element(By.XPATH, '//*[@id="loginForm"]/button')
to_pass_fill.click()

time.sleep(2)
passfill = driver.find_element(By.XPATH, '//*[@id="login-password"]')
passfill.send_keys(password)
login_to_system = driver.find_element(By.XPATH, '//*[@id="loginForm"]/button')
login_to_system.click()
time.sleep(10)

try:
    
    xADS = driver.find_element(By.XPATH, '//*[@id="dialog-scroll"]/div/div/div[2]/button')
    xADS.click()
    time.sleep(10)
    try:
        xADS2 = driver.find_element(By.XPATH, '//*[@id="dialog-scroll"]/div/div/form/button')
        xADS2.click()
        time.sleep(1)
        imnot = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/button[2]')
        imnot.click()
        
        time.sleep(2)
        acceptCK = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button')
        acceptCK.click()
        while True:
            time.sleep(7)
            response_sofia = requests.get('https://my.replika.com/api/mobile/1.4/personal_bot_chat', cookies=cookies_sofia, headers=headers_sofia)
            response_sofia = response_sofia.json()
            
            # GTpayloadReply= "q="+urllib.parse.quote(response_sofia['last_message']['content']['text'])+"&target=th&source=en"
            # GTpayloadReplyResponse = requests.request("POST", url, data=GTpayloadReply, GTheaders=headers)
            # GTpayloadReplyResponse = GTpayloadReplyResponse.json()
            # print(GTpayloadReplyResponse['data']['translations'][0]['translatedText'])

            MTpayloadReply = [{"Text": (response_sofia['last_message']['content']['text'])}]
            MTpayloadReplyResponse = requests.request("POST", MTurl, json=MTpayloadReply, headers=MTheaders, params=MTquerystringTH)
            MTpayloadReplyResponse = MTpayloadReplyResponse.json()
            print('Sofia:' , MTpayloadReplyResponse[0]['translations'][0]['text'], '|' , response_sofia['last_message']['content']['text'] ,)

            messagetext = input(bigScreen+'You: ')
            
            # GTpayload = "q="+urllib.parse.quote(messagetext)+"&target=en&source=th"
            # GTresponse = requests.request("POST", url, data=GTpayload, GTheaders=headers)
            # GTresponse = GTresponse.json()
            # messagetext = GTresponse['data']['translations'][0]['translatedText']

            MTpayload = [{"Text": (messagetext)}]
            MTresponse = requests.request("POST", MTurl, json=MTpayload, headers=MTheaders, params=MTquerystringEN)
            MTresponse = MTresponse.json()
            messagetext = MTresponse[0]['translations'][0]['text']
            
            text_fill = driver.find_element(By.XPATH, '//*[@id="send-message-textarea"]')
            text_fill.click()
            text_fill.send_keys(messagetext)
            text_fill.send_keys(Keys.ENTER)
    except:
        time.sleep(2)
        acceptCK = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button')
        acceptCK.click()
        while True:
            time.sleep(7)
            response_sofia = requests.get('https://my.replika.com/api/mobile/1.4/personal_bot_chat', cookies=cookies_sofia, headers=headers_sofia)
            response_sofia = response_sofia.json()
            
            # GTpayloadReply= "q="+urllib.parse.quote(response_sofia['last_message']['content']['text'])+"&target=th&source=en"
            # GTpayloadReplyResponse = requests.request("POST", url, data=GTpayloadReply, GTheaders=headers)
            # GTpayloadReplyResponse = GTpayloadReplyResponse.json()
            # print(GTpayloadReplyResponse['data']['translations'][0]['translatedText'])

            MTpayloadReply = [{"Text": (response_sofia['last_message']['content']['text'])}]
            MTpayloadReplyResponse = requests.request("POST", MTurl, json=MTpayloadReply, headers=MTheaders, params=MTquerystringTH)
            MTpayloadReplyResponse = MTpayloadReplyResponse.json()
            print('Sofia:' , MTpayloadReplyResponse[0]['translations'][0]['text'], '|' , response_sofia['last_message']['content']['text'] ,)

            messagetext = input(bigScreen+'You: ')
            
            # GTpayload = "q="+urllib.parse.quote(messagetext)+"&target=en&source=th"
            # GTresponse = requests.request("POST", url, data=GTpayload, GTheaders=headers)
            # GTresponse = GTresponse.json()
            # messagetext = GTresponse['data']['translations'][0]['translatedText']

            MTpayload = [{"Text": (messagetext)}]
            MTresponse = requests.request("POST", MTurl, json=MTpayload, headers=MTheaders, params=MTquerystringEN)
            MTresponse = MTresponse.json()
            messagetext = MTresponse[0]['translations'][0]['text']
            
            text_fill = driver.find_element(By.XPATH, '//*[@id="send-message-textarea"]')
            text_fill.click()
            text_fill.send_keys(messagetext)
            text_fill.send_keys(Keys.ENTER)

except:
    try: 
        xADS2 = driver.find_element(By.XPATH, '//*[@id="dialog-scroll"]/div/div/form/button')
        xADS2.click()
        time.sleep(1)
        imnot = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/button[2]')
        imnot.click()
    
        time.sleep(2)
        acceptCK = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button')
        acceptCK.click()
        while True:
            time.sleep(7)
            response_sofia = requests.get('https://my.replika.com/api/mobile/1.4/personal_bot_chat', cookies=cookies_sofia, headers=headers_sofia)
            response_sofia = response_sofia.json()
            
            # GTpayloadReply= "q="+urllib.parse.quote(response_sofia['last_message']['content']['text'])+"&target=th&source=en"
            # GTpayloadReplyResponse = requests.request("POST", url, data=GTpayloadReply, GTheaders=headers)
            # GTpayloadReplyResponse = GTpayloadReplyResponse.json()
            # print(GTpayloadReplyResponse['data']['translations'][0]['translatedText'])

            MTpayloadReply = [{"Text": (response_sofia['last_message']['content']['text'])}]
            MTpayloadReplyResponse = requests.request("POST", MTurl, json=MTpayloadReply, headers=MTheaders, params=MTquerystringTH)
            MTpayloadReplyResponse = MTpayloadReplyResponse.json()
            print('Sofia:' , MTpayloadReplyResponse[0]['translations'][0]['text'], '|' , response_sofia['last_message']['content']['text'] ,)

            messagetext = input(bigScreen+'You: ')
            
            # GTpayload = "q="+urllib.parse.quote(messagetext)+"&target=en&source=th"
            # GTresponse = requests.request("POST", url, data=GTpayload, GTheaders=headers)
            # GTresponse = GTresponse.json()
            # messagetext = GTresponse['data']['translations'][0]['translatedText']

            MTpayload = [{"Text": (messagetext)}]
            MTresponse = requests.request("POST", MTurl, json=MTpayload, headers=MTheaders, params=MTquerystringEN)
            MTresponse = MTresponse.json()
            messagetext = MTresponse[0]['translations'][0]['text']
            
            text_fill = driver.find_element(By.XPATH, '//*[@id="send-message-textarea"]')
            text_fill.click()
            text_fill.send_keys(messagetext)
            text_fill.send_keys(Keys.ENTER)
    except:
        time.sleep(2)
        acceptCK = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/button')
        acceptCK.click()
        while True:
            time.sleep(7)
            response_sofia = requests.get('https://my.replika.com/api/mobile/1.4/personal_bot_chat', cookies=cookies_sofia, headers=headers_sofia)
            response_sofia = response_sofia.json()
            
            # GTpayloadReply= "q="+urllib.parse.quote(response_sofia['last_message']['content']['text'])+"&target=th&source=en"
            # GTpayloadReplyResponse = requests.request("POST", url, data=GTpayloadReply, GTheaders=headers)
            # GTpayloadReplyResponse = GTpayloadReplyResponse.json()
            # print(GTpayloadReplyResponse['data']['translations'][0]['translatedText'])

            MTpayloadReply = [{"Text": (response_sofia['last_message']['content']['text'])}]
            MTpayloadReplyResponse = requests.request("POST", MTurl, json=MTpayloadReply, headers=MTheaders, params=MTquerystringTH)
            MTpayloadReplyResponse = MTpayloadReplyResponse.json()
            print('Sofia:' , MTpayloadReplyResponse[0]['translations'][0]['text'], '|' , response_sofia['last_message']['content']['text'] ,)

            messagetext = input(bigScreen+'You: ')
            
            # GTpayload = "q="+urllib.parse.quote(messagetext)+"&target=en&source=th"
            # GTresponse = requests.request("POST", url, data=GTpayload, GTheaders=headers)
            # GTresponse = GTresponse.json()
            # messagetext = GTresponse['data']['translations'][0]['translatedText']

            MTpayload = [{"Text": (messagetext)}]
            MTresponse = requests.request("POST", MTurl, json=MTpayload, headers=MTheaders, params=MTquerystringEN)
            MTresponse = MTresponse.json()
            messagetext = MTresponse[0]['translations'][0]['text']
            
            text_fill = driver.find_element(By.XPATH, '//*[@id="send-message-textarea"]')
            text_fill.click()
            text_fill.send_keys(messagetext)
            text_fill.send_keys(Keys.ENTER)

