import schedule
import time
from resources import canConnectWeb

def testFunction():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"스케쥴 실행중... : {now}")

schedule.every(3).seconds.do(testFunction) # step3.실행 주기 설정
# schedule.every(30).minutes.do(checkWebsite) # step3.실행 주기 설정

testFunction()

while True: # step4.스캐쥴 시작
    schedule.run_pending()
    time.sleep(1)