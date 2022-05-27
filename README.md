# testCreatezonePythonanywhere

**파이썬 버전**
Python 3.9.13

**pythonanywhere**
https://www.pythonanywhere.com/user/testCreatezonePythonanywhere/

**pyinstaller 사용법**
https://coding-kindergarten.tistory.com/84
https://taedi.net/11
먼저 spec파일을 만들어두고 : `pyinstaller --onefile --name testCreatezonePythonanywhere main.py`
그 후에는 이 명령으로 동일한 스펙의 실행파일을 만들 수 있다. : `pyinstaller testCreatezonePythonanywhere.spec`

**VS code에서 가상환경 구축하는 방법**
https://mr-spock.tistory.com/19

**명령어 정리**
- 가상 환경 만들기
  `python3 -m venv .venv`
- 가상 환경 삭제
  `deactivate`
  `sudo rm -rf .venv`
- 설치된 패키지 확인
  `pip freeze`
- 설치된 패키지를 관리하는 requirements.txt 파일 만들기
  `pip freeze > requirements.txt`
- requirements.txt 에 적혀있는 패키지 설치하기
  `pip install -r requirements.txt`
- requirements.txt 에 적혀있는 패키지 삭제하기
  `pip uninstall -r requirements.txt -y`
- 가상환경 터미널에서 활성화시키기
  `source pTest_venv/bin/activate`
