# https://docs.python.org/3.9/library/email.examples.html
# https://yeolco.tistory.com/93

def sendMail(mailContent, mailSubject, mailSender, mailReceiverBcc):
    import smtplib
    from email.mime.text import MIMEText
    from email.message import EmailMessage

    # 보낼 메시지 설정
    msg = EmailMessage()
    msg.set_content(mailContent)
    msg['Subject'] = mailSubject
    msg['From'] = mailSender
    msg['To'] = ''
    msg['Bcc'] = mailReceiverBcc

    # print(msg.keys())

    # 메일 발송
    mailSession = smtplib.SMTP('smtp.gmail.com', 587) # 세션 생성
    mailSession.starttls() # TLS 보안 시작
    mailSession.login('createzonebot@gmail.com', 'jedzbhlcxotjqyln') # 로그인 인증
    mailSession.send_message(msg)
    mailSession.quit() # 세션 종료

if __name__=="__main__":
    import time

    now = time.strftime('%Y-%m-%d %H:%M:%S')

    mailContent = f'ruliweb.com\n의 접속 상태가 「접속 가능」에서 「접속 불가능」으로 바뀌었습니다.\n의 접속 상태가 「접속 불가능」에서 「접속 가능」으로 바뀌었습니다.\n\n변경 확인 시간 : {now}'
    mailSubject = "`ruliweb.com` 에 접속 가능 여부에 변경이 있었습니다."
    mailSender = 'createzonebot@gmail.com'
    mailReceiverBcc = 'createzone+TEST@gmail.com, createzone+TEST2@gmail.com'
    
    sendMail(mailContent, mailSubject, mailSender, mailReceiverBcc)