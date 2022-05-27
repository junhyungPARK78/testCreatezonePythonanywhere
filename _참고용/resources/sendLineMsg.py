# 파이썬에서 LINE 메세지 보내기
# https://kwonkyo.tistory.com/520

import requests

def sendLineMsg(content, receiver):
    try:
        TARGET_URL = 'https://notify-api.line.me/api/notify'
        TOKENS = {
            True: 'TsPKQupoFJYa0HrVMmliPHbnyK40f2XrCZcN41lVNWd', # 모두가 보는 방
            False: 'AbOPMw01vcCuQcovpbvJQq6X5WKS4wCsxgKduaLuDxr'} # 나만 보는 방
        TOKEN = TOKENS[receiver]
        print(TOKEN)
        headers={'Authorization': 'Bearer ' + TOKEN}
        data={'message': f"\n{content}"}

        response = requests.post(TARGET_URL, headers=headers, data=data)

    except Exception as ex:
        print(ex)
