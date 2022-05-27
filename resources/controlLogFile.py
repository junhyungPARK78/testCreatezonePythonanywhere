# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=xowww&logNo=220987549179
# https://pjw48.net/wordpress/2017/03/22/make-json-py/
# https://pjw48.net/wordpress/2017/03/23/json-parsing-py/

import os
import sys

def addTextToLogFile(text):
    # 세이브 데이터 path 지정 Start
    filePath = ""

    if getattr(sys, 'frozen', False):
        #test.exe로 실행한 경우,test.exe를 보관한 디렉토리의 full path를 취득
        filePath = f"{os.path.dirname(os.path.abspath(sys.executable))}/resources"
    else:
        #python test.py로 실행한 경우,test.py를 보관한 디렉토리의 full path를 취득
        filePath = os.path.dirname(os.path.abspath(__file__))

    logFile = f"{filePath}/log.txt"
    # 세이브 데이터 path 지정 End

    with open(logFile, 'a') as f:
        f.write(f"{text}\n")

if __name__=="__main__":
    addTextToLogFile(f"실험 중")