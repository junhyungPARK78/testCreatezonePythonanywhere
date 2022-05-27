# https://wikidocs.net/137924

import schedule
import time
from resources import withJson
from resources import canConnectWeb
from resources import sendMail
from resources import sendLineMsg

def checkWebsite():
    data = withJson.openSaveData()
    oldStatus = True
    newStatus = True

    print(f"현재 시간 : {time.strftime('%Y-%m-%d %H:%M:%S')}")

    for keyWebpage in data.keys():
        oldStatus = data[keyWebpage]['connectStatus']
        newStatus = canConnectWeb.canConnectWeb(keyWebpage)

        # 세이브 데이터의 웹페이지 접속가능 여부와 현재 상태의 비교
        if oldStatus == newStatus:
            print((
                f"=============================\n"
                f"`{keyWebpage}`\n"
                f"=============================\n"
                f"접속 스테이터스가 변하지 않았습니다."
            ))
        else:
            print((
                f"=============================\n"
                f"`{keyWebpage}`\n"
                f"=============================\n"
                f"접속 스테이터스가 변했습니다."
            ))

            # 메일 내용 생성
            statusName = {True: "접속 가능", False: "접속 불가능"}
            mailContent = (
                f"=============================\n"
                f"확인 시간 : {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
                f"=============================\n\n"
                f"`{keyWebpage}`\n"
                f"접속 상태가 「{statusName[oldStatus]}」에서 「{statusName[newStatus]}」으로 바뀌었습니다."
            )
            mailSubject = f"{keyWebpage}에 접속 가능 여부에 변경이 있었습니다."
            mailSender = 'createzonebot@gmail.com'
            mailReceiverBcc = ', '.join(s for s in data[keyWebpage]["mails"])

            # 스테이터스 변경을 세이브 데이터에 적용
            data[keyWebpage]['connectStatus'] = newStatus
            withJson.writeSaveData(data)

            # 메일 발송하기
            sendMail.sendMail(mailContent, mailSubject, mailSender, mailReceiverBcc)

            # 라인 메세지 보내기
            if data[keyWebpage]['shouldSendLineMsgAll']:
                sendLineMsg.sendLineMsg(mailContent, True)
            else:
                sendLineMsg.sendLineMsg(mailContent, False)

def testFunction():
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    print(f"스케쥴 실행중... : {now}")

# schedule.every(3).seconds.do(testFunction) # step3.실행 주기 설정
schedule.every(30).minutes.do(checkWebsite) # step3.실행 주기 설정

checkWebsite()

while True: # step4.스캐쥴 시작
    schedule.run_pending()
    time.sleep(1)

