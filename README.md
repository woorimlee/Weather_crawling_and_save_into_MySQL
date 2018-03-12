# Weather_crawling_and_save_into_MySQL
## 사용방법

0. 기본적으로 MySQL이 설치되어 있고, 모듈이 import 되어 있다고 전제한다.

1. 변수 my_passwd 에는 나중에 연결 할 MYSQL의 접속하고자 하는 user의 비밀번호를 적는다.

2. 파이썬 파일을 IDLE 같은 툴로 running 시켜도 되고, 더블 클릭하여 콘솔 창으로 출력해도 된다.
![2](https://user-images.githubusercontent.com/36785390/37285031-fb84fd0e-2640-11e8-954f-45322b46c260.png)

3. 매일 날씨 정보를 업데이트 하기 위해 Windows(OS)의 Task Scheduler를 사용한다.

url은 다음과 같다.
url = "http://weather.naver.com/rgn/cityWetrMain.nhn"
![1](https://user-images.githubusercontent.com/36785390/37284762-2497ecd4-2640-11e8-8051-ea3224bdbe38.png)

사용 방법은 아래의 링크를 참조하자.
http://fnmj.tistory.com/19
