def canConnectWeb(url):
    # https://appia.tistory.com/293

    import requests

    try:
        result=requests.get(url)

    except:
        return False

    else:
        if result.status_code == 200:
            return True
        else:
            return False
