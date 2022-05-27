import schedule
import time
from resources import canConnectWeb
from resources import controlLogFile

def whatTimeIsNow():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    resultText = f"코드 실행 시간 : {now}"
    # print(resultText)

    controlLogFile.addTextToLogFile(resultText)


def isRuliwebConnect():
    result = canConnectWeb.canConnectWeb("https://ruliweb.com")
    resultText = f"루리웹에 접속 가능하다 : {result}"
    # print(resultText)

    controlLogFile.addTextToLogFile(resultText)

schedule.every(5).seconds.do(whatTimeIsNow) # step3.실행 주기 설정
schedule.every(10).seconds.do(isRuliwebConnect) # step3.실행 주기 설정
# schedule.every(30).minutes.do(checkWebsite) # step3.실행 주기 설정

whatTimeIsNow()
isRuliwebConnect()

while True: # step4.스캐쥴 시작
    schedule.run_pending()
    time.sleep(1)